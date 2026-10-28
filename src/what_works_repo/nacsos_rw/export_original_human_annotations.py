"""Export original (pre-resolution) human annotations, if complete."""

import asyncio
from pathlib import Path
from typing import cast

import pandas as pd
import typer
from nacsos_data.db import get_engine_async
from nacsos_data.db.crud.annotations import read_assignment_counts_for_scope
from nacsos_data.db.crud.items import read_any_item_by_item_id
from nacsos_data.db.crud.users import user_ids_to_names
from nacsos_data.models.items import AcademicItemModel
from nacsos_data.util.annotations import read_item_annotations

from what_works_repo.nacsos_rw.export_human_annotations import read_scopes
from what_works_repo.settings import settings


async def export_annotations(scope_id: str) -> list[dict]:
    db_engine = get_engine_async("config/.env")

    counts = await read_assignment_counts_for_scope(
        assignment_scope_id=scope_id, db_engine=db_engine
    )
    if counts.num_open > 0 or counts.num_partial > 0:
        raise ValueError(
            f"Scope has incomplete assignments: "
            f"{counts.num_open} open, {counts.num_partial} partial"
        )

    async with db_engine.session() as session:
        annotations = await read_item_annotations(
            session=session,
            assignment_scope_id=scope_id,
            ignore_hierarchy=True,
            ignore_repeat=True,
        )
        usernames = await user_ids_to_names(session=session)

    annotations = [
        a
        for a in annotations
        if a.key == settings.nacsos.inclusion_key and a.value_int is not None
    ]

    annotations_to_export = []

    for annotation in annotations:
        item = await read_any_item_by_item_id(annotation.item_id, "academic", db_engine)
        item = cast(AcademicItemModel, item)
        if not item:
            raise ValueError("Item not found")
        annotations_to_export.append(
            {
                "document_id": str(item.scopus_id),
                "name": item.title,
                "abstract": item.text,
                "annotator": usernames[str(annotation.user_id)],
                settings.nacsos.inclusion_key: annotation.value_int,
            }
        )
    return annotations_to_export


async def gather_exports(scope_ids: list[str]) -> list[dict]:
    results = await asyncio.gather(
        *[export_annotations(scope_id) for scope_id in scope_ids]
    )
    return [row for rows in results for row in rows]


def main(scope_path: Path, output_path: Path):
    """
    Retrieve the original annotations of each human annotator in a scope.

    Write results to a csv.
    """
    scope_ids = read_scopes(scope_path)
    all_rows = asyncio.run(gather_exports(scope_ids))

    pd.DataFrame(all_rows).sort_values(["annotator", "document_id"]).to_csv(
        output_path, index=False
    )


if __name__ == "__main__":
    typer.run(main)
