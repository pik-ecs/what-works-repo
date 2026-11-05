"""Import a batch of AcademicItemModel JSONL into NACSOS through the core API.

Replaces the `nacsos import ACADEMIC` CLI, with the same duplicate checking and
revision bookkeeping (both run server-side). Steps: upload the JSONL to the core
server's data dir, point the project's Import config at it, trigger the dramatiq
import task, wait for the new revision's task to reach a terminal state.
"""

import time
from pathlib import Path

import typer

from what_works_repo.logging import logger
from what_works_repo.nacsos_api import call
from what_works_repo.nacsos_api.generated.api.imports.get_import_counts_api_imports_import_import_id_count_get import (  # noqa: E501
    sync as get_import_counts,
)
from what_works_repo.nacsos_api.generated.api.imports.get_import_details_api_imports_import_import_id_get import (  # noqa: E501
    sync as get_import_details,
)
from what_works_repo.nacsos_api.generated.api.imports.get_import_revisions_api_imports_import_import_id_revisions_get import (  # noqa: E501
    sync as get_import_revisions,
)
from what_works_repo.nacsos_api.generated.api.imports.put_import_details_api_imports_import_put import (  # noqa: E501
    sync as put_import_details,
)
from what_works_repo.nacsos_api.generated.api.imports.trigger_import_api_imports_import_import_id_post import (  # noqa: E501
    sync as trigger_import,
)
from what_works_repo.nacsos_api.generated.models import AcademicItemImport, TaskStatus
from what_works_repo.nacsos_api.ops import upload_file
from what_works_repo.settings import settings

POLL_SECONDS = 10
TIMEOUT_SECONDS = 4 * 60 * 60


def import_items(items: Path, batch_number: int) -> None:
    uploaded_path = upload_file(items, folder=f"what_works/batch_{batch_number}")
    logger.info(f"Uploaded {items} to nacsos-core as {uploaded_path}")

    import_details = call(get_import_details, import_id=settings.nacsos.import_id)
    import_details.config = AcademicItemImport(sources=[uploaded_path])
    call(put_import_details, body=import_details)

    baseline = len(call(get_import_revisions, import_id=settings.nacsos.import_id))
    call(trigger_import, import_id=settings.nacsos.import_id)

    deadline = time.monotonic() + TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        revisions = call(get_import_revisions, import_id=settings.nacsos.import_id)
        if len(revisions) > baseline and revisions[0].task is not None:
            status = revisions[0].task.status
            if status == TaskStatus.COMPLETED:
                count = call(get_import_counts, import_id=settings.nacsos.import_id)
                logger.info(f"Import complete; import now holds {count} items")
                return
            if status in (TaskStatus.FAILED, TaskStatus.CANCELLED):
                raise RuntimeError(f"nacsos import task {status}: {revisions[0].task}")
        time.sleep(POLL_SECONDS)
    raise TimeoutError(f"nacsos import task did not finish within {TIMEOUT_SECONDS}s")


def main(items: Path, batch_number: int):
    import_items(items=items, batch_number=batch_number)


if __name__ == "__main__":
    typer.run(main)
