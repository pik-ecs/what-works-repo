from pathlib import Path

import pandas as pd
import typer
from sklearn.metrics import f1_score, fbeta_score, precision_score, recall_score
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


def main(path: Path, path2: Path):
    df_1 = pd.read_csv(filepath_or_buffer=path)
    df_2 = pd.read_csv(filepath_or_buffer=path2)

    fig, ax = plt.subplots()

    ConfusionMatrixDisplay.from_predictions(
        y_true=df_1["llm_extraction"],
        y_pred=df_2["llm_extraction"],
        ax=ax,
    )


    plt.show()

if __name__ == "__main__":
    typer.run(main)
