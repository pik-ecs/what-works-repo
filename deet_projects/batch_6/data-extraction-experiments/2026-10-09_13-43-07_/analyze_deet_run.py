import argparse
import csv
import json
from collections import Counter
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("run_dir", type=Path)
args = parser.parse_args()

comparison_path = args.run_dir / "goldstandard_llm_comparison.csv"
annotations_path = args.run_dir / "llm_annotations.json"

with comparison_path.open(encoding="utf-8-sig", newline="") as file:
    rows = list(csv.DictReader(file))

annotations = json.loads(annotations_path.read_text(encoding="utf-8-sig"))
abstracts = {
    str(item["document"]["document_id"]): item["document"].get("context", "")
    for item in annotations["annotated_documents"]
}

counts = Counter()
mismatches = []

for row in rows:
    gold = row["human_extraction"].strip().lower() == "true"
    prediction = row["llm_extraction"].strip().lower() == "true"
    counts[(gold, prediction)] += 1

    if gold != prediction:
        mismatches.append({
            "error_type": "false_positive" if prediction else "false_negative",
            "document_name": row["document_name"],
            "external_id": row["external_id"],
            "human_extraction": row["human_extraction"],
            "llm_extraction": row["llm_extraction"],
            "llm_reasoning": row["llm_reasoning"],
            "llm_verbatim_text": row["llm_verbatim_text"],
            "abstract": abstracts.get(row["external_id"], ""),
        })

output_path = args.run_dir / "error_analysis.csv"
fields = list(mismatches[0]) if mismatches else [
    "error_type", "document_name", "external_id", "human_extraction",
    "llm_extraction", "llm_reasoning", "llm_verbatim_text", "abstract"
]

with output_path.open("w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(mismatches)

print(f"Documents evaluated: {len(rows)}")
print(f"False positives: {counts[(False, True)]}")
print(f"False negatives: {counts[(True, False)]}")
print(f"Mismatch details: {output_path}")
 