"""Utility functions for dealing with data"""

import json
from pathlib import Path

from what_works_repo.constants import RAW_DATA

CACHE = Path(".cache/document_count.json")


def count_documents(data_dir: Path = Path(RAW_DATA)) -> int:
    """Count distinct documents (by eid) across all raw jsonl files.

    Raw exports overlap, so record counts inflate the screening universe;
    the eid dedup matches sample_scopus_records.py.
    """
    files = sorted(data_dir.rglob("*.jsonl"))
    fingerprint = {
        "n_files": len(files),
        "total_bytes": sum(f.stat().st_size for f in files),
    }

    if CACHE.exists():
        cached = json.loads(CACHE.read_text())
        if all(cached.get(k) == v for k, v in fingerprint.items()):
            return cached["count"]

    eids: set[str | None] = set()
    for f in files:
        for line in f.open(encoding="utf-8"):
            eids.add(json.loads(line).get("eid"))
    count = len(eids)
    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_text(json.dumps({"count": count, **fingerprint}, indent=2) + "\n")
    return count
