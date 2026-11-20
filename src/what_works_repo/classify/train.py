"""Train the prioritisation model that ranks the remaining corpus.

Labels are every human and DEET verdict collected so far. There is no test split:
selection is argmax pooled out-of-fold AUC on the label pool (see tuning.py), then
refit on all labels. The loop's own later annotation is the real evaluation. The
depth-to-recall report answers "how deep must we annotate to reach the positives".
"""

from typing import Any

import numpy as np
import pandas as pd
import typer

from what_works_repo.batch import Batch, collect_annotations
from what_works_repo.classify.metrics import (
    depth_to_recall,
    pooled_ap,
    positive_rank_summary,
)
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


def main(
    batch_number: int,
    models: str = ",".join(CANDIDATES),
    trials: int = typer.Option(0, help="Trials per candidate (0 = family default)"),
    seed: int = DEFAULT_SEED,
):
    """Tune candidates on shared folds, refit the winner, store it for predict.py."""
    batch = Batch(batch_number)
    df = training_frame()
    x = df["text"].tolist()
    y = df["incl"].to_numpy()
    logger.info(f"Training on {len(x)} labeled documents, {int(y.sum())} positive")
    if len(x) == 0 or y.sum() == 0:
        raise ValueError("No labeled data (or no positives) to train on")

    folds = shared_folds(y, seed)
    out_dir = batch.prioritisation_dir
    names = [m.strip() for m in models.split(",") if m.strip()]

    report: dict[str, Any] = {
        "batch": batch_number,
        "n_docs": len(x),
        "n_pos": int(y.sum()),
        "candidates": {},
    }
    oof: dict[str, np.ndarray] = {}
    for name in names:
        candidate = CANDIDATES[name]
        result = tune_candidate(
            candidate, x, y, folds, out_dir, n_trials=trials or None, seed=seed
        )
        probs = result.pop("oof_probs")
        oof[name] = probs
        result["ap"] = pooled_ap(y, probs)
        result.update(depth_to_recall(y, probs))
        result.update(positive_rank_summary(y, probs))
        report["candidates"][name] = result

    winner_name = max(
        report["candidates"], key=lambda k: report["candidates"][k]["auc"]
    )
    winner = CANDIDATES[winner_name]
    best_params = report["candidates"][winner_name]["best_params"]
    winner_auc = report["candidates"][winner_name]["auc"]
    logger.info(f"Winner: {winner_name} (pooled AUC {winner_auc:.4f})")
    fitted = winner.builder(dict(best_params))
    if winner.kind == "bert":
        fitted.params["seed"] = seed
    fitted.fit(x, y)
    fitted.save(batch.model_dir)

    report["winner"] = winner_name
    report_path = batch.prioritisation_report
    report_path.write_text(np_json_dumps(report))
    pd.DataFrame(
        {
            "document_id": df["document_id"],
            "batch": df["batch"],
            "incl": y,
            **{f"score_{name}": oof[name] for name in names},
        }
    ).to_csv(out_dir / f"oof_batch{batch_number}.csv", index=False)
    # Sentinel consumed by snakemake; records which candidate produced model_dir.
    batch.model.write_text(f"{winner_name}\n")


if __name__ == "__main__":
    typer.run(main)
