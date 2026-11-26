from pathlib import Path

import pandas as pd
import typer
from sklearn.metrics import f1_score, fbeta_score, precision_score, recall_score


def main(path: Path, thresh: float, beta: float = 2):
    df = pd.read_csv(filepath_or_buffer=path)
    y_true = df["human_extraction"]
    y_pred = df["llm_reasoning"].astype(float) > thresh
    print("F1: ", f1_score(y_true, y_pred))
    print("Precision: ", precision_score(y_true, y_pred))
    print("Recall: ", recall_score(y_true, y_pred))
    print(f"F_{beta} ", fbeta_score(y_true, y_pred, beta=beta))


if __name__ == "__main__":
    typer.run(main)
