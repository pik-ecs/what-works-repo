from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AffiliationModel")



@_attrs_define
class AffiliationModel:
    """ 
        Attributes:
            name (str):
            country (None | str | Unset):
            openalex_id (None | str | Unset):
            s2_id (None | str | Unset):
     """

    name: str
    country: None | str | Unset = UNSET
    openalex_id: None | str | Unset = UNSET
    s2_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        openalex_id: None | str | Unset
        if isinstance(self.openalex_id, Unset):
            openalex_id = UNSET
        else:
            openalex_id = self.openalex_id

        s2_id: None | str | Unset
        if isinstance(self.s2_id, Unset):
            s2_id = UNSET
        else:
            s2_id = self.s2_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if country is not UNSET:
            field_dict["country"] = country
        if openalex_id is not UNSET:
            field_dict["openalex_id"] = openalex_id
        if s2_id is not UNSET:
            field_dict["s2_id"] = s2_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))


        def _parse_openalex_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        openalex_id = _parse_openalex_id(d.pop("openalex_id", UNSET))


        def _parse_s2_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s2_id = _parse_s2_id(d.pop("s2_id", UNSET))


        affiliation_model = cls(
            name=name,
            country=country,
            openalex_id=openalex_id,
            s2_id=s2_id,
        )


        affiliation_model.additional_properties = d
        return affiliation_model

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
