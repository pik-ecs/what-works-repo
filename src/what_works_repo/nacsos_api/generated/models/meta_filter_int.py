from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="MetaFilterInt")



@_attrs_define
class MetaFilterInt:
    """ 
        Attributes:
            field (str):
            comp (str):
            value (int):
            filter_ (Literal['meta_int'] | Unset):  Default: 'meta_int'.
            value_type (Literal['int'] | Unset):  Default: 'int'.
     """

    field: str
    comp: str
    value: int
    filter_: Literal['meta_int'] | Unset = 'meta_int'
    value_type: Literal['int'] | Unset = 'int'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field = self.field

        comp = self.comp

        value = self.value

        filter_ = self.filter_

        value_type = self.value_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field": field,
            "comp": comp,
            "value": value,
        })
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if value_type is not UNSET:
            field_dict["value_type"] = value_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        comp = d.pop("comp")

        value = d.pop("value")

        filter_ = cast(Literal['meta_int'] | Unset , d.pop("filter", UNSET))
        if filter_ != 'meta_int'and not isinstance(filter_, Unset):
            raise ValueError(f"filter must match const 'meta_int', got '{filter_}'")

        value_type = cast(Literal['int'] | Unset , d.pop("value_type", UNSET))
        if value_type != 'int'and not isinstance(value_type, Unset):
            raise ValueError(f"value_type must match const 'int', got '{value_type}'")

        meta_filter_int = cls(
            field=field,
            comp=comp,
            value=value,
            filter_=filter_,
            value_type=value_type,
        )


        meta_filter_int.additional_properties = d
        return meta_filter_int

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
