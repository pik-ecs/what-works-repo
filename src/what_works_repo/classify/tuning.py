"""Candidate registry and Optuna tuning for prioritisation models.

Objective is pooled out-of-fold ROC-AUC: a smooth surrogate for the tail-depth
goal (every positive-above-every-negative pair counts equally, wherever it sits
in the ranking). Folds are computed once in train.py and shared by every
candidate so the comparison is apples-to-apples.
"""

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import optuna
from sklearn.model_selection import StratifiedKFold

from what_works_repo.classify.metrics import (
    depth_to_recall,
    pooled_ap,
    pooled_auc,
    positive_rank_summary,
)
from what_works_repo.classify.models import BertClassifier, SklearnClassifier
from what_works_repo.logging import logger

DEFAULT_SEED = 42
N_FOLDS = 5
BERT_FOLDS = 3
TRIALS_CPU = 300
TRIALS_GPU = 50


@dataclass(frozen=True)
class Candidate:
    name: str
    kind: str  # "sklearn" or "bert"
    builder: Callable[[dict[str, Any]], Any]  # params -> unfitted classifier
    space: Callable[[optuna.Trial], dict[str, Any]]
    n_trials: int
    n_folds: int
    model_name: str | None = None


def _logreg_space(trial: optuna.Trial) -> dict[str, Any]:
    # "weighted": positives overweighted by a swept multiplier.
    weight_mode = trial.suggest_categorical(
        "class_weight", [None, "balanced", "weighted"]
    )
    if weight_mode == "weighted":
        multiplier = trial.suggest_float("positive_weight", 1.0, 8.0, log=True)
        class_weight: Any = {0: 1.0, 1: multiplier}
    else:
        class_weight = weight_mode
    return {
        "clf__C": trial.suggest_float("C", 0.01, 100.0, log=True),
        "clf__class_weight": class_weight,
        "tfidf__min_df": trial.suggest_int("min_df", 1, 5),
        "tfidf__max_df": trial.suggest_float("max_df", 0.6, 1.0),
        "tfidf__ngram_range": (1, trial.suggest_int("ngram_max", 1, 2)),
    }


def _nb_space(trial: optuna.Trial) -> dict[str, Any]:
    return {
        "clf__alpha": trial.suggest_float("alpha", 1e-3, 5.0, log=True),
        "tfidf__min_df": trial.suggest_int("min_df", 1, 5),
        "tfidf__max_df": trial.suggest_float("max_df", 0.6, 1.0),
        "tfidf__ngram_range": (1, trial.suggest_int("ngram_max", 1, 2)),
    }


def _bert_space(trial: optuna.Trial) -> dict[str, Any]:
    # Loss weights are negatives 1.0 / positives positive_weight (1.0 = off).
    # max_length not swept: BERT_DEFAULTS 2048 truncates no measured text.
    return {
        "lr": trial.suggest_float("lr", 2e-6, 1e-4, log=True),
        "epochs": trial.suggest_int("epochs", 2, 5),
        "batch_size": trial.suggest_categorical("batch_size", [8, 16, 32]),
        "weight_decay": trial.suggest_float("weight_decay", 0.0, 0.2),
        "positive_weight": trial.suggest_float("positive_weight", 1.0, 8.0, log=True),
    }


def _bert_builder(model_name: str) -> Callable[[dict[str, Any]], BertClassifier]:
    def build(params: dict[str, Any]) -> BertClassifier:
        return BertClassifier(model_name, params)

    return build


CANDIDATES: dict[str, Candidate] = {
    "logreg": Candidate(
        name="logreg",
        kind="sklearn",
        builder=lambda p: SklearnClassifier("logreg", p),
        space=_logreg_space,
        n_trials=TRIALS_CPU,
        n_folds=N_FOLDS,
    ),
    "nb": Candidate(
        name="nb",
        kind="sklearn",
        builder=lambda p: SklearnClassifier("nb", p),
        space=_nb_space,
        n_trials=TRIALS_CPU,
        n_folds=N_FOLDS,
    ),
    "modernbert": Candidate(
        name="modernbert",
        kind="bert",
        builder=_bert_builder("answerdotai/ModernBERT-base"),
        space=_bert_space,
        n_trials=TRIALS_GPU,
        n_folds=BERT_FOLDS,
        model_name="answerdotai/ModernBERT-base",
    ),
    # ModernBERT continued-pretrained on climate corpora (arXiv:2609.07798).
    # Fallback variant if the merge underperforms on tail depth: A_CX_LRD.
    "climate-modernbert": Candidate(
        name="climate-modernbert",
        kind="bert",
        builder=_bert_builder("CMB-ClimateModernBERT/Merge_Soup_LRD"),
        space=_bert_space,
        n_trials=TRIALS_GPU,
        n_folds=BERT_FOLDS,
        model_name="CMB-ClimateModernBERT/Merge_Soup_LRD",
    ),
}


