from enum import StrEnum

class UsersFilterMode(StrEnum):
    ALL = "ALL"
    ANY = "ANY"

    def __str__(self) -> str:
        return str(self.value)
