"""Capture a batch's NACSOS assignment scopes from the live project.

Replaces hand-editing assignment_scope_ids.json: lists the scopes created
after the batch's import, with completion counts, and writes the selected
IDs to the file the export rules consume.
"""

import asyncio
import json
import sys
from datetime import UTC, datetime, timedelta

import typer
from InquirerPy import inquirer
from nacsos_data.db import get_engine_async
from nacsos_data.db.crud.annotations import (
    read_assignment_counts_for_scope,
    read_assignment_scopes_for_project,
)
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from what_works_repo.batch import Batch
from what_works_repo.settings import settings

# allowance for clock skew between this machine and the NACSOS database
CUTOFF_SLACK = timedelta(hours=1)


def _as_utc(dt: datetime) -> datetime:
    return dt if dt.tzinfo else dt.replace(tzinfo=UTC)


async def candidate_scopes(batch: Batch) -> list[dict]:
    """Project scopes created after the batch was imported, with counts.

    DEET human-resolution scopes cover the same documents but are created by
    the pipeline, so they are excluded by their name suffix.
    """
    cutoff = (
        datetime.fromtimestamp(batch.imported.stat().st_mtime, tz=UTC) - CUTOFF_SLACK
    )
    db_engine = get_engine_async("config/.env")
    async with db_engine.session() as session:
        scopes = await read_assignment_scopes_for_project(
            project_id=settings.nacsos.project_id, session=session
        )
        rows = []
        for scope in scopes:
            created = _as_utc(scope.time_created) if scope.time_created else None
            if created is None or created < cutoff:
                continue
            if (scope.name or "").endswith("__human_resolution"):
                continue
            counts = await read_assignment_counts_for_scope(
                assignment_scope_id=str(scope.assignment_scope_id), session=session
            )
            rows.append(
                {
                    "scope_id": str(scope.assignment_scope_id),
                    "name": scope.name,
                    "time_created": created,
                    **counts.model_dump(),
                }
            )
    return sorted(rows, key=lambda r: r["time_created"])


console = Console()


def _summary(row: dict) -> str:
    complete = row["num_open"] == row["num_partial"] == 0
    status = (
        "complete"
        if complete
        else f"{row['num_open']} open, {row['num_partial']} partial"
    )
    mark = "  " if complete else "(!)"
    return (
        f"{mark} {row['name']}  |  {row['num_total']} assignments, {status}"
        f"  |  {row['time_created']:%d %b %H:%M}"
    )


_BANNER_KEYS = [
    ("ARROWS", "move the cursor"),
    ("SPACE", "toggle a scope"),
    ("ENTER", "confirm the selection and continue the pipeline"),
    ("CTRL-C", "cancel: nothing is written, re-run snakemake later"),
]


def _banner(batch_n: int) -> None:
    body = Text()
    body.append(
        "Select assignment scope(s) belonging to this batch in NACSOS.\n\n"
        "Export will fail for incomplete scopes\n\n"
    )
    for key, desc in _BANNER_KEYS:
        body.append(f"  {key:<8}", style="bold")
        body.append(desc + "\n")
    console.print(
        Panel(
            body,
            title=(f"[bold]Batch {batch_n}[/] - select assignment scope(s)"),
            title_align="left",
            border_style="yellow",
        )
    )


def _choose(rows: list[dict]) -> list[dict]:
    """Arrow-key / space multi-select, same widget family as the DEET wizard."""
    try:
        chosen = inquirer.checkbox(
            message="Scopes created since this batch was imported:",
            choices=[{"name": _summary(r), "value": r} for r in rows],
            default=rows if len(rows) == 1 else [],
            validate=lambda res: len(res) > 0,
            invalid_message="Select at least one scope.",
        ).execute()
        incomplete = [r for r in chosen if r["num_open"] or r["num_partial"]]
        if (
            incomplete
            and not inquirer.confirm(
                message=f"{len(incomplete)} selected scope(s) still have open or "
                "partial assignments, which the export will refuse. Continue?",
                default=False,
            ).execute()
        ):
            raise typer.Abort
    except KeyboardInterrupt:
        raise typer.Abort from None
    return chosen


def main(batch_n: int):
    """Write the batch's assignment_scope_ids.json from interactively chosen scopes."""
    console.print("\n\n\n")
    batch = Batch(batch_n)
    if not batch.imported.exists():
        print(f"{batch.imported} not found - has this batch been imported yet?")
        raise typer.Exit(1)
    if not sys.stdin.isatty():
        # ahead of the DB query: this path needs no data, and a missing DB
        # tunnel would otherwise crash the headless run
        console.print(
            "[yellow]No terminal attached:[/] write the chosen scope IDs to "
            f"[bold]{batch.scope_ids}[/] as a JSON array of UUID strings, then "
            "re-run snakemake."
        )
        raise typer.Exit(1)
    rows = asyncio.run(candidate_scopes(batch))
    if not rows:
        imported_at = datetime.fromtimestamp(batch.imported.stat().st_mtime)
        console.print(
            f"[yellow]No new scopes in project {settings.nacsos.project_id} since "
            f"the import at {imported_at:%Y-%m-%d %H:%M}.[/] Ask the team to "
            "create the assignment scope(s) in NACSOS, then [bold]re-run "
            "snakemake[/] to try again."
        )
        raise typer.Exit(1)
    _banner(batch.number)
    try:
        chosen = _choose(rows)
    except typer.Abort:
        console.print(
            "[yellow]Cancelled - nothing written.[/] When the scope(s) are "
            "ready, re-run snakemake to choose again."
        )
        raise typer.Exit(130) from None
    batch.scope_ids.write_text(
        json.dumps([r["scope_id"] for r in chosen], indent=2) + "\n"
    )
    console.print(
        f"[green]Wrote {len(chosen)} scope id(s)[/] to [bold]{batch.scope_ids}[/]"
    )


if __name__ == "__main__":
    typer.run(main)
