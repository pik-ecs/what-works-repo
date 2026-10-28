from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AssignmentCounts")



@_attrs_define
class AssignmentCounts:
    """ 
        Attributes:
            num_total (int):
            num_open (int):
            num_partial (int):
            num_full (int):
     """

    num_total: int
    num_open: int
    num_partial: int
    num_full: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        num_total = self.num_total

        num_open = self.num_open

        num_partial = self.num_partial

        num_full = self.num_full


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "num_total": num_total,
            "num_open": num_open,
            "num_partial": num_partial,
            "num_full": num_full,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num_total = d.pop("num_total")

        num_open = d.pop("num_open")

        num_partial = d.pop("num_partial")

        num_full = d.pop("num_full")

        assignment_counts = cls(
            num_total=num_total,
            num_open=num_open,
            num_partial=num_partial,
            num_full=num_full,
        )


        assignment_counts.additional_properties = d
        return assignment_counts

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
