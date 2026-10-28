from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="AbstractFilter")



@_attrs_define
class AbstractFilter:
    """ 
        Attributes:
            filter_ (Literal['abstract'] | Unset):  Default: 'abstract'.
            comp (None | str | Unset):
            size (int | None | Unset):
            empty (bool | None | Unset):
     """

    filter_: Literal['abstract'] | Unset = 'abstract'
    comp: None | str | Unset = UNSET
    size: int | None | Unset = UNSET
    empty: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_

        comp: None | str | Unset
        if isinstance(self.comp, Unset):
            comp = UNSET
        else:
            comp = self.comp

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        empty: bool | None | Unset
        if isinstance(self.empty, Unset):
            empty = UNSET
        else:
            empty = self.empty


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if comp is not UNSET:
            field_dict["comp"] = comp
        if size is not UNSET:
            field_dict["size"] = size
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_ = cast(Literal['abstract'] | Unset , d.pop("filter", UNSET))
        if filter_ != 'abstract'and not isinstance(filter_, Unset):
            raise ValueError(f"filter must match const 'abstract', got '{filter_}'")

        def _parse_comp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comp = _parse_comp(d.pop("comp", UNSET))


        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))


        def _parse_empty(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        empty = _parse_empty(d.pop("empty", UNSET))


        abstract_filter = cls(
            filter_=filter_,
            comp=comp,
            size=size,
            empty=empty,
        )


        abstract_filter.additional_properties = d
        return abstract_filter

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
