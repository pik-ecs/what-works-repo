#!/usr/bin/env bash
# Submit one prioritisation-training round: CPU tuning, GPU tuning, then the
# winner-picker gated on both via Slurm job dependencies. Run on a login node.
#
#   ./scripts/submit_training.sh              # tunes the current batch (9)
#   BATCH_N=10 ./scripts/submit_training.sh
#
# Before running: git pull so the cluster checkout has the current train.py, and
# remove stale outputs of interrupted runs (their tuning_*.json lack the label
# fingerprint select() needs):
#   rm -f data/processed/batches/batch_${BATCH_N:-9}/prioritisation/tuning_*.json

set -euo pipefail
cd "$(dirname "$0")/.."

BATCH_N="${BATCH_N:-9}"

J_CPU=$(sbatch --parsable --partition=priority --qos=priority \
        --export=ALL,BATCH_N="$BATCH_N" scripts/train_cpu.slurm)
J_GPU=$(sbatch --parsable \
        --export=ALL,BATCH_N="$BATCH_N" scripts/train_gpu.slurm)
J_PICK=$(sbatch --parsable --dependency="afterok:${J_CPU}:${J_GPU}" \
        --export=ALL,BATCH_N="$BATCH_N" scripts/select_model.slurm)

echo "cpu tune job:  $J_CPU (priority partition)"
echo "gpu tune jobs: $J_GPU (array: modernbert, climate-modernbert)"
echo "picker job:    $J_PICK (starts when both tunings exit 0; mails on END/FAIL)"
squeue -j "$J_CPU,$J_GPU,$J_PICK"
