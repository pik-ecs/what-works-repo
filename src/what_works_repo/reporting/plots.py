"""Generate plots"""

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

import matplotlib.pyplot as plt
import pandas as pd
import typer

from what_works_repo.batch import collect_annotations, collect_original_annotations
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


def unanimous_include_share(human: pd.DataFrame, originals: pd.DataFrame) -> pd.Series:
    """Share of finally-included documents that every annotator included.

    Documents whose inclusion the resolution had to force past an annotator's
    veto do not count. Single-annotator documents are trivially unanimous.
    """
    shares = {}
    for batch, group in human.groupby("batch"):
        included = group.loc[group["incl"] == 1, "document_id"]
        batch_originals = originals.loc[originals["batch"] == batch]
        if included.empty or not set(included) <= set(batch_originals["document_id"]):
            shares[batch] = float("nan")
            continue
        every = batch_originals.groupby("document_id")["incl"].min()
        shares[batch] = (every.loc[list(included)] == 1).mean()
    return pd.Series(shares)


def annotation_progress_table(
    df: pd.DataFrame,
    originals: pd.DataFrame | None = None,
    output: Path = TABLES_DIR / "annotation_progress.md",
) -> None:
    """Write a per-batch markdown table of screening counts and rates."""
    human = df[df["annotator"] == "human"]
    stats = human.groupby("batch").agg(
        records=("incl", "size"), included=("incl", "sum")
    )
    shares = (
        unanimous_include_share(human, originals)
        if originals is not None
        else pd.Series(dtype=float)
    )

    lines = [
        "| Batch | Records | Included | Inclusion rate | Unanimous includes |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for batch, row in stats.iterrows():
        rate = row["included"] / row["records"]
        share = shares.get(batch, float("nan"))
        share_str = "—" if pd.isna(share) else f"{share:.1%}"
        lines.append(
            f"| {batch} | {row['records']} | {row['included']} "
            f"| {rate:.1%} | {share_str} |"
        )

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
    annotation_progress_table(df, originals=collect_original_annotations())


if __name__ == "__main__":
    app()
