from pathlib import Path

import pandas as pd
import typer
from sklearn.metrics import f1_score, fbeta_score, precision_score, recall_score
import matplotlib.pyplot as plt


def main(path: Path, path2: Path):
    df_1 = pd.read_csv(filepath_or_buffer=path)
    df_2 = pd.read_csv(filepath_or_buffer=path2)

    fig, ax = plt.subplots()

    ax.scatter(df_1["llm_reasoning"], df_2["llm_reasoning"])

    ax.set_xlabel("probability from " + str(path).split("/")[-1].split("\\")[-2])
    ax.set_ylabel("probability from " + str(path2).split("/")[-1].split("\\")[-2])

    ax.set_title("Comparison of system one probabilities between two datasets")

    plt.show()

if __name__ == "__main__":
    typer.run(main)
