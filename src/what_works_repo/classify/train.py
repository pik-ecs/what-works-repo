"""Train the prioritisation model that ranks the remaining corpus.

Labels are every human and DEET verdict collected so far. There is no test split:
selection is argmax pooled out-of-fold AUC on the label pool (see tuning.py), then
refit on all labels. The loop's own later annotation is the real evaluation.
The depth-to-recall report answers "how deep must we annotate to reach the positives".

Two modes so tuning can run as parallel cluster jobs without racing on shared
outputs. Default (tune): each requested candidate writes its self-contained
prioritisation/tuning_<model>.json (trials, best params, metrics, OOF probs) and
nothing else. --select: read every tuning_*.json, pick the argmax-AUC winner,
refit it on all labels, and be the sole writer of model/, model.txt, report.json
and oof_batch<N>.csv.
"""

import json
from typing import Any

import numpy as np
import pandas as pd
import typer

from what_works_repo.batch import Batch, collect_annotations
from what_works_repo.classify.tuning import (
    CANDIDATES,
    DEFAULT_SEED,
    np_json_dumps,
    shared_folds,
    tune_candidate,
)
from what_works_repo.logging import logger


def training_frame() -> pd.DataFrame:
    """One labeled row per document, text built exactly as predict.py builds it."""
    df = collect_annotations(include_text=True)
    # concat with empty per-batch stubs widens incl to object.
    df["incl"] = pd.to_numeric(df["incl"]).astype(int)
    # A document resampled into a later batch can be labeled twice; human verdicts win.
    df = (
        df.sort_values("annotator", key=lambda s: s.ne("human"))
        .drop_duplicates("document_id")
        .reset_index(drop=True)
    )
    # Mirrors predict.py: (row.title or "") + " " + (row.text or "").
    df["text"] = df["name"].fillna("") + " " + df["abstract"].fillna("")
    return df


def _labeled_xy(batch_number: int) -> tuple[pd.DataFrame, list[str], np.ndarray]:
    df = training_frame()
    x = df["text"].tolist()
    y = df["incl"].to_numpy()
    logger.info(f"Training on {len(x)} labeled documents, {int(y.sum())} positive")
    if len(x) == 0 or y.sum() == 0:
        raise ValueError("No labeled data (or no positives) to train on")
    return df, x, y


def tune(batch: Batch, models: list[str], trials: int, seed: int) -> None:
    """Tune each candidate on shared folds; one self-contained JSON per candidate."""
    _, x, y = _labeled_xy(batch.number)
    folds = shared_folds(y, seed)
    for name in models:
        tune_candidate(
            CANDIDATES[name],
            x,
            y,
            folds,
            batch.prioritisation_dir,
            n_trials=trials or None,
            seed=seed,
        )


def _load_tunings(
    batch: Batch, x: list[str], y: np.ndarray, seed: int
) -> dict[str, dict[str, Any]]:
    """All tuning_*.json for this batch, each checked against the current label set."""
    tunings: dict[str, dict[str, Any]] = {}
    for path in sorted(batch.prioritisation_dir.glob("tuning_*.json")):
        tuning = json.loads(path.read_text())
        name = tuning["model"]
        if "n_docs" not in tuning or "oof_probs" not in tuning:
            raise ValueError(
                f"{path.name} is an old-format tuning file; delete and re-tune"
            )
        if (tuning["n_docs"], tuning["n_pos"]) != (len(x), int(y.sum())):
            raise ValueError(
                f"{path.name} tuned on {tuning['n_docs']} docs/{tuning['n_pos']} pos, "
                f"current labels are {len(x)}/{int(y.sum())}; re-tune"
            )
        if tuning.get("seed") != seed:
            raise ValueError(
                f"{path.name} tuned with seed {tuning.get('seed')}, not {seed}"
            )
        tunings[name] = tuning
    if not tunings:
        raise ValueError(
            f"no tuning_*.json under {batch.prioritisation_dir}; run tune first"
        )
    return tunings


def select_and_fit(batch: Batch, seed: int) -> None:
    """Compare tuned candidates, refit the winner, write the pipeline outputs."""
    df, x, y = _labeled_xy(batch.number)
    tunings = _load_tunings(batch, x, y, seed)
    winner_name = max(tunings, key=lambda k: tunings[k]["auc"])
    winner = CANDIDATES[winner_name]
    logger.info(
        f"Winner: {winner_name} (pooled AUC {tunings[winner_name]['auc']:.4f}); "
        f"compared {', '.join(f'{k}={v["auc"]:.4f}' for k, v in tunings.items())}"
    )

    report: dict[str, Any] = {
        "batch": batch.number,
        "n_docs": len(x),
        "n_pos": int(y.sum()),
        "winner": winner_name,
        "candidates": {
            name: {k: v for k, v in tuning.items() if k != "oof_probs"}
            for name, tuning in tunings.items()
        },
    }
    batch.prioritisation_report.write_text(np_json_dumps(report))
    pd.DataFrame(
        {
            "document_id": df["document_id"],
            "batch": df["batch"],
            "incl": y,
            **{
                f"score_{name}": tuning["oof_probs"] for name, tuning in tunings.items()
            },
        }
    ).to_csv(batch.prioritisation_dir / f"oof_batch{batch.number}.csv", index=False)

    fitted = winner.builder(dict(tunings[winner_name]["best_params"]))
    if winner.kind == "bert":
        fitted.params["seed"] = seed
    fitted.fit(x, y)
    fitted.save(batch.model_dir)
    # Sentinel consumed by snakemake; records which candidate produced model_dir.
    batch.model.write_text(f"{winner_name}\n")


def main(
    batch_number: int,
    models: str = ",".join(CANDIDATES),
    trials: int = typer.Option(0, help="Trials per candidate (0 = family default)"),
    seed: int = DEFAULT_SEED,
    select: bool = typer.Option(
        False, help="Skip tuning; aggregate tuning_*.json, refit winner"
    ),
):
    """Tune candidates on shared folds, or --select the winner across tunings."""
    batch = Batch(batch_number)
    if select:
        select_and_fit(batch, seed)
    else:
        tune(batch, [m.strip() for m in models.split(",") if m.strip()], trials, seed)


if __name__ == "__main__":
    typer.run(main)
