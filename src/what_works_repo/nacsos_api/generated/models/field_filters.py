from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.field_filters_field import FieldFiltersField
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="FieldFilters")



@_attrs_define
class FieldFilters:
    """ 
        Attributes:
            field (FieldFiltersField):
            values (list[str]):
            filter_ (Literal['field_mul'] | Unset):  Default: 'field_mul'.
     """

    field: FieldFiltersField
    values: list[str]
    filter_: Literal['field_mul'] | Unset = 'field_mul'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field = self.field.value

        values = self.values



        filter_ = self.filter_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field": field,
            "values": values,
        })
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = FieldFiltersField(d.pop("field"))




        values = cast(list[str], d.pop("values"))


        filter_ = cast(Literal['field_mul'] | Unset , d.pop("filter", UNSET))
        if filter_ != 'field_mul'and not isinstance(filter_, Unset):
            raise ValueError(f"filter must match const 'field_mul', got '{filter_}'")

        field_filters = cls(
            field=field,
            values=values,
            filter_=filter_,
        )


        field_filters.additional_properties = d
        return field_filters

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
