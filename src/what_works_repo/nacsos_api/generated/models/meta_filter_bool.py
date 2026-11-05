from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="MetaFilterBool")



@_attrs_define
class MetaFilterBool:
    """ 
        Attributes:
            field (str):
            value (bool):
            filter_ (Literal['meta_bool'] | Unset):  Default: 'meta_bool'.
            value_type (Literal['bool'] | Unset):  Default: 'bool'.
            comp (Literal['='] | Unset):  Default: '='.
     """

    field: str
    value: bool
    filter_: Literal['meta_bool'] | Unset = 'meta_bool'
    value_type: Literal['bool'] | Unset = 'bool'
    comp: Literal['='] | Unset = '='
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field = self.field

        value = self.value

        filter_ = self.filter_

        value_type = self.value_type

        comp = self.comp


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field": field,
            "value": value,
        })
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if value_type is not UNSET:
            field_dict["value_type"] = value_type
        if comp is not UNSET:
            field_dict["comp"] = comp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        value = d.pop("value")

        filter_ = cast(Literal['meta_bool'] | Unset , d.pop("filter", UNSET))
        if filter_ != 'meta_bool'and not isinstance(filter_, Unset):
            raise ValueError(f"filter must match const 'meta_bool', got '{filter_}'")

        value_type = cast(Literal['bool'] | Unset , d.pop("value_type", UNSET))
        if value_type != 'bool'and not isinstance(value_type, Unset):
            raise ValueError(f"value_type must match const 'bool', got '{value_type}'")

        comp = cast(Literal['='] | Unset , d.pop("comp", UNSET))
        if comp != '='and not isinstance(comp, Unset):
            raise ValueError(f"comp must match const '=', got '{comp}'")

        meta_filter_bool = cls(
            field=field,
            value=value,
            filter_=filter_,
            value_type=value_type,
            comp=comp,
        )


        meta_filter_bool.additional_properties = d
        return meta_filter_bool

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
