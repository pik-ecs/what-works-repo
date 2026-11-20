"""Prioritisation model wrappers: sklearn pipelines and BERT-family fine-tunes.

Both families expose fit(x, y) / predict_proba(x) -> positive-class scores, and
save(path)/load(path) into a directory. transformers and torch are imported
lazily so the sklearn path runs without the ml extra installed.
"""

import json
from pathlib import Path
from typing import Any

import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from what_works_repo.logging import logger

SKLEARN_FILE = "model.sklearn"
INFO_FILE = "model_info.json"

BERT_DEFAULTS: dict[str, Any] = {
    "lr": 3e-5,
    "epochs": 3,
    "batch_size": 16,
    "weight_decay": 0.01,
    # Longest title+abstract measured is ~1760 tokens (labeled pool and raw sample).
    "max_length": 2048,
    # Loss weight for positives; negatives are weighted 1.0. 1.0 disables weighting.
    "positive_weight": 4.0,
    "seed": 42,
}


class SklearnClassifier:
    """TfidfVectorizer + linear classifier, params keyed by pipeline step name."""

    def __init__(self, estimator: str = "logreg", params: dict[str, Any] | None = None):
        self.estimator = estimator
        self.params = params or {}
        self.pipeline = self._build()

    def _build(self) -> Pipeline:
        steps: list[tuple[str, Any]] = [("tfidf", TfidfVectorizer())]
        if self.estimator == "logreg":
            steps.append(("clf", LogisticRegression(max_iter=5000)))
        elif self.estimator == "nb":
            steps.append(("clf", MultinomialNB()))
        else:
            raise ValueError(f"Unknown estimator {self.estimator!r}")
        return Pipeline(steps)

    def fit(self, x: list[str], y: np.ndarray) -> "SklearnClassifier":
        self.pipeline.set_params(**self.params)
        self.pipeline.fit(x, y)
        return self

    def predict_proba(self, x: list[str]) -> np.ndarray:
        return self.pipeline.predict_proba(x)[:, 1]

    def save(self, path: Path) -> None:
        path.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.pipeline, path / SKLEARN_FILE)
        (path / INFO_FILE).write_text(
            json.dumps(
                {"type": "sklearn", "estimator": self.estimator, "params": self.params},
                indent=2,
            )
        )

    @classmethod
    def load(cls, path: Path) -> "SklearnClassifier":
        info = json.loads((path / INFO_FILE).read_text())
        clf = cls(estimator=info["estimator"], params=info["params"])
        clf.pipeline = joblib.load(path / SKLEARN_FILE)
        return clf


