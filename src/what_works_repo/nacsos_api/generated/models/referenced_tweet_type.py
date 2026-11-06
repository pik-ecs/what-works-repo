from enum import StrEnum

class ReferencedTweetType(StrEnum):
    QUOTED = "quoted"
    REPLIED_TO = "replied_to"
    RETWEETED = "retweeted"

    def __str__(self) -> str:
        return str(self.value)
