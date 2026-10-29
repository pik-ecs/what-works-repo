"""Inter-coder reliability metrics from the original human annotations.

Rewritten from impact-case-1's ic1.reporting loaders/annotation.py,
simplified for this repo's data model: a single ``incl`` column with no
abstentions, and the resolved value in a separate file from the original
per-annotator rows. Plots for these tables live in ``plots.py``.
"""

from itertools import combinations

import numpy as np
import pandas as pd
from sklearn.metrics import (
    cohen_kappa_score,
    f1_score,
    precision_score,
    recall_score,
)

SUMMARY_ROWS = ("average coder", "pooled")


def _dedupe(originals: pd.DataFrame) -> pd.DataFrame:
    """One row per (batch, document, coder); include wins on contradictions."""
    return originals.sort_values("incl").drop_duplicates(
        ["batch", "document_id", "annotator"], keep="last"
    )


def _wide(originals: pd.DataFrame) -> pd.DataFrame:
    """Documents x coders matrix of incl, one row per (batch, document)."""
    return _dedupe(originals).pivot_table(
        index=["batch", "document_id"], columns="annotator", values="incl"
    )


def pairwise_table(originals: pd.DataFrame, min_shared: int = 25) -> pd.DataFrame:
    """Coder pairs with co-annotated item count and Cohen's kappa.

    Pairs sharing fewer than ``min_shared`` items, or lacking decision variety
    on either side, get NaN kappa. Batch is part of the item key so the pooled
    pivot cannot join same-id documents from different batches.
    """
    wide = _wide(originals)
    rows = []
    for a, b in combinations(sorted(wide.columns), 2):
        pair = wide[[a, b]].dropna()
        sparse = (
            len(pair) < min_shared or pair[a].nunique() < 2 or pair[b].nunique() < 2
        )
        rows.append(
            {
                "coder_a": a,
                "coder_b": b,
                "shared": len(pair),
                "kappa": np.nan if sparse else cohen_kappa_score(pair[a], pair[b]),
            }
        )
    table = pd.DataFrame(rows, columns=["coder_a", "coder_b", "shared", "kappa"])
    table["shared"] = table["shared"].astype(int)
    table["kappa"] = table["kappa"].astype(float)
    return table.sort_values("kappa", ascending=False, ignore_index=True)


def pairwise_kappa(originals: pd.DataFrame, min_shared: int = 25) -> pd.DataFrame:
    """Coder x coder matrix of Cohen's kappa, diagonal 1.0, sparse pairs NaN."""
    wide = _wide(originals)
    coders = sorted(wide.columns)
    mat = pd.DataFrame(np.nan, index=coders, columns=coders, dtype=float)
    for coder in coders:
        mat.loc[coder, coder] = 1.0
    for a, b in combinations(coders, 2):
        pair = wide[[a, b]].dropna()
        if len(pair) < min_shared or pair[a].nunique() < 2 or pair[b].nunique() < 2:
            continue
        kappa = cohen_kappa_score(pair[a], pair[b])
        mat.loc[a, b] = mat.loc[b, a] = kappa
    return mat


def coder_pr(originals: pd.DataFrame, resolved: pd.DataFrame) -> pd.DataFrame:
    """Per-coder precision/recall/F1 against the resolved human labels.

    One row per coder with ``n`` scored items, plus an ``average coder`` row
    (macro mean of the coders) and a ``pooled`` row (every coder decision in
    one confusion matrix). Resolvers score against their own adjudications, so
    the plot understates their disagreement with the rest.
    """
    gold = (
        resolved.loc[resolved["annotator"] == "human", ["batch", "document_id", "incl"]]
        .rename(columns={"incl": "gold"})
        .drop_duplicates(["batch", "document_id"])
    )
    gold["gold"] = pd.to_numeric(gold["gold"])
    scored = _dedupe(originals).merge(gold, on=["batch", "document_id"])
    if scored.empty:
        return pd.DataFrame(columns=["coder", "n", "precision", "recall", "f1"])

    def _pr(yt: np.ndarray, yp: np.ndarray) -> dict:
        return {
            "precision": precision_score(yt, yp, zero_division=0),
            "recall": recall_score(yt, yp, zero_division=0),
            "f1": f1_score(yt, yp, zero_division=0),
        }

    rows = [
        {
            "coder": coder,
            "n": len(group),
            **_pr(group["gold"].to_numpy(), group["incl"].to_numpy()),
        }
        for coder, group in scored.groupby("annotator")
    ]
    per = pd.DataFrame(rows).sort_values("f1", ascending=False, ignore_index=True)
    pooled = {
        "coder": "pooled",
        "n": len(scored),
        **_pr(scored["gold"].to_numpy(), scored["incl"].to_numpy()),
    }
    average = {
        "coder": "average coder",
        "n": int(per["n"].mean()),
        **per[["precision", "recall", "f1"]].mean().to_dict(),
    }
    return pd.concat([per, pd.DataFrame([average, pooled])], ignore_index=True)
