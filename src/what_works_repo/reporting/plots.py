"""Generate plots"""

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

import matplotlib.pyplot as plt
import pandas as pd
import typer

from what_works_repo.batch import collect_annotations
from what_works_repo.constants import FIGURES_DIR

app = typer.Typer()


def plot_annotation_progress(df: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.plot(df["incl"].cumsum())
    ax.set_xlabel("Documents seen")
    ax.set_ylabel("Relevant documents seen")

    ends = df.groupby("batch").size().cumsum().to_list()
    for batch, x in zip(df["batch"].unique(), ends, strict=True):
        ax.axvline(float(x), color="0.85", lw=0.8)
        ax.annotate(
            f"{batch}",
            (x, 0),
            xytext=(0, 3),
            textcoords="offset points",
            ha="right",
            fontsize=7,
            color="0.4",
        )
    return fig


@app.command()
def annotation_progress(output: Path = FIGURES_DIR / "progress.svg") -> None:
    """Plot cumulative includes against documents annotated."""
    plt.rcParams["svg.hashsalt"] = "what-works-repo"
    fig = plot_annotation_progress(collect_annotations())
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, metadata={"Date": None})


if __name__ == "__main__":
    app()
