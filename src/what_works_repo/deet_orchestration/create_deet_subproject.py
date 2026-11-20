"""Create a deet subproject from a batch."""

import csv
import os
import shutil
from contextlib import chdir
from pathlib import Path

import typer
import yaml
from deet.data_models.documents import ContextType
from deet.data_models.enums import EvaluationStrategyName
from deet.data_models.project import DeetProject
from deet.extractors.llm_data_extractor import DataExtractionConfig, LLMProvider
from deet.processors.converter_register import SupportedImportFormat


def _gold_is_empty(path: Path) -> bool:
    with path.open(newline="", encoding="utf-8") as f:
        rows = csv.reader(f)
        next(rows, None)
        return next(rows, None) is None


def _copy_previous_batch_project(deet_project_dir: Path) -> None:
    """All-DEET batch: reuse the previous batch's deet project wholesale.

    With no human annotations there is no gold to build a project from, and
    DEET's csv converter rejects the empty file. The copy carries the tuned
    prompts, extraction config, and finalized runs forward, and its
    gold_standard_data_path still resolves to the previous batch's gold.
    Only the project name is rewritten.
    """
    batch_n = int(deet_project_dir.name.split("_", 1)[1])
    previous = deet_project_dir.parent / f"batch_{batch_n - 1}"
    if not (previous / "project.yaml").exists():
        raise FileNotFoundError(
            f"no deet project under {previous} to reuse for all-deet batch {batch_n}"
        )
    shutil.copytree(previous, deet_project_dir, dirs_exist_ok=True)
    config_path = deet_project_dir / "project.yaml"
    config = yaml.safe_load(config_path.read_text())
    config["project"]["name"] = deet_project_dir.name
    config_path.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")


def main(annotation_path: Path, config_target: Path):
    deet_project_dir = config_target.parent
    if _gold_is_empty(annotation_path):
        _copy_previous_batch_project(deet_project_dir)
        return

    relative_annotation_path = Path(os.path.relpath(annotation_path, deet_project_dir))

    with chdir(deet_project_dir):
        project = DeetProject(
            name=deet_project_dir.name,
            gold_standard_data_format=SupportedImportFormat.GENERIC_CSV,
            gold_standard_data_path=relative_annotation_path,
            pdf_dir=None,
            evaluation_strategy=EvaluationStrategyName.DEV_VAL_TEST,
        )
        project.setup()

        config = DataExtractionConfig(
            default_context_type=ContextType.ABSTRACT_ONLY,
            provider=LLMProvider.OLLAMA,
            model="smollm:360m",
        )
        project.config_path.write_text(
            yaml.safe_dump(config.model_dump(mode="json"), sort_keys=False),
            encoding="utf-8",
        )


if __name__ == "__main__":
    typer.run(main)
