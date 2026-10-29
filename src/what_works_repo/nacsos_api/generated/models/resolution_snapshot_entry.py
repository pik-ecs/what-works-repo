from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ResolutionSnapshotEntry")



@_attrs_define
class ResolutionSnapshotEntry:
    """ 
        Attributes:
            order_key (str):
            path_key (str):
            ba_id (str):
     """

    order_key: str
    path_key: str
    ba_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_key = self.order_key

        path_key = self.path_key

        ba_id = self.ba_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_key": order_key,
            "path_key": path_key,
            "ba_id": ba_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_key = d.pop("order_key")

        path_key = d.pop("path_key")

        ba_id = d.pop("ba_id")

        resolution_snapshot_entry = cls(
            order_key=order_key,
            path_key=path_key,
            ba_id=ba_id,
        )


        resolution_snapshot_entry.additional_properties = d
        return resolution_snapshot_entry

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
