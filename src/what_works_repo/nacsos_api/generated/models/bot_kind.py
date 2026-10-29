from enum import StrEnum

class BotKind(StrEnum):
    CLASSIFICATION = "CLASSIFICATION"
    RESOLVE = "RESOLVE"
    RULES = "RULES"
    SCRIPT = "SCRIPT"
    TOPICS = "TOPICS"

    def __str__(self) -> str:
        return str(self.value)
