from enum import StrEnum

class ExportTypeEnum(StrEnum):
    CSV = "csv"
    EXCEL = "excel"
    JSONL = "jsonl"
    RIS = "ris"

    def __str__(self) -> str:
        return str(self.value)
