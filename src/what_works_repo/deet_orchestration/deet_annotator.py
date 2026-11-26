"""
Create annotations from a deet config
"""

import csv
from pathlib import Path

from deet.data_models.base import Attribute, AttributeType
from deet.data_models.documents import ContextType, Document, DocumentIdentity
from deet.data_models.extraction import ExtractionRunOutput
from deet.data_models.project import ExperimentArtefacts
from deet.extractors.llm_data_extractor import DataExtractionConfig, LLMDataExtractor
from deet.processors.parser import ParsedOutput
from destiny_sdk.references import ReferenceFileInput


class DeetAnnotator:
    def __init__(self, experiment: ExperimentArtefacts, max_workers: int = 1) -> None:
        self.config = DataExtractionConfig.from_yaml(experiment.config_snapshot)
        self.config.max_workers = max(1, max_workers)
        self.extractor = LLMDataExtractor(config=self.config)
        self.parse_attributes(experiment.prompts_snapshot)

    def parse_attributes(self, prompt_path: Path) -> None:
        """Parse attributes from a prompt path"""
        with prompt_path.open(newline="", encoding="utf-8") as csv_file:
            self.attributes = [
                Attribute(
                    prompt=row["prompt"],
                    output_data_type=AttributeType(row["output_data_type"]),
                    attribute_id=int(row["attribute_id"]),
                    attribute_label=row["attribute_label"],
                )
                for row in csv.DictReader(csv_file)
                if row["output_data_type"] == "bool"
            ]

    def predict_batch(self, texts: dict[str, str]) -> ExtractionRunOutput:
        """Extract from {document_id: text} in one thread-pooled DEET run.

        Citation metadata is unused (context comes from the parsed text), so
        each document carries a synthetic identity built from its external id;
        that also keeps DEET from parsing an empty Labs citation per document.
        """
        documents = [
            Document(
                name=doc_id,
                citation=ReferenceFileInput(),
                document_id=doc_id,
                document_identity=DocumentIdentity(
                    doi=None, first_author=None, year=None, external_id=doc_id
                ),
                parsed_document=ParsedOutput(text=text, parser_library="unknown"),
            )
            for doc_id, text in texts.items()
        ]
        return self.extractor.extract_from_documents(
            attributes=self.attributes,
            documents=documents,
            context_type=ContextType.FULL_DOCUMENT,
            show_progress=True,
        )
