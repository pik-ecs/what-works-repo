"""Generate plots"""

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from what_works_repo.batch import collect_annotations, collect_original_annotations
from what_works_repo.constants import FIGURES_DIR, TABLES_DIR
from what_works_repo.reporting import irr


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


def _drop_batches(df: "pd.DataFrame", exclude: list[int]) -> "pd.DataFrame":
    """Remove the given batch numbers from a collected annotations frame."""
    return df[~df["batch"].isin(exclude)]


def annotation_progress(
    output: Path = FIGURES_DIR / "progress.svg", exclude: list[int] | None = None
) -> None:
    """Plot cumulative includes against documents annotated, and write the table."""
    plt.rcParams["svg.hashsalt"] = "what-works-repo"
    exclude = exclude or []
    df = _drop_batches(collect_annotations(), exclude)
    fig = plot_annotation_progress(df)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, metadata={"Date": None})
    annotation_progress_table(
        df, originals=_drop_batches(collect_original_annotations(), exclude)
    )


# --- Inter-coder reliability figures (metrics in reporting/irr.py) ---

# (beta, colour, linestyle) for the iso-Fβ contour families in the coder plot.
_FBETA_STYLE = ((1, "#bbbbbb", "dashed"), (2, "#b07aa1", "dotted"))

# Landis & Koch agreement bands (kappa), for reference shading.
_KAPPA_BANDS = [
    (0.0, "none"),
    (0.20, "slight"),
    (0.40, "fair"),
    (0.60, "moderate"),
    (0.80, "substantial"),
    (1.01, "almost perfect"),
]


def _initials(username: str) -> str:
    """``harry.fearnehough`` -> ``HF``, for figure labels."""
    return "".join(p[0] for p in username.split(".") if p)[:2].upper()


def _kappa_band_shading(ax: plt.Axes) -> None:
    """Alternate light-grey spans over the Landis & Koch bands along κ (x)."""
    lo = 0.0
    for i, (hi, name) in enumerate(_KAPPA_BANDS):
        if i == 0:
            lo = hi
            continue
        hi = min(hi, 1.0)
        ax.axvspan(lo, hi, color="#000000", alpha=0.03 if i % 2 else 0.06, zorder=0)
        ax.text(
            (lo + hi) / 2,
            1.008,
            name,
            ha="center",
            va="bottom",
            fontsize=9.5,
            color="#888888",
            zorder=1,
            clip_on=False,
            transform=ax.get_xaxis_transform(),
        )
        lo = hi


