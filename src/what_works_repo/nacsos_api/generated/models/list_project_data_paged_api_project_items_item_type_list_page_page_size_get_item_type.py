from enum import StrEnum

class ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType(StrEnum):
    ACADEMIC = "academic"
    GENERIC = "generic"
    LEXIS = "lexis"
    PATENTS = "patents"
    TWITTER = "twitter"

    def __str__(self) -> str:
        return str(self.value)
