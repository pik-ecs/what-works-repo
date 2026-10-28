from enum import StrEnum

class LabelFilterMultiType(StrEnum):
    BOT = "bot"
    RESOLVED = "resolved"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
