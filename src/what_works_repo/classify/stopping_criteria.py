"""Calculate stopping criteria based on annotations in batches."""

import typer
from buscarpy import calculate_h0

from what_works_repo.batch import Batch, collect_annotations
from what_works_repo.utils import count_documents


def main(batch_n: int):
    batch = Batch(batch_n)
    df = collect_annotations()
    df = df[df["batch"] <= batch_n]
    N = count_documents()
    p = calculate_h0(df["incl"], N)
    batch.stopping_decision.write_text(f"{p}")


if __name__ == "__main__":
    typer.run(main)
