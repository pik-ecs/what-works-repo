from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ScopeInfo")



@_attrs_define
class ScopeInfo:
    """ 
        Attributes:
            scope_id (str):
            scope_name (str):
            scheme_id (str):
            scheme_name (str):
     """

    scope_id: str
    scope_name: str
    scheme_id: str
    scheme_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        scope_id = self.scope_id

        scope_name = self.scope_name

        scheme_id = self.scheme_id

        scheme_name = self.scheme_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "scope_id": scope_id,
            "scope_name": scope_name,
            "scheme_id": scheme_id,
            "scheme_name": scheme_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scope_id = d.pop("scope_id")

        scope_name = d.pop("scope_name")

        scheme_id = d.pop("scheme_id")

        scheme_name = d.pop("scheme_name")

        scope_info = cls(
            scope_id=scope_id,
            scope_name=scope_name,
            scheme_id=scheme_id,
            scheme_name=scheme_name,
        )


        scope_info.additional_properties = d
        return scope_info

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
