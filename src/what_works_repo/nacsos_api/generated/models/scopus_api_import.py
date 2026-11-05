from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="ScopusAPIImport")



@_attrs_define
class ScopusAPIImport:
    """ 
        Attributes:
            file (str):
            file_date (str):
            query (str):
            date (str):
            kind (Literal['scopus-api'] | Unset):  Default: 'scopus-api'.
     """

    file: str
    file_date: str
    query: str
    date: str
    kind: Literal['scopus-api'] | Unset = 'scopus-api'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file = self.file

        file_date = self.file_date

        query = self.query

        date = self.date

        kind = self.kind


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file": file,
            "file_date": file_date,
            "query": query,
            "date": date,
        })
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = d.pop("file")

        file_date = d.pop("file_date")

        query = d.pop("query")

        date = d.pop("date")

        kind = cast(Literal['scopus-api'] | Unset , d.pop("kind", UNSET))
        if kind != 'scopus-api'and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'scopus-api', got '{kind}'")

        scopus_api_import = cls(
            file=file,
            file_date=file_date,
            query=query,
            date=date,
            kind=kind,
        )


        scopus_api_import.additional_properties = d
        return scopus_api_import

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
