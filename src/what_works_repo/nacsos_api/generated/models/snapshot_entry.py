from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SnapshotEntry")



@_attrs_define
class SnapshotEntry:
    """ 
        Attributes:
            order_key (str):
            path_key (str):
            item_id (str):
            anno_id (str):
            user_id (str):
            value_bool (bool | None | Unset):
            value_int (int | None | Unset):
            value_float (float | None | Unset):
            value_str (None | str | Unset):
            multi_int (list[int] | None | Unset):
     """

    order_key: str
    path_key: str
    item_id: str
    anno_id: str
    user_id: str
    value_bool: bool | None | Unset = UNSET
    value_int: int | None | Unset = UNSET
    value_float: float | None | Unset = UNSET
    value_str: None | str | Unset = UNSET
    multi_int: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_key = self.order_key

        path_key = self.path_key

        item_id = self.item_id

        anno_id = self.anno_id

        user_id = self.user_id

        value_bool: bool | None | Unset
        if isinstance(self.value_bool, Unset):
            value_bool = UNSET
        else:
            value_bool = self.value_bool

        value_int: int | None | Unset
        if isinstance(self.value_int, Unset):
            value_int = UNSET
        else:
            value_int = self.value_int

        value_float: float | None | Unset
        if isinstance(self.value_float, Unset):
            value_float = UNSET
        else:
            value_float = self.value_float

        value_str: None | str | Unset
        if isinstance(self.value_str, Unset):
            value_str = UNSET
        else:
            value_str = self.value_str

        multi_int: list[int] | None | Unset
        if isinstance(self.multi_int, Unset):
            multi_int = UNSET
        elif isinstance(self.multi_int, list):
            multi_int = self.multi_int


        else:
            multi_int = self.multi_int


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_key": order_key,
            "path_key": path_key,
            "item_id": item_id,
            "anno_id": anno_id,
            "user_id": user_id,
        })
        if value_bool is not UNSET:
            field_dict["value_bool"] = value_bool
        if value_int is not UNSET:
            field_dict["value_int"] = value_int
        if value_float is not UNSET:
            field_dict["value_float"] = value_float
        if value_str is not UNSET:
            field_dict["value_str"] = value_str
        if multi_int is not UNSET:
            field_dict["multi_int"] = multi_int

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_key = d.pop("order_key")

        path_key = d.pop("path_key")

        item_id = d.pop("item_id")

        anno_id = d.pop("anno_id")

        user_id = d.pop("user_id")

        def _parse_value_bool(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        value_bool = _parse_value_bool(d.pop("value_bool", UNSET))


        def _parse_value_int(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        value_int = _parse_value_int(d.pop("value_int", UNSET))


        def _parse_value_float(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value_float = _parse_value_float(d.pop("value_float", UNSET))


        def _parse_value_str(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_str = _parse_value_str(d.pop("value_str", UNSET))


        def _parse_multi_int(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                multi_int_type_0 = cast(list[int], data)

                return multi_int_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        multi_int = _parse_multi_int(d.pop("multi_int", UNSET))


        snapshot_entry = cls(
            order_key=order_key,
            path_key=path_key,
            item_id=item_id,
            anno_id=anno_id,
            user_id=user_id,
            value_bool=value_bool,
            value_int=value_int,
            value_float=value_float,
            value_str=value_str,
            multi_int=multi_int,
        )


        snapshot_entry.additional_properties = d
        return snapshot_entry

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
