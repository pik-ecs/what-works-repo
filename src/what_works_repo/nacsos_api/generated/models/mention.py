from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="Mention")



@_attrs_define
class Mention:
    """ 
        Attributes:
            start (int):
            end (int):
            username (str):
            user_id (int | str):
     """

    start: int
    end: int
    username: str
    user_id: int | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        username = self.username

        user_id: int | str
        user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "start": start,
            "end": end,
            "username": username,
            "user_id": user_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        username = d.pop("username")

        def _parse_user_id(data: object) -> int | str:
            return cast(int | str, data)

        user_id = _parse_user_id(d.pop("user_id"))


        mention = cls(
            start=start,
            end=end,
            username=username,
            user_id=user_id,
        )


        mention.additional_properties = d
        return mention

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
