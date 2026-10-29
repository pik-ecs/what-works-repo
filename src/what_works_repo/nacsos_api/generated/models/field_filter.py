from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.field_filter_field import FieldFilterField
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="FieldFilter")



@_attrs_define
class FieldFilter:
    """ 
        Attributes:
            field (FieldFilterField):
            value (int | str):
            filter_ (Literal['field'] | Unset):  Default: 'field'.
            comp (None | str | Unset):
     """

    field: FieldFilterField
    value: int | str
    filter_: Literal['field'] | Unset = 'field'
    comp: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field = self.field.value

        value: int | str
        value = self.value

        filter_ = self.filter_

        comp: None | str | Unset
        if isinstance(self.comp, Unset):
            comp = UNSET
        else:
            comp = self.comp


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field": field,
            "value": value,
        })
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if comp is not UNSET:
            field_dict["comp"] = comp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = FieldFilterField(d.pop("field"))




        def _parse_value(data: object) -> int | str:
            return cast(int | str, data)

        value = _parse_value(d.pop("value"))


        filter_ = cast(Literal['field'] | Unset , d.pop("filter", UNSET))
        if filter_ != 'field'and not isinstance(filter_, Unset):
            raise ValueError(f"filter must match const 'field', got '{filter_}'")

        def _parse_comp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comp = _parse_comp(d.pop("comp", UNSET))


        field_filter = cls(
            field=field,
            value=value,
            filter_=filter_,
            comp=comp,
        )


        field_filter.additional_properties = d
        return field_filter

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
