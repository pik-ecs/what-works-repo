"""Export human annotations, if complete."""

import json
import uuid
from pathlib import Path

import pandas as pd
import typer

from what_works_repo.nacsos_api import call
from what_works_repo.nacsos_api.generated.api.annotations.get_assignments_for_scope_api_annotations_annotate_assignments_scope_assignment_scope_id_get import (  # noqa: E501
    sync as get_assignments_for_scope,
)
from what_works_repo.nacsos_api.generated.api.annotations.get_bot_scopes_api_annotations_bot_scopes_get import (  # noqa: E501
    sync as get_bot_scopes,
)
from what_works_repo.nacsos_api.ops import export_annotations_jsonl
from what_works_repo.settings import settings


def read_scopes(scope_path: Path) -> list[str]:
    scope_ids = []
    for item in json.loads(scope_path.read_text()):
        try:
            uuid.UUID(item)
        except ValueError as e:
            raise e
        scope_ids.append(item)
    if not scope_ids:
        raise ValueError("The list of scope IDs is empty")
    return scope_ids


def export_assignments(assignment_scope_id: str) -> list[dict]:
    assignments = call(
        get_assignments_for_scope, assignment_scope_id=assignment_scope_id
    )

    # The resolution created in the NACSOS UI is the bot metadata for this scope.
    metas = [
        meta
        for meta in call(get_bot_scopes)
        if str(meta.assignment_scope_id) == assignment_scope_id
    ]
    if len(metas) != 1:
        raise ValueError(
            f"Expected exactly one resolution for scope, found {len(metas)}."
        )

    rows = [
        row
        for row in export_annotations_jsonl(
            bot_annotation_metadata_ids=[str(metas[0].bot_annotation_metadata_id)]
        )
        if row["username"] == "RESOLVED"
    ]
    resolved_item_ids = {str(row["item_id"]) for row in rows}

    for assignment in assignments:
        if str(assignment.item_id) not in resolved_item_ids:
            raise ValueError(f"Assignment {assignment.item_id} not resolved")

    incl_column = f"{settings.nacsos.inclusion_key}|1"
    return [
        {
            "document_id": str(row["scopus_id"]),
            "name": row["title"],
            "abstract": row["text"],
            settings.nacsos.inclusion_key: row[incl_column],
        }
        for row in rows
        if row[incl_column] is not None
    ]


def main(scope_path: Path, output_path: Path):

    scope_ids = read_scopes(scope_path)
    all_rows = [row for scope_id in scope_ids for row in export_assignments(scope_id)]

    pd.DataFrame(all_rows).to_csv(output_path, index=False)


if __name__ == "__main__":
    typer.run(main)
