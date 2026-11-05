from enum import StrEnum

class RISLabelFormat(StrEnum):
    CHOICE_NAMES = "CHOICE_NAMES"
    LABEL_AND_CHOICE_NAMES = "LABEL_AND_CHOICE_NAMES"
    RAW_TAGS = "RAW_TAGS"

    def __str__(self) -> str:
        return str(self.value)
