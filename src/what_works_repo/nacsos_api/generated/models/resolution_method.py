from enum import StrEnum

class ResolutionMethod(StrEnum):
    FIRST = "first"
    LAST = "last"
    MAJORITY = "majority"
    TRUST = "trust"

    def __str__(self) -> str:
        return str(self.value)
