#!/bin/bash

# Fine-tune the BERT-family prioritisation candidates on GPU (one array task per model).
# Set BATCH_N to the batch whose labels to train on and whose dirs receive the output.

#SBATCH --time=08:00:00
#SBATCH --nodes=1
#SBATCH --mem=32G
#SBATCH --mail-user="maxca"
#SBATCH --output=data/logs/train_%a_%j.out
#SBATCH --error=data/logs/train_%a_%j.err
#SBATCH --chdir=/home/maxca/what-works-repo
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu
#SBATCH --qos=gpumedium
#SBATCH --cpus-per-task=8
#SBATCH --mail-type=END,FAIL
#SBATCH --array=0-1

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
case "$SLURM_ARRAY_TASK_ID" in
  0) MODEL=modernbert ;;
  1) MODEL=climate-modernbert ;;
esac

.venv/bin/python src/what_works_repo/classify/train.py "$BATCH_N" --models "$MODEL"