class BertClassifier:
    """Sequence-classification fine-tune of a HuggingFace encoder.

    Plain torch loop (no Trainer/datasets deps); dynamic padding; optional
    inverse-frequency class weights. predict_proba returns the positive class.
    """

    def __init__(self, model_name: str, params: dict[str, Any] | None = None):
        self.model_name = model_name
        self.params = {**BERT_DEFAULTS, **(params or {})}
        self._tokenizer: Any = None
        self._model: Any = None
        self._device: Any = None

    def fit(self, x: list[str], y: np.ndarray) -> "BertClassifier":
        import torch
        from torch.utils.data import DataLoader, Dataset
        from transformers import AutoModelForSequenceClassification, AutoTokenizer

        p = self.params
        torch.manual_seed(p["seed"])
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        if tokenizer is None:
            raise RuntimeError(f"No tokenizer for {self.model_name}")
        self._tokenizer = tokenizer

        enc = [tokenizer(t, truncation=True, max_length=p["max_length"]) for t in x]

        class _TokDS(Dataset):
            def __len__(self) -> int:
                return len(enc)

            def __getitem__(self, index: int) -> tuple[list[int], list[int], int]:
                return (
                    enc[index]["input_ids"],
                    enc[index]["attention_mask"],
                    int(y[index]),
                )

        def collate(batch):
            width = max(len(ids) for ids, _, _ in batch)
            pad_id = tokenizer.pad_token_id or 0
            ids = torch.tensor(
                [ids + [pad_id] * (width - len(ids)) for ids, _, _ in batch]
            )
            mask = torch.tensor([m + [0] * (width - len(m)) for _, m, _ in batch])
            labels = torch.tensor([lab for _, _, lab in batch])
            return ids, mask, labels

        # Halve batch when texts are long (p90 width), not when the cap is.
        widths = [len(e["input_ids"]) for e in enc]
        eff_batch = (
            p["batch_size"] // 2
            if np.quantile(widths, 0.9) >= 1024
            else p["batch_size"]
        )
        loader = DataLoader(
            _TokDS(), batch_size=eff_batch, shuffle=True, collate_fn=collate
        )

        model = AutoModelForSequenceClassification.from_pretrained(
            self.model_name, num_labels=2, ignore_mismatched_sizes=True
        ).to(device)
        weights = torch.tensor(
            [1.0, p["positive_weight"]], dtype=torch.float32, device=device
        )
        counts = np.bincount(y, minlength=2)
        logger.info(f"Loss weights {weights.tolist()} (label counts {counts.tolist()})")
        loss_fn = torch.nn.CrossEntropyLoss(weight=weights)
        opt = torch.optim.AdamW(
            model.parameters(), lr=p["lr"], weight_decay=p["weight_decay"]
        )
        steps = p["epochs"] * max(len(loader), 1)
        sched = torch.optim.lr_scheduler.LinearLR(
            opt, start_factor=1.0, end_factor=0.0, total_iters=steps
        )
        use_amp = device.type == "cuda"
        for _ in range(p["epochs"]):
            model.train()
            for ids, mask, labels in loader:
                ids, mask, labels = ids.to(device), mask.to(device), labels.to(device)
                opt.zero_grad()
                with torch.autocast(device.type, torch.bfloat16, enabled=use_amp):
                    logits = model(input_ids=ids, attention_mask=mask).logits
                # Loss applied here; labels= on forward would use unweighted CE.
                loss = loss_fn(logits.float(), labels)
                loss.backward()
                opt.step()
                sched.step()
        self._model = model
        self._device = device
        return self

    def predict_proba(self, x: list[str], batch_size: int = 32) -> np.ndarray:
        import torch

        model, tokenizer = self._model, self._tokenizer
        if model is None or tokenizer is None:
            raise RuntimeError("Call fit() or load() before predict_proba()")
        device = self._device
        scores = []
        for i in range(0, len(x), batch_size):
            enc = tokenizer(
                x[i : i + batch_size],
                truncation=True,
                max_length=self.params["max_length"],
                padding=True,
                return_tensors="pt",
            ).to(device)
            model.eval()
            with torch.no_grad():
                logits = model(**enc).logits
            scores.append(torch.softmax(logits.float(), dim=-1)[:, 1].cpu().numpy())
        return np.concatenate(scores)

    def save(self, path: Path) -> None:
        path.mkdir(parents=True, exist_ok=True)
        self._model.save_pretrained(path)
        self._tokenizer.save_pretrained(path)
        (path / INFO_FILE).write_text(
            json.dumps(
                {"type": "bert", "model_name": self.model_name, "params": self.params},
                indent=2,
            )
        )

    @classmethod
    def load(cls, path: Path) -> "BertClassifier":
        import torch
        from transformers import AutoModelForSequenceClassification, AutoTokenizer

        info = json.loads((path / INFO_FILE).read_text())
        clf = cls(info["model_name"], info["params"])
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        clf._tokenizer = AutoTokenizer.from_pretrained(path)
        clf._model = AutoModelForSequenceClassification.from_pretrained(path).to(device)
        clf._device = device
        return clf


def load_classifier(path: Path) -> SklearnClassifier | BertClassifier:
    """Format-detecting loader for a saved prioritisation model directory."""
    info = json.loads((path / INFO_FILE).read_text())
    if info["type"] == "sklearn":
        return SklearnClassifier.load(path)
    return BertClassifier.load(path)
