from pathlib import Path

import pandas as pd
import typer

from what_works_repo.constants import DEET_SCOPE_SENTINEL
from what_works_repo.logging import logger
from what_works_repo.nacsos_api.generated.models import AssignmentFilter
from what_works_repo.nacsos_api.ops import (
    ensure_scope_complete,
    export_annotations_jsonl,
)
from what_works_repo.settings import settings


def export(resolution_scope_id: str, output_path: Path):
    ensure_scope_complete(resolution_scope_id, "Resolution scope")

    # TODO: Deal with resolutions if desired.
    # This just assumes single annotators are source of truth

    rows = export_annotations_jsonl(
        nql_filter=AssignmentFilter(mode=2, scopes=[resolution_scope_id]),
        assignment_scope_ids=[resolution_scope_id],
    )
    df = pd.DataFrame(rows)

    df[["scopus_id", "title", "text", f"{settings.nacsos.inclusion_key}|1"]].rename(
        columns={
            "scopus_id": "document_id",
            "title": "name",
            "text": "abstract",
            f"{settings.nacsos.inclusion_key}|1": "incl",
        }
    ).to_csv(output_path, index=False)


def main(deet_resolutions_scope: Path, output_path: Path):
    """
    Retrieve and human resolutions of deet annotations.

    Write results to a csv.
    """
    resolution_scope_id = deet_resolutions_scope.read_text().strip()
    if resolution_scope_id == DEET_SCOPE_SENTINEL:
        logger.info("No documents to resolve")
        output_path.write_text("document_id,name,abstract,incl\n")
        return

    logger.info("Exporting human resolutions of deet annotations.")

    export(
        resolution_scope_id=resolution_scope_id,
        output_path=output_path,
    )


if __name__ == "__main__":
    typer.run(main)
