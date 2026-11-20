#!/bin/bash

# Tune the linear prioritisation candidates (single CPU task, both models).

#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --mem=16G
#SBATCH --mail-user="maxca"
#SBATCH --output=data/logs/train_cpu_%j.out
#SBATCH --error=data/logs/train_cpu_%j.err
#SBATCH --chdir=/home/maxca/what-works-repo
#SBATCH --partition=compute
#SBATCH --qos=short
#SBATCH --cpus-per-task=8
#SBATCH --mail-type=END,FAIL

set -e
set -o xtrace

unset VIRTUAL_ENV
export PYTHONUNBUFFERED=1
export OPENBLAS_NUM_THREADS=1
export TRANSFORMERS_OFFLINE=1
export HF_HUB_OFFLINE=1
export UV_OFFLINE=1
export HF_HOME=/data/rd5/ecs/huggingface-cache
export UV_PROJECT_ENVIRONMENT=/home/maxca/software/WWCS/what-works-repo/.venv

BATCH_N="${BATCH_N:-9}"

.venv/bin/python src/what_works_repo/classify/train.py "$BATCH_N" --models logreg,nb
