from enum import StrEnum

class OpenAlexSolrImportDefType(StrEnum):
    DISMAX = "dismax"
    EDISMAX = "edismax"
    LUCENE = "lucene"

    def __str__(self) -> str:
        return str(self.value)
