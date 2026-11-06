from enum import StrEnum

class AssignmentStatus(StrEnum):
    FULL = "FULL"
    INVALID = "INVALID"
    OPEN = "OPEN"
    PARTIAL = "PARTIAL"

    def __str__(self) -> str:
        return str(self.value)
