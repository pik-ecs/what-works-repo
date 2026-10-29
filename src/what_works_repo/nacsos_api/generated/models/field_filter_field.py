from enum import StrEnum

class FieldFilterField(StrEnum):
    ABSTRACT = "abstract"
    DATE = "date"
    PUB_YEAR = "pub_year"
    SOURCE = "source"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
