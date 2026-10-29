from enum import StrEnum

class LabelFilterBoolType(StrEnum):
    BOT = "bot"
    RESOLVED = "resolved"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
