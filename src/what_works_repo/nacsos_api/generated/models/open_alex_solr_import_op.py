from enum import StrEnum

class OpenAlexSolrImportOp(StrEnum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
