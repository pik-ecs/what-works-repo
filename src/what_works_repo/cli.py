"""Single console entry point: `wwcs <subcommand>`.

Reporting commands call the module functions directly; NACSOS/DEET-touching
commands can be added below with the try/import guard ic1 uses, so `wwcs
figures` stays runnable without the nacsos extra.
"""

from pathlib import Path
from typing import Annotated

import typer

from what_works_repo.constants import FIGURES_DIR, ZOTERO_DIR
from what_works_repo.reporting import plots

app = typer.Typer(help="Reporting and docs-figure commands.")


@app.callback()
def main() -> None:
    """Keep Typer in group mode while there is a single command."""


@app.command()
def figures(
    min_shared: int = 25,
    output_dir: Annotated[
        Path, typer.Option(help="Where to write the SVGs.")
    ] = FIGURES_DIR,
    exclude_batches: Annotated[
        list[str] | None,
        typer.Option(
            "-x",
            "--exclude-batches",
            help="Batch numbers to drop, comma-separated. Repeatable.",
        ),
    ] = None,
) -> None:
    """Build every docs figure."""
    exclude = [
        int(tok) for opt in exclude_batches or [] for tok in opt.split(",") if tok
    ]
    plots.annotation_progress(output_dir / "progress.svg", exclude=exclude)
    plots.render_irr(min_shared=min_shared, output_dir=output_dir, exclude=exclude)


@app.command()
def zotero_export(
    output: Annotated[
        Path,
        typer.Option("-o", "--output", help="Where to write the RIS file."),
    ] = ZOTERO_DIR / "included.ris",
    refresh: Annotated[
        bool,
        typer.Option(
            help="Force a re-fetch of the cached scopus_id -> NACSOS item_id table."
        ),
    ] = False,
) -> None:
    """Export the locally-included items as RIS for a shared Zotero library.

    Each record keeps its NACSOS ID in the Extra field, so imported items can be
    mapped back to NACSOS records and to their PDF attachments later.
    """
    from what_works_repo.zotero_export import run

    records, with_id = run(output, refresh=refresh)
    typer.echo(
        f"Wrote {records} records ({with_id} with a NACSOS ID in Extra) to {output}"
    )
