from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.assignment_config_legacy_legacy import AssignmentConfigLegacyLegacy





T = TypeVar("T", bound="AssignmentConfigLegacy")



@_attrs_define
class AssignmentConfigLegacy:
    """ 
        Attributes:
            legacy (AssignmentConfigLegacyLegacy):
            config_type (Literal['LEGACY'] | Unset):  Default: 'LEGACY'.
     """

    legacy: AssignmentConfigLegacyLegacy
    config_type: Literal['LEGACY'] | Unset = 'LEGACY'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.assignment_config_legacy_legacy import AssignmentConfigLegacyLegacy # noqa: PLC0415
        legacy = self.legacy.to_dict()

        config_type = self.config_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "legacy": legacy,
        })
        if config_type is not UNSET:
            field_dict["config_type"] = config_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assignment_config_legacy_legacy import AssignmentConfigLegacyLegacy # noqa: PLC0415
        d = dict(src_dict)
        legacy = AssignmentConfigLegacyLegacy.from_dict(d.pop("legacy"))




        config_type = cast(Literal['LEGACY'] | Unset , d.pop("config_type", UNSET))
        if config_type != 'LEGACY'and not isinstance(config_type, Unset):
            raise ValueError(f"config_type must match const 'LEGACY', got '{config_type}'")

        assignment_config_legacy = cls(
            legacy=legacy,
            config_type=config_type,
        )


        assignment_config_legacy.additional_properties = d
        return assignment_config_legacy

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