def plot_pairwise_kappa(mat: pd.DataFrame) -> plt.Figure:
    """Heatmap of pairwise Cohen's kappa; sparse pairs and diagonal greyed."""
    labels = [_initials(c) for c in mat.index]
    off = mat.to_numpy(dtype=float).copy()
    np.fill_diagonal(off, np.nan)
    fig, ax = plt.subplots(figsize=(8.5, 7.2), layout="constrained")
    cmap = plt.get_cmap("RdYlBu").copy()
    cmap.set_bad("#eeeeee")
    im = ax.imshow(off, cmap=cmap, vmin=-0.4, vmax=0.8, aspect="equal")
    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=90, fontsize=8)
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xticks(np.arange(-0.5, len(labels), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(labels), 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=1)
    ax.tick_params(which="minor", length=0)
    for i in range(len(labels)):
        for j in range(len(labels)):
            if not np.isnan(off[i, j]):
                ax.text(
                    j, i, f"{off[i, j]:.2f}", ha="center", va="center", fontsize=6.5
                )
    fig.colorbar(im, ax=ax, shrink=0.7, label="Cohen's κ")
    ax.set_title("Pairwise coder agreement (Cohen's κ), batches pooled")
    return fig


def plot_pairwise_kappa_bars(pairs: pd.DataFrame) -> plt.Figure:
    """Coder-pair Cohen's kappa as horizontal bars over the agreement bands.

    Consumes ``irr.pairwise_table``; sparse (NaN kappa) pairs are dropped.
    Bars are labelled with the co-annotated item count past the bar end.
    """
    pairs = pairs.dropna(subset=["kappa"]).sort_values("kappa", ignore_index=True)
    fig, ax = plt.subplots(figsize=(8.5, 0.32 * len(pairs) + 1.6), layout="constrained")
    if pairs.empty:
        ax.text(0.5, 0.5, "No coder pair co-annotated enough items", ha="center")
        ax.set_axis_off()
        return fig
    _kappa_band_shading(ax)
    y = range(len(pairs))
    ax.barh(y, pairs["kappa"], color="#4c78a8", zorder=2)
    for yi, (kappa, shared) in enumerate(
        zip(pairs["kappa"], pairs["shared"], strict=True)
    ):
        ax.text(
            kappa + 0.015,
            yi,
            f"{kappa:.2f}  (n={shared})",
            va="center",
            ha="left",
            fontsize=7,
            color="#666666",
            zorder=3,
        )
    ax.set_ylim(-0.6, len(pairs) - 0.4)
    ax.set_yticks(list(y))
    ax.set_yticklabels(
        [
            f"{_initials(a)}+{_initials(b)}"
            for a, b in zip(pairs["coder_a"], pairs["coder_b"], strict=True)
        ],
        fontsize=8,
    )
    ax.set_xlabel("Cohen's κ")
    ax.set_xlim(min(0.0, pairs["kappa"].min() - 0.02), 1.0)
    ax.set_title(
        "Pairwise coder agreement (Cohen's κ) — in/out screen, batches pooled",
        pad=30,
    )
    return fig


def _draw_fbeta_contours(ax: plt.Axes) -> None:
    """Curves of constant Fβ, Fβ = (1+β²)PR / (β²P + R), so each coder's F is
    readable off their position. F2 bows toward the recall axis."""
    grid = np.linspace(0.001, 1, 300)
    r, p = np.meshgrid(grid, grid)
    for beta, color, style in _FBETA_STYLE:
        f_beta = (1 + beta**2) * p * r / (beta**2 * p + r)
        cs = ax.contour(
            r,
            p,
            f_beta,
            levels=[0.2, 0.4, 0.6, 0.8],
            colors=color,
            linewidths=0.9,
            linestyles=style,
            zorder=1,
        )
        ax.clabel(cs, fmt=lambda v, b=beta: f"F{b}={v:.1f}", fontsize=7, colors=color)


def plot_coder_pr(f1df: pd.DataFrame) -> plt.Figure:
    """Precision-recall scatter of coders vs the resolved value.

    Marker size grows with documents screened; the pooled score is a red star,
    the average coder a diamond. Over-includers sit bottom-right,
    under-includers top-left.
    """
    summ = f1df[f1df["coder"].isin(irr.SUMMARY_ROWS)].set_index("coder")
    per = f1df[~f1df["coder"].isin(irr.SUMMARY_ROWS)]
    fig, ax = plt.subplots(figsize=(7.2, 6.4), layout="constrained")
    _draw_fbeta_contours(ax)

    nmax = per["n"].max()

    def size(n: float) -> float:
        return 90 + 230 * (n / nmax) ** 0.5

    ax.scatter(
        per["recall"],
        per["precision"],
        s=[size(n) for n in per["n"]],
        facecolors="#4c78a8",
        edgecolors="white",
        linewidths=1.0,
        alpha=0.85,
        zorder=3,
    )
    for row in per.itertuples():
        ax.annotate(
            _initials(row.coder),
            (row.recall, row.precision),
            ha="center",
            va="center",
            fontsize=6,
            color="white",
            fontweight="bold",
            zorder=4,
        )

    handles = [
        plt.Line2D([0], [0], color="#bbbbbb", linestyle="dashed", label="iso-F1"),
        plt.Line2D(
            [0],
            [0],
            color="#b07aa1",
            linestyle="dotted",
            label="iso-F2 (recall-weighted)",
        ),
    ]
    marks = {"pooled": ("*", "#d62728", 260), "average coder": ("D", "#333333", 120)}
    for name, (marker, color, ms) in marks.items():
        if name in summ.index:
            row = summ.loc[name]
            ax.scatter(
                row["recall"],
                row["precision"],
                marker=marker,
                s=ms,
                facecolors=color,
                edgecolors="white",
                linewidths=1.2,
                zorder=5,
            )
            handles.append(
                plt.Line2D(
                    [0],
                    [0],
                    marker=marker,
                    color=color,
                    linestyle="none",
                    markersize=11 if marker == "*" else 8,
                    label=name,
                )
            )

    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(-0.03, 1.05)
    ax.set_xlabel("recall  (of the relevant papers, how many the coder caught)")
    ax.set_ylabel("precision  (of the coder's includes, how many were relevant)")
    ax.set_aspect("equal")
    ax.set_title("Coder precision vs recall against the resolved value")
    ax.legend(handles=handles, loc="lower left", fontsize=8.5)
    ax.annotate(
        "marker size ∝ documents screened",
        (0.98, 0.02),
        xycoords="axes fraction",
        ha="right",
        va="bottom",
        fontsize=8,
        color="#666666",
    )
    return fig


def render_irr(
    min_shared: int = 25,
    output_dir: Path = FIGURES_DIR,
    exclude: list[int] | None = None,
) -> None:
    """Write the pairwise-kappa heatmap, kappa bars, and coder PR plot."""
    plt.rcParams["svg.hashsalt"] = "what-works-repo"
    exclude = exclude or []
    originals = _drop_batches(collect_original_annotations(), exclude)
    resolved = _drop_batches(collect_annotations(), exclude)
    if originals["annotator"].nunique() < 2:
        print("Skipping IRR figures: fewer than two coders left after exclusions.")
        return
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, fig in [
        (
            "pairwise_kappa",
            plot_pairwise_kappa(irr.pairwise_kappa(originals, min_shared)),
        ),
        (
            "pairwise_kappa_bars",
            plot_pairwise_kappa_bars(irr.pairwise_table(originals, min_shared)),
        ),
        ("coder_pr", plot_coder_pr(irr.coder_pr(originals, resolved))),
    ]:
        fig.savefig(output_dir / f"{name}.svg", metadata={"Date": None})
        plt.close(fig)
