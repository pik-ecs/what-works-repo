#!/bin/bash

# Aggregate tuning_*.json written by the tune jobs, refit the pooled-AUC winner, and
# write model/, model.txt, report.json and the OOF table. Submit with
# --dependency=afterok:<cpu_job>:<gpu_job> so it runs only when both tunings succeeded.
# Runs on the gpu partition because the winner may be a BERT, whose refit needs a GPU.

#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --mem=32G
#SBATCH --mail-user="maxca"
#SBATCH --output=data/logs/select_%j.out
#SBATCH --error=data/logs/select_%j.err
#SBATCH --chdir=/home/maxca/what-works-repo
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --qos=gpushort
#SBATCH --cpus-per-task=8
#SBATCH --mail-type=END,FAIL

set -e
set -o xtrace

module load cuda

unset VIRTUAL_ENV
export PYTHONUNBUFFERED=1
export OPENBLAS_NUM_THREADS=1
export TRANSFORMERS_OFFLINE=1
export HF_HUB_OFFLINE=1
export UV_OFFLINE=1
export HF_HOME=/data/rd5/ecs/huggingface-cache
export UV_PROJECT_ENVIRONMENT=/home/maxca/software/WWCS/what-works-repo/.venv

BATCH_N="${BATCH_N:-9}"

.venv/bin/python src/what_works_repo/classify/train.py "$BATCH_N" --select
