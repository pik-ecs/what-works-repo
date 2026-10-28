from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ContextAnnotation")



@_attrs_define
class ContextAnnotation:
    """ Flattened and reduced version of the context_annotation object
    https://developer.twitter.com/en/docs/twitter-api/annotations/overview

    NOTE: Under the assumption that we could always recover the `description`
          of the domain and entity, this information is not stored to save space.

        Attributes:
            domain_id (str):
            domain_name (str):
            entity_id (str):
            entity_name (str):
     """

    domain_id: str
    domain_name: str
    entity_id: str
    entity_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        domain_id = self.domain_id

        domain_name = self.domain_name

        entity_id = self.entity_id

        entity_name = self.entity_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "domain_id": domain_id,
            "domain_name": domain_name,
            "entity_id": entity_id,
            "entity_name": entity_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_id = d.pop("domain_id")

        domain_name = d.pop("domain_name")

        entity_id = d.pop("entity_id")

        entity_name = d.pop("entity_name")

        context_annotation = cls(
            domain_id=domain_id,
            domain_name=domain_name,
            entity_id=entity_id,
            entity_name=entity_name,
        )


        context_annotation.additional_properties = d
        return context_annotation

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
