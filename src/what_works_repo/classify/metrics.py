"""Ranking-quality metrics for prioritisation models.

The consumer annotates down the full ranking until positives run out, so the
decision readout is how deep into the ranking positives land, not top-k richness.
"""

from typing import Any

import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score


def pooled_auc(y_true: np.ndarray, y_prob: np.ndarray) -> float:
    """ROC-AUC over pooled out-of-fold scores; 0.0 if single-class input."""
    if len(np.unique(y_true)) < 2:
        return 0.0
    return float(roc_auc_score(y_true, y_prob))


def pooled_ap(y_true: np.ndarray, y_prob: np.ndarray) -> float:
    if len(np.unique(y_true)) < 2:
        return 0.0
    return float(average_precision_score(y_true, y_prob))


def positive_rank_summary(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    quantiles: tuple[float, ...] = (0.5, 0.9, 0.99),
) -> dict[str, Any]:
    """Ranks (1-based, best first) of the positives in a descending sort."""
    order = np.argsort(-y_prob, kind="stable")
    ranks = np.flatnonzero(y_true[order] == 1) + 1
    out: dict[str, Any] = {"n_positives": int(len(ranks))}
    for q in quantiles:
        out[f"rank_p{int(q * 100)}"] = int(np.quantile(ranks, q))
    out["rank_max"] = int(ranks.max()) if len(ranks) else None
    return out


def depth_to_recall(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    targets: tuple[float, ...] = (0.95, 0.99, 1.0),
) -> dict[str, int]:
    """Ranking position where cumulative positive recall reaches each target."""
    order = np.argsort(-y_prob, kind="stable")
    pos_hits = np.cumsum(y_true[order] == 1)
    n_pos = int(y_true.sum())
    out: dict[str, int] = {}
    for t in targets:
        needed = int(np.ceil(t * n_pos))
        hits = np.flatnonzero(pos_hits >= needed)
        out[f"depth_recall_{t:g}"] = int(hits[0] + 1) if len(hits) else len(y_true)
    return out
