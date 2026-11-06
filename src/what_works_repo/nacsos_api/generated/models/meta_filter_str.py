from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="MetaFilterStr")



@_attrs_define
class MetaFilterStr:
    """ 
        Attributes:
            field (str):
            value (str):
            filter_ (Literal['meta_str'] | Unset):  Default: 'meta_str'.
            value_type (Literal['str'] | Unset):  Default: 'str'.
            comp (Literal['LIKE'] | Unset):  Default: 'LIKE'.
     """

    field: str
    value: str
    filter_: Literal['meta_str'] | Unset = 'meta_str'
    value_type: Literal['str'] | Unset = 'str'
    comp: Literal['LIKE'] | Unset = 'LIKE'
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

        filter_ = cast(Literal['meta_str'] | Unset , d.pop("filter", UNSET))
        if filter_ != 'meta_str'and not isinstance(filter_, Unset):
            raise ValueError(f"filter must match const 'meta_str', got '{filter_}'")

        value_type = cast(Literal['str'] | Unset , d.pop("value_type", UNSET))
        if value_type != 'str'and not isinstance(value_type, Unset):
            raise ValueError(f"value_type must match const 'str', got '{value_type}'")

        comp = cast(Literal['LIKE'] | Unset , d.pop("comp", UNSET))
        if comp != 'LIKE'and not isinstance(comp, Unset):
            raise ValueError(f"comp must match const 'LIKE', got '{comp}'")

        meta_filter_str = cls(
            field=field,
            value=value,
            filter_=filter_,
            value_type=value_type,
            comp=comp,
        )


        meta_filter_str.additional_properties = d
        return meta_filter_str

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
