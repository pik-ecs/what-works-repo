"""Generate plots"""

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

import matplotlib.pyplot as plt
import pandas as pd
import typer

from what_works_repo.batch import collect_annotations
from what_works_repo.constants import FIGURES_DIR, TABLES_DIR

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


def annotation_progress_table(
    df: pd.DataFrame,
    output: Path = TABLES_DIR / "annotation_progress.md",
) -> None:
    """Write a per-batch markdown table of screening counts and rates."""
    human = df[df["annotator"] == "human"]
    stats = human.groupby("batch").agg(
        records=("incl", "size"), included=("incl", "sum")
    )

    lines = [
        "| Batch | Records | Included | Inclusion rate |",
        "| --- | ---: | ---: | ---: |",
    ]
    for batch, row in stats.iterrows():
        rate = row["included"] / row["records"]
        lines.append(f"| {batch} | {row['records']} | {row['included']} | {rate:.1%} |")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n")


@app.command()
def annotation_progress(output: Path = FIGURES_DIR / "progress.svg") -> None:
    """Plot cumulative includes against documents annotated, and write the table."""
    plt.rcParams["svg.hashsalt"] = "what-works-repo"
    df = collect_annotations()
    fig = plot_annotation_progress(df)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, metadata={"Date": None})
    annotation_progress_table(df)


if __name__ == "__main__":
    app()