def out_of_fold_probs(
    candidate: Candidate, x: list[str], y: np.ndarray, params: dict[str, Any], folds
) -> np.ndarray:
    """Score every document once with a model that never saw it."""
    probs = np.zeros(len(x))
    for train_idx, test_idx in folds:
        clf = candidate.builder(dict(params))
        if candidate.kind == "bert":
            clf.params["seed"] = DEFAULT_SEED
        clf.fit([x[i] for i in train_idx], y[train_idx])
        probs[test_idx] = clf.predict_proba([x[i] for i in test_idx])
    return probs


def tune_candidate(
    candidate: Candidate,
    x: list[str],
    y: np.ndarray,
    folds: list[tuple[np.ndarray, np.ndarray]],
    out_dir: Path,
    n_trials: int | None = None,
    seed: int = DEFAULT_SEED,
) -> dict[str, Any]:
    """Optuna TPE search maximizing pooled out-of-fold AUC; writes a result JSON."""
    folds = folds[: candidate.n_folds]
    n_trials = n_trials or candidate.n_trials

    def objective(trial: optuna.Trial) -> float:
        params = candidate.space(trial)
        # best_trial.params holds un-prefixed suggest names; builders need this dict.
        trial.set_user_attr("params", params)
        try:
            probs = out_of_fold_probs(candidate, x, y, params, folds)
        except (ValueError, RuntimeError) as e:
            logger.warning(f"trial {trial.number} failed: {e}")
            return 0.0
        return pooled_auc(y, probs)

    sampler = optuna.samplers.TPESampler(
        seed=seed, n_startup_trials=max(n_trials // 2, 10)
    )
    study = optuna.create_study(
        direction="maximize", sampler=sampler, study_name=candidate.name
    )
    optuna.logging.set_verbosity(optuna.logging.WARNING)
    study.optimize(objective, n_trials=n_trials, catch=(Exception,))

    best = study.best_trial
    best_params = best.user_attrs["params"]
    probs = out_of_fold_probs(candidate, x, y, best_params, folds)
    # Self-contained record: select mode rebuilds everything from this file alone.
    tuning = {
        "model": candidate.name,
        "model_name": candidate.model_name,
        "n_trials": n_trials,
        "n_docs": len(x),
        "n_pos": int(y.sum()),
        "seed": seed,
        "best_params": best_params,
        "auc": pooled_auc(y, probs),
        "ap": pooled_ap(y, probs),
        "trials": [
            {"number": t.number, "value": t.value, "state": t.state.name}
            for t in study.trials
        ],
        "oof_probs": probs.tolist(),
    }
    tuning.update(depth_to_recall(y, probs))
    tuning.update(positive_rank_summary(y, probs))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"tuning_{candidate.name}.json").write_text(np_json_dumps(tuning))
    logger.info(
        f"{candidate.name}: best pooled AUC {tuning['auc']:.4f} params={best_params}"
    )
    return tuning


def np_json_dumps(obj: Any) -> str:
    import json

    def default(o):
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, (np.floating,)):
            return float(o)
        if isinstance(o, tuple):
            return list(o)
        raise TypeError(f"not JSON serializable: {type(o)}")

    return json.dumps(obj, indent=2, default=default)


def shared_folds(
    y: np.ndarray, seed: int = DEFAULT_SEED
) -> list[tuple[np.ndarray, np.ndarray]]:
    return list(
        StratifiedKFold(N_FOLDS, shuffle=True, random_state=seed).split(
            np.zeros(len(y)), y
        )
    )
