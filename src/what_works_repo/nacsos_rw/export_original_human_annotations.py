"""Export original (pre-resolution) human annotations, if complete."""

from pathlib import Path

import pandas as pd
import typer

from what_works_repo.nacsos_api.ops import (
    ensure_scope_complete,
    export_annotations_jsonl,
)
from what_works_repo.nacsos_rw.export_human_annotations import read_scopes
from what_works_repo.settings import settings


def export_annotations(scope_id: str) -> list[dict]:
    ensure_scope_complete(scope_id, "Scope")

    incl_column = f"{settings.nacsos.inclusion_key}|1"
    rows = [
        {
            "document_id": str(row["scopus_id"]),
            "name": row["title"],
            "abstract": row["text"],
            "annotator": row["username"],
            settings.nacsos.inclusion_key: row[incl_column],
        }
        for row in export_annotations_jsonl(assignment_scope_ids=[scope_id])
        if row["username"] not in (None, "RESOLVED") and row[incl_column] is not None
    ]
    return rows


def main(scope_path: Path, output_path: Path):
    """
    Retrieve the original annotations of each human annotator in a scope.

    Write results to a csv.
    """
    scope_ids = read_scopes(scope_path)
    all_rows = [row for scope_id in scope_ids for row in export_annotations(scope_id)]

    pd.DataFrame(all_rows).sort_values(["annotator", "document_id"]).to_csv(
        output_path, index=False
    )


if __name__ == "__main__":
    typer.run(main)
