#!/usr/bin/env bash
# Submit one prediction round: the 8-way scoring array, then a single finisher
# job chained via Slurm dependencies. The array's tasks each re-run the
# filter/items write over partial results (predict.py always does); the
# finisher skips every scored partition via its _SUCCESS sentinel and is the
# last writer of batch_N+1/items.jsonl. Run on a login node.
#
#   BATCH_N=9 ./scripts/submit_predict.sh
#
# Before running, the batch needs next_batch_config.json from the interactive
# wizard (it cannot run inside a job):
#   .venv/bin/python src/what_works_repo/classify/configure_next_batch.py $BATCH_N
# After any retrain, wipe last round's scores or the sentinels skip them:
#   rm -rf data/predictions/prioritisation/

set -euo pipefail
cd "$(dirname "$0")/.."

if [[ -z "${BATCH_N:-}" ]]; then
  echo "set BATCH_N explicitly, e.g. BATCH_N=9 $0" >&2
  exit 1
fi

if [[ ! -f "data/processed/batches/batch_${BATCH_N}/next_batch_config.json" ]]; then
  echo "batch_${BATCH_N}/next_batch_config.json missing; run the wizard first:" >&2
  echo "  .venv/bin/python src/what_works_repo/classify/configure_next_batch.py ${BATCH_N}" >&2
  exit 1
fi

J_ARRAY=$(sbatch --parsable --export=ALL,BATCH_N="$BATCH_N" scripts/predict.slurm)
J_ARRAY_SPEC=${J_ARRAY%%:*}  # <id>_[0-7]; the form Slurm dependencies take for a whole array
J_ARRAY_ID=${J_ARRAY##*:}
J_FINAL=$(sbatch --parsable --array=0-0 \
          --dependency="afterok:${J_ARRAY_SPEC}" \
          --export=ALL,BATCH_N="$BATCH_N" scripts/predict.slurm)

echo "scoring array: $J_ARRAY_ID (8 gpu tasks)"
echo "finisher job:  $J_FINAL (runs when all 8 exit 0; writes batch_$((BATCH_N + 1))/items.jsonl)"
squeue -j "$J_ARRAY_ID,$J_FINAL"
