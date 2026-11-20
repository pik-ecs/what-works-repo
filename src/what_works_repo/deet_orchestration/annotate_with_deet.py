import datetime
import json
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
from what_works_repo.nacsos_api.generated.api.annotations.put_assignment_scope_api_annotations_assignments_scope_put import (  # noqa: E501
    sync as put_assignment_scope,
)
from what_works_repo.nacsos_api.generated.api.project.list_project_data_paged_api_project_items_item_type_list_page_page_size_get import (  # noqa: E501
    sync as list_project_data_paged,
)
from what_works_repo.nacsos_api.generated.models import (
    AssignmentScopeModel,
    BulkAddPayload,
    ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType,
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


ANNOTATION_CHUNK_SIZE = 500


def annotate(
    annotator: DeetAnnotator, annotation_df: pd.DataFrame, output_path: Path
) -> list[str]:
    """
    Annotate documents in dataframe, appending results to output_path.

    DEET runs in chunks so an interruption loses at most one chunk of work.
    Returns the document_ids DEET failed to extract (rate limits, content
    policy); they are absent from output_path and retried on a rerun.
    """
    header = ",".join([*annotation_df.columns, "incl", "reasoning"])
    if not output_path.exists() or output_path.open().readline().strip() != header:
        output_path.write_text(header + "\n")

    missing: list[str] = []
    for start in range(0, len(annotation_df), ANNOTATION_CHUNK_SIZE):
        chunk = annotation_df.iloc[start : start + ANNOTATION_CHUNK_SIZE]
        texts = {
            str(row["document_id"]): " ".join(
                str(value)
                for value in (row["name"], row["abstract"])
                if pd.notna(value) and value
            )
            for _, row in chunk.iterrows()
        }
        run = annotator.predict_batch(texts)
        annotations = {
            str(doc.document.document_identity.external_id): doc.annotations
            for doc in run.annotated_documents
        }
        records = []
        for _, row in chunk.iterrows():
            doc_annotations = annotations.get(str(row["document_id"]))
            if doc_annotations is None:
                missing.append(str(row["document_id"]))
                continue
            deet_value, reasoning = next(
                (ann.output_data, ann.reasoning)
                for ann in doc_annotations
                if ann.attribute.attribute_label == settings.nacsos.inclusion_key
            )
            records.append(
                {**row, "incl": bool(deet_value), "reasoning": reasoning or ""}
            )
        pd.DataFrame(records).to_csv(output_path, mode="a", header=False, index=False)
        logger.info(f"Annotated {len(records)} of {len(chunk)} documents.")
    return missing


def _annotated_ids(path: Path) -> set[str]:
    """document_ids already written by a previous, interrupted DEET run."""
    if not path.exists():
        return set()
    df = pd.read_csv(path)
    if "document_id" not in df.columns:
        return set()
    return set(df["document_id"].astype(str))


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


PAGE_SIZE = 1000


def _read_batch_items(batch: Batch) -> pd.DataFrame:
    """Unique scopus documents of the batch, in prediction order, from items.jsonl."""
    records: list[dict] = []
    seen: set[str] = set()
    for line in batch.items.open():
        if not line.strip():
            continue
        data = json.loads(line)
        scopus_id = str(data["scopus_id"])
        if scopus_id in seen:
            continue
        seen.add(scopus_id)
        records.append(
            {
                "document_id": scopus_id,
                "name": data.get("title"),
                "abstract": data.get("text"),
            }
        )
    return pd.DataFrame(records, columns=["document_id", "name", "abstract"])


def _scopus_item_ids(batch: Batch) -> dict[str, str]:
    """Map scopus_id to server item_id, cached under the batch dir.

    Client-written item_ids in items.jsonl are not the server's; server ids
    are only discoverable by paging through the project's items.
    """
    cache = batch.dir / "scopus_item_ids.csv"
    if cache.exists():
        df = pd.read_csv(cache)
        return dict(zip(df["scopus_id"], df["item_id"], strict=True))
    pairs: list[tuple[str, str]] = []
    page = 1
    while items := call(
        list_project_data_paged,
        item_type=ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType.ACADEMIC,
        page=page,
        page_size=PAGE_SIZE,
    ):
        pairs.extend((str(item.scopus_id), str(item.item_id)) for item in items)
        page += 1
    pd.DataFrame(pairs, columns=["scopus_id", "item_id"]).to_csv(cache, index=False)
    return dict(pairs)


def get_items_to_annotate(
    annotation_config: DeetAnnotationConfig,
    batch: Batch,
) -> pd.DataFrame:
    """Return the batch's documents as a dataframe.

    The worklist is the batch's own items; NACSOS's item-count view excludes
    never-assigned items, so it cannot serve as a source of new documents.
    Server item_ids are only needed to assign human resolution scopes, so
    the lookup runs only when the check flags ask for one.

    dataframe columns: document_id (scopus id), name, abstract, item_id
    """
    to_annotate = _read_batch_items(batch).head(annotation_config.n_annotations)
    if annotation_config.check_positives or annotation_config.check_negatives:
        to_annotate["item_id"] = to_annotate["document_id"].map(_scopus_item_ids(batch))
        missing = to_annotate["document_id"][to_annotate["item_id"].isna()]
        if not missing.empty:
            # items the server deduped onto existing rows (whose scopus_id is
            # not denormalized) stay unresolvable; their DEET verdicts still
            # count, but humans cannot be assigned to review them
            logger.warning(
                f"{len(missing)} items have no NACSOS item_id and will skip "
                f"human resolution, e.g. {missing.head(5).tolist()}"
            )
        to_annotate["item_id"] = to_annotate["item_id"].fillna("").astype(str)
    else:
        to_annotate["item_id"] = ""
    return to_annotate


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
    # items without a server item_id cannot be assigned (see get_items_to_annotate)
    return [str(i) for i in items_to_resolve if isinstance(i, str) and i]


def _promote_partial(batch: Batch) -> None:
    """Merge the partial file into the final one once the run is complete.

    The final file's existence then always means a complete annotation pass;
    snakemake rules that declare it as output can trust it.
    """
    frames = [
        pd.read_csv(p)
        for p in (batch.deet_annotations, batch.deet_annotations_partial)
        if p.exists()
    ]
    if frames:
        pd.concat(frames, ignore_index=True).drop_duplicates("document_id").to_csv(
            batch.deet_annotations, index=False
        )
    batch.deet_annotations_partial.unlink(missing_ok=True)


def _main(
    annotator: DeetAnnotator, annotation_config: DeetAnnotationConfig, batch: Batch
) -> None:
    to_annotate = get_items_to_annotate(annotation_config, batch)
    done = _annotated_ids(batch.deet_annotations_partial) | _annotated_ids(
        batch.deet_annotations
    )
    to_annotate = to_annotate[~to_annotate["document_id"].astype(str).isin(done)]
    logger.info(f"{len(to_annotate)} items to annotate ({len(done)} already done).")
    missing = annotate(annotator, to_annotate, batch.deet_annotations_partial)
    if missing:
        raise ValueError(
            f"DEET failed to extract {len(missing)} documents, e.g. {missing[:5]}. "
            "Re-run to retry only the missing ones."
        )
    _promote_partial(batch)
    annotated_df = pd.read_csv(batch.deet_annotations)
    items_to_resolve = get_items_to_resolve(annotated_df, annotation_config)

    today = datetime.date.today()
    scope_name = f"{today.strftime('%Y_%m_%d')}_deet_batch_{batch.number}"

    new_scope_id = assign_deet_verification_scope(
        items_to_resolve, settings.nacsos.scheme_id, scope_name
    )
    batch.deet_resolution_scope.write_text(new_scope_id)


def main(
    batch_number: int,
    max_workers: int = typer.Option(
        8, help="Concurrent per-document LLM calls; raise within your Azure quota."
    ),
):
    """
    Annotate documents with deet.

    Take documents from the batch's items.jsonl, in prediction order.
    Annotate with deet, using the configuration read from the overall deet
    project config, and the annotation config.

    Create a new scope with assignments to human users,
        as specified in annotation config.
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
    annotator = DeetAnnotator(experiment=experiment, max_workers=max_workers)
    _main(annotator=annotator, annotation_config=annotation_config, batch=batch)


if __name__ == "__main__":
    typer.run(main)
