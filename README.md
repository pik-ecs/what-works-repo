# what-works-repo

Active-learning screening pipeline: sample → import to NACSOS → human annotation
→ DEET auto-annotation → resolve → stopping criterion.
The stages, and the files they read and write, are described in `docs/workflow.md`.

## Quick start
```bash
uv sync
uv run dvc pull           # fetch the data; see Data (DVC) below for the one-time remote setup
uv run snakemake          # runs until a manual step is needed, then stops
```

## Data (DVC)
The contents of `data/` live in DVC, not git. Each top-level subdirectory has
its own pointer file in git, so the subdirectories can be pulled separately:

```bash
uv run dvc pull                       # everything, ~21 GB
uv run dvc pull data/processed.dvc    # the annotated batches only
```

The remote is SSH on ts01 (PIK network). The committed `.dvc/config` names one
Pik account as the SSH user; set your own (written to `.dvc/config.local`,
which is gitignored):

```bash
dvc remote modify ts01 user <pik-username> --local
```

After adding or replacing data files, run `uv run dvc add data/<subdir>`,
commit the changed `.dvc` pointer, and run `uv run dvc push`.

## Running the pipeline
The annotation team annotates batches in NACSOS, 
and this repo is used to process each batch according to the pipeline.

A cycle is two `uv run snakemake` runs with the human steps
below in between. Every stop prints its instructions and exits with an error;
complete the step and re-run.

1. When the team reports the current batch annotated, run `uv run snakemake`. It
   prompts you to pick the batch's assignment scopes, exports the finished annotations, and asks
   which DEET run to use - the wizard expects someone to have run and
   finalised a DEET experiment over the batch's gold data. DEET labels the
   rest of the records and puts its predicted positives into a NACSOS review
   scope; the pipeline waits until humans have checked them. It then evaluates
   the stopping criterion and, if screening should continue, trains the
   prioritisation model and writes the next batch.
2. Run snakemake again. The new batch is imported into NACSOS, and the run
   stops once it is up. Tell the team the batch is uploaded: they create assignment
   scopes, and annotate.
3. When the team reports that batch annotated, the cycle comes round again.
   Once the stopping criterion is met, step 1 finishes without a new batch and
   screening is complete.

## Prompt development in deet