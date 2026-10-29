"""Higher-level operations over the generated endpoints, shared by the pipeline scripts."""  # noqa: E501

import json
from pathlib import Path
from typing import Any

from what_works_repo.nacsos_api import NacsosApiError, call, get_client
from what_works_repo.nacsos_api.generated.api.annotations.get_num_assignments_for_scope_api_annotations_annotate_scope_counts_assignment_scope_id_get import (  # noqa: E501
    sync as get_num_assignments_for_scope,
)
from what_works_repo.nacsos_api.generated.api.export.export_annotations_api_export_annotations_export_format_post import (  # noqa: E501
    sync as export_annotations,
)
from what_works_repo.nacsos_api.generated.api.export.get_export_label_options_api_export_project_label_options_scheme_id_get import (  # noqa: E501
    sync as get_export_label_options,
)
from what_works_repo.nacsos_api.generated.models import (
    AssignmentCounts,
    ExportRequest,
    ExportTypeEnum,
    LabelOptions,
)
from what_works_repo.settings import settings


def upload_file(local_path: Path, folder: str) -> str:
    """Multipart-POST a file to the core server's data dir; returns its server path.

    The generated client stringifies binary multipart parts, so this goes through
    the wrapper's httpx client directly (token signing and refresh still apply).
    """
    client = get_client().get_httpx_client()
    with local_path.open("rb") as fh:
        response = client.post(
            "/api/pipes/artefacts/files/upload",
            params={"folder": folder},
            files={"file": (local_path.name, fh, "application/json")},
            headers={"x-project-id": settings.nacsos.project_id},
        )
    if response.status_code != 200:
        raise NacsosApiError(
            f"upload of {local_path} failed ({response.status_code}): "
            f"{response.text[:300]}"
        )
    return response.json()


def ensure_scope_complete(assignment_scope_id: str, label: str) -> None:
    counts: AssignmentCounts = call(
        get_num_assignments_for_scope, assignment_scope_id=assignment_scope_id
    )
    if counts.num_open > 0 or counts.num_partial > 0:
        raise ValueError(
            f"{label} has incomplete assignments: "
            f"{counts.num_open} open, {counts.num_partial} partial"
        )


def project_labels(scheme_id: str) -> list[LabelOptions]:
    """Label options for a scheme, as accepted by the export endpoint."""
    raw = call(get_export_label_options, scheme_id=scheme_id)
    return [
        value if isinstance(value, LabelOptions) else LabelOptions(**value)
        for value in raw.additional_properties.values()
    ]


def export_annotations_jsonl(**body_kwargs: Any) -> list[dict]:
    """POST the annotation export as JSONL and return the parsed rows.

    Rows carry the item fields plus one `<key>|<value>` column per label option
    (1/0/None), `item_id`, and `username` (`RESOLVED` for resolved bot rows).
    """
    body = ExportRequest(
        labels=project_labels(settings.nacsos.scheme_id),
        ignore_hierarchy=True,
        ignore_repeat=True,
        **body_kwargs,
    )
    content = call(
        export_annotations,
        export_format=ExportTypeEnum.JSONL,
        body=body,
        max_results=1_000_000,
    )
    return [json.loads(line) for line in content.decode().splitlines() if line]
