from enum import StrEnum

class FieldFiltersField(StrEnum):
    DOI = "doi"
    ITEM_ID = "item_id"
    OPENALEX_ID = "openalex_id"

    def __str__(self) -> str:
        return str(self.value)
