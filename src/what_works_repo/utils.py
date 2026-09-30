"""Utility functions for dealing with data"""

import json
from pathlib import Path

from what_works_repo.constants import RAW_DATA

CACHE = Path(".cache/document_count.json")


def count_documents(data_dir: Path = Path(RAW_DATA)) -> int:
    "Count total records across all raw jsonl files."
    files = sorted(data_dir.rglob("*.jsonl"))
    fingerprint = {
        "n_files": len(files),
        "total_bytes": sum(f.stat().st_size for f in files),
    }

    if CACHE.exists():
        cached = json.loads(CACHE.read_text())
        if all(cached.get(k) == v for k, v in fingerprint.items()):
            return cached["count"]

    count = sum(sum(1 for _ in f.open(encoding="utf-8")) for f in files)
    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_text(json.dumps({"count": count, **fingerprint}, indent=2) + "\n")
    return count
