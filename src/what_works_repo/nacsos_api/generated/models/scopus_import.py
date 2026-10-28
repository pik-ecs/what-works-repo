from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="ScopusImport")



@_attrs_define
class ScopusImport:
    """ 
        Attributes:
            sources (list[str]):
            kind (Literal['scopus'] | Unset):  Default: 'scopus'.
     """

    sources: list[str]
    kind: Literal['scopus'] | Unset = 'scopus'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        sources = self.sources



        kind = self.kind


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sources": sources,
        })
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sources = cast(list[str], d.pop("sources"))


        kind = cast(Literal['scopus'] | Unset , d.pop("kind", UNSET))
        if kind != 'scopus'and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'scopus', got '{kind}'")

        scopus_import = cls(
            sources=sources,
            kind=kind,
        )


        scopus_import.additional_properties = d
        return scopus_import

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
