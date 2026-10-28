from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.referenced_tweet_type import ReferencedTweetType
from typing import cast






T = TypeVar("T", bound="ReferencedTweet")



@_attrs_define
class ReferencedTweet:
    """ 
        Attributes:
            id (int | str):
            type_ (ReferencedTweetType):
     """

    id: int | str
    type_: ReferencedTweetType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: int | str
        id = self.id

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_id(data: object) -> int | str:
            return cast(int | str, data)

        id = _parse_id(d.pop("id"))


        type_ = ReferencedTweetType(d.pop("type"))




        referenced_tweet = cls(
            id=id,
            type_=type_,
        )


        referenced_tweet.additional_properties = d
        return referenced_tweet

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
