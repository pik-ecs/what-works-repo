from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.users_filter_mode import UsersFilterMode
from typing import cast






T = TypeVar("T", bound="UsersFilter")



@_attrs_define
class UsersFilter:
    """ 
        Attributes:
            user_ids (list[str]):
            mode (UsersFilterMode):
     """

    user_ids: list[str]
    mode: UsersFilterMode
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_ids = self.user_ids



        mode = self.mode.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user_ids": user_ids,
            "mode": mode,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_ids = cast(list[str], d.pop("user_ids"))


        mode = UsersFilterMode(d.pop("mode"))




        users_filter = cls(
            user_ids=user_ids,
            mode=mode,
        )


        users_filter.additional_properties = d
        return users_filter

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
