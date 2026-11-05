"""Build a Zotero RIS file of included items from the local batch data.

The inclusion set is exactly `collect_annotations` filtered to includes: human
verdicts, human resolutions of DEET, and yolo'd (unreviewed) DEET verdicts.
Metadata comes from the batches' items.jsonl; the scopus_id -> NACSOS item_id
table is cached on disk and refreshed from nacsos-core on demand.
"""

import csv
import json
import re
from pathlib import Path

from what_works_repo.batch import Batch, collect_annotations
from what_works_repo.constants import DEET_SCOPE_SENTINEL

ITEM_ID_MAP = Path("data/processed/nacsos_item_ids.csv")
_SCOPUS_ID = re.compile(r"^2-s2\.0-\d+$")


def included_ids() -> set[str]:
    """Included scopus ids per collect_annotations, validated as Scopus ids."""
    df = collect_annotations()
    ids = {str(sid) for sid in df[df["incl"] == 1]["document_id"]}
    bad = [sid for sid in ids if not _SCOPUS_ID.fullmatch(sid)]
    if bad:
        raise ValueError(
            f"{len(bad)} included document_ids are not Scopus ids, e.g. {bad[:3]}"
        )
    return ids


def _metadata_index(scopus_ids: set[str]) -> dict[str, dict]:
    """Parse items.jsonl once, keeping the record for each requested scopus id."""
    meta: dict[str, dict] = {}
    for batch in Batch.existing():
        if not batch.items.is_file():
            continue
        with batch.items.open() as f:
            for line in f:
                if not line.strip():
                    continue
                record = json.loads(line)
                sid = record.get("scopus_id")
                if sid in scopus_ids and sid not in meta:
                    meta[sid] = record
    return meta


def _annotation_scope_ids() -> list[str]:
    """All human annotation and DEET-resolution scope ids recorded by the pipeline."""
    scope_ids: list[str] = []
    for batch in Batch.existing():
        if batch.scope_ids.is_file():
            scope_ids.extend(json.loads(batch.scope_ids.read_text()))
        if batch.deet_resolution_scope.is_file():
            scope = batch.deet_resolution_scope.read_text().strip()
            if scope and scope != DEET_SCOPE_SENTINEL:
                scope_ids.append(scope)
    return sorted(set(scope_ids))


def refresh_item_id_map(force: bool = False) -> dict[str, str]:
    """scopus_id -> NACSOS item_id from the cached table.

    Refetched from nacsos-core when the cache is absent or `force` is set.
    """
    if ITEM_ID_MAP.is_file() and not force:
        with ITEM_ID_MAP.open(newline="") as f:
            return {row["scopus_id"]: row["item_id"] for row in csv.DictReader(f)}
    from what_works_repo.nacsos_api.ops import export_annotations_jsonl

    scopes = _annotation_scope_ids()
    if not scopes:
        raise FileNotFoundError("no annotation scopes recorded; cannot map item ids")
    rows = export_annotations_jsonl(assignment_scope_ids=scopes)
    mapping = {
        str(row["scopus_id"]): str(row["item_id"])
        for row in rows
        if row.get("scopus_id") and row.get("item_id")
    }
    ITEM_ID_MAP.parent.mkdir(parents=True, exist_ok=True)
    with ITEM_ID_MAP.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["scopus_id", "item_id"])
        writer.writerows(sorted(mapping.items()))
    return mapping


def _fetch_missing_meta(
    scopus_ids: set[str], id_map: dict[str, str]
) -> dict[str, dict]:
    """Pull metadata from nacsos-core for items that predate the batch layout."""
    from what_works_repo.nacsos_api import call
    from what_works_repo.nacsos_api.generated.api.item.get_item_info_api_item_info_item_id_get import (  # noqa: E501
        sync as get_item_info,
    )

    meta: dict[str, dict] = {}
    for sid in sorted(scopus_ids):
        item_id = id_map.get(sid)
        if not item_id:
            raise ValueError(f"included id {sid} has no batch metadata and no mapping")
        meta[sid] = call(get_item_info, item_id=item_id).to_dict()
    return meta


def _tag(tag: str, value: object) -> str:
    return f"{tag}  - {str(value).replace(chr(10), ' ').replace(chr(13), ' ')}"


def _record(meta: dict, nacsos_id: str | None) -> list[str]:
    """One RIS journal-article record; Extra carries the NACSOS and Scopus ids."""
    lines = ["TY  - JOUR"]
    for author in meta.get("authors") or []:
        name = author.get("name") if isinstance(author, dict) else str(author)
        if not name:
            continue
        given, _, last = name.rpartition(" ")
        lines.append(_tag("AU", f"{last}, {given}" if given else name))
    if meta.get("publication_year"):
        lines.append(_tag("PY", meta["publication_year"]))
    if meta.get("title"):
        lines.append(_tag("TI", meta["title"]))
    if meta.get("source"):
        lines.append(_tag("JO", meta["source"]))
    if meta.get("doi"):
        lines.append(_tag("DO", f"https://doi.org/{meta['doi']}"))
    for keyword in meta.get("keywords") or []:
        lines.append(_tag("KW", keyword))
    if meta.get("text"):
        lines.append(_tag("AB", meta["text"]))
    if nacsos_id:
        lines.append(_tag("M2", f"NACSOS ID: {nacsos_id}"))
    lines.append(_tag("M2", f"Scopus ID: {meta['scopus_id']}"))
    lines.append("ER  - ")
    return lines


def run(output: Path, refresh: bool = False) -> tuple[int, int]:
    """Write the included-items RIS file to `output`.

    Returns (records, records_with_nacsos_id).
    """
    included = included_ids()
    id_map = refresh_item_id_map(force=refresh)
    meta = _metadata_index(included)
    meta.update(_fetch_missing_meta(included - meta.keys(), id_map))
    records = [_record(meta[sid], id_map.get(sid)) for sid in sorted(included)]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join("\n".join(r) for r in records) + "\n", encoding="utf-8")
    return len(records), sum(sid in id_map for sid in included)
