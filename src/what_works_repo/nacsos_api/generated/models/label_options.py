from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="LabelOptions")



@_attrs_define
class LabelOptions:
    """ 
        Attributes:
            key (str):
            options_int (list[int] | None | Unset):
            options_bool (list[bool] | None | Unset):
            options_multi (list[int] | None | Unset):
            strings (bool | None | Unset):
     """

    key: str
    options_int: list[int] | None | Unset = UNSET
    options_bool: list[bool] | None | Unset = UNSET
    options_multi: list[int] | None | Unset = UNSET
    strings: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        options_int: list[int] | None | Unset
        if isinstance(self.options_int, Unset):
            options_int = UNSET
        elif isinstance(self.options_int, list):
            options_int = self.options_int


        else:
            options_int = self.options_int

        options_bool: list[bool] | None | Unset
        if isinstance(self.options_bool, Unset):
            options_bool = UNSET
        elif isinstance(self.options_bool, list):
            options_bool = self.options_bool


        else:
            options_bool = self.options_bool

        options_multi: list[int] | None | Unset
        if isinstance(self.options_multi, Unset):
            options_multi = UNSET
        elif isinstance(self.options_multi, list):
            options_multi = self.options_multi


        else:
            options_multi = self.options_multi

        strings: bool | None | Unset
        if isinstance(self.strings, Unset):
            strings = UNSET
        else:
            strings = self.strings


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
        })
        if options_int is not UNSET:
            field_dict["options_int"] = options_int
        if options_bool is not UNSET:
            field_dict["options_bool"] = options_bool
        if options_multi is not UNSET:
            field_dict["options_multi"] = options_multi
        if strings is not UNSET:
            field_dict["strings"] = strings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        def _parse_options_int(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_int_type_0 = cast(list[int], data)

                return options_int_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        options_int = _parse_options_int(d.pop("options_int", UNSET))


        def _parse_options_bool(data: object) -> list[bool] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_bool_type_0 = cast(list[bool], data)

                return options_bool_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[bool] | None | Unset, data)

        options_bool = _parse_options_bool(d.pop("options_bool", UNSET))


        def _parse_options_multi(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_multi_type_0 = cast(list[int], data)

                return options_multi_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        options_multi = _parse_options_multi(d.pop("options_multi", UNSET))


        def _parse_strings(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        strings = _parse_strings(d.pop("strings", UNSET))


        label_options = cls(
            key=key,
            options_int=options_int,
            options_bool=options_bool,
            options_multi=options_multi,
            strings=strings,
        )


        label_options.additional_properties = d
        return label_options

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
