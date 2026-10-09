"""Collect annotations into one megabatch."""

import pandas as pd
import typer

from what_works_repo.batch import Batch
from what_works_repo.constants import DEET_MEGABATCH_DIR
from what_works_repo.settings import settings


def main():
    annotations = pd.concat(
        [
            pd.read_csv(Batch(n).annotations)
            for n in range(
                settings.deet_eval.megabatch_start, settings.deet_eval.megabatch_end + 1
            )
        ],
        ignore_index=True,
    )
    annotations.to_csv(DEET_MEGABATCH_DIR / "annotations.csv", index=False)


if __name__ == "__main__":
    typer.run(main)
