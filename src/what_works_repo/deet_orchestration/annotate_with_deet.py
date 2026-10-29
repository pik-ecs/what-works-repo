import datetime
import uuid
from pathlib import Path

import pandas as pd
import typer
from deet.data_models.project import DeetProject, ExperimentArtefacts

from what_works_repo.batch import Batch
from what_works_repo.configurations import (
    DeetAnnotationConfig,
)
from what_works_repo.constants import DEET_RUN_SKIP, DEET_SCOPE_SENTINEL
from what_works_repo.deet_orchestration.deet_annotator import DeetAnnotator
from what_works_repo.logging import logger
from what_works_repo.nacsos_api import call
from what_works_repo.nacsos_api.generated.api.annotations.bulk_add_assignment_api_annotations_config_scopes_bulk_add_put import (  # noqa: E501
    sync as bulk_add_assignment,
)
from what_works_repo.nacsos_api.generated.api.annotations.get_items_with_count_api_annotations_config_items_get import (  # noqa: E501
    sync as get_items_with_count,
)
from what_works_repo.nacsos_api.generated.api.annotations.put_assignment_scope_api_annotations_assignments_scope_put import (  # noqa: E501
    sync as put_assignment_scope,
)
from what_works_repo.nacsos_api.generated.api.item.get_item_info_api_item_info_item_id_get import (  # noqa: E501
    sync as get_item_info,
)
from what_works_repo.nacsos_api.generated.models import (
    AssignmentScopeModel,
    BulkAddPayload,
)
from what_works_repo.settings import settings


def resolve_deet_experiment(
    run_id: str, deet_project_config: Path
) -> ExperimentArtefacts:
    """Resolve a deet project and run id (stored in a text file) to an experiment."""
    project = DeetProject.load(project_dir=deet_project_config.parent)
    experiment = ExperimentArtefacts(base_dir=project.experiments_dir / run_id)
    if not experiment.is_complete:
        raise ValueError
    return experiment


def annotate(annotator: DeetAnnotator, annotation_df: pd.DataFrame) -> pd.DataFrame:
    """
    Annotate documents in dataframe
    """
    incl_values = []
    reasoning_values = []

    for _, row in annotation_df.iterrows():
        text = (row["name"] or "") + " " + (row["abstract"] or "")
        deet_annotations = annotator.predict(text)

        deet_value, reasoning = next(
            (ann.output_data, ann.reasoning)
            for ann in deet_annotations
            if ann.attribute.attribute_label == settings.nacsos.inclusion_key
        )

        incl_values.append(bool(deet_value))
        reasoning_values.append(reasoning or "")

    annotation_df["incl"] = incl_values
    annotation_df["reasoning"] = reasoning_values

    return annotation_df


def assign_deet_verification_scope(
    predicted_positive_ids: list[str], scheme_id: str, scope_name: str
) -> str:
    """
    Assign predicted positives to users defined in config.

    If either the list of users is empty, or there are no predicted positives,
    return a sentinel.

    Else, create a new assignment scope, and create assignments splitting
    predicted positives across users.
    """
    if not predicted_positive_ids or not settings.nacsos.deet_check_users:
        return DEET_SCOPE_SENTINEL

    new_scope_id = str(uuid.uuid4())
    call(
        put_assignment_scope,
        body=AssignmentScopeModel(
            assignment_scope_id=new_scope_id,
            annotation_scheme_id=scheme_id,
            name=f"{scope_name}__human_resolution",
            description="Human review of deet-predicted positives",
        ),
    )
    for user_id in settings.nacsos.deet_check_users:
        call(
            bulk_add_assignment,
            body=BulkAddPayload(
                user_id=user_id,
                scope_id=new_scope_id,
                scheme_id=scheme_id,
                item_ids=predicted_positive_ids,
            ),
        )
    return new_scope_id


def get_items_to_annotate(
    annotation_config: DeetAnnotationConfig,
) -> pd.DataFrame:
    """From all unassigned documents, return a dataframe of documents.

    dataframe should have columns
     - document_id (scopus id),
     - name (title)
     - abstract (abstract)
    """
    unassigned = [
        str(item.item_id) for item in call(get_items_with_count) if item.num_total == 0
    ][: annotation_config.n_annotations]

    return pd.DataFrame(
        [
            {
                "document_id": str(item.scopus_id),
                "name": item.title,
                "abstract": item.text,
                "item_id": str(item.item_id),
            }
            for item in (call(get_item_info, item_id=item_id) for item_id in unassigned)
        ]
    )


def get_items_to_resolve(
    annotated_df: pd.DataFrame, annotation_config: DeetAnnotationConfig
) -> list[str]:
    """
    Given an annotated df, return the list of documents to resolve.

    Resolution configuration is set in `annotation_config`.
    """
    items_to_resolve = []
    if annotation_config.check_negatives:
        items_to_resolve.extend(annotated_df[~annotated_df["incl"]]["item_id"].tolist())
    if annotation_config.check_positives:
        items_to_resolve.extend(annotated_df[annotated_df["incl"]]["item_id"].tolist())
    return items_to_resolve


def _main(
    annotator: DeetAnnotator, annotation_config: DeetAnnotationConfig, batch: Batch
) -> None:
    to_annotate = get_items_to_annotate(annotation_config)
    logger.info(f"{len(to_annotate)} items to annotate.")
    annotated_df = annotate(annotator, to_annotate)
    annotated_df.to_csv(batch.deet_annotations, index=False)
    items_to_resolve = get_items_to_resolve(annotated_df, annotation_config)

    today = datetime.date.today()
    scope_name = f"{today.strftime('%Y_%m_%d')}_deet_batch_{batch.number}"

    new_scope_id = assign_deet_verification_scope(
        items_to_resolve, settings.nacsos.scheme_id, scope_name
    )
    batch.deet_resolution_scope.write_text(new_scope_id)


def main(
    batch_number: int,
):
    """
    Annotate documents with deet.

    Take documents from items. Annotate with deet, using the configuration
    read from the overall deet project config, and the annotation config.

    Create a new scope with assignments to human users,
        as specified in annotation config.

    TODO: Should this come from items instead? In this way we can preserve the order.
    Actually, order in NACSOS doesn't matter, we can reconstruct the order
    on stopping criteria calculation.
    """
    batch = Batch(batch_number)
    annotation_config = DeetAnnotationConfig.model_validate_json(
        batch.deet_annotation_config.read_text()
    )
    if (
        annotation_config.deet_run == DEET_RUN_SKIP
        or annotation_config.n_annotations < 1
    ):
        batch.deet_annotations.write_text("document_id,name,abstract,incl\n")
        batch.deet_resolution_scope.write_text(DEET_SCOPE_SENTINEL)
        return

    experiment = resolve_deet_experiment(annotation_config.deet_run, batch.deet_config)
    annotator = DeetAnnotator(experiment=experiment)
    _main(annotator=annotator, annotation_config=annotation_config, batch=batch)


if __name__ == "__main__":
    typer.run(main)
