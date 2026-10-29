from enum import StrEnum

class LabelFilterIntType(StrEnum):
    BOT = "bot"
    RESOLVED = "resolved"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
