from enum import StrEnum

class OpenAlexSolrImportField(StrEnum):
    ABSTRACT = "abstract"
    TITLE = "title"
    TITLE_ABSTRACT = "title_abstract"

    def __str__(self) -> str:
        return str(self.value)
