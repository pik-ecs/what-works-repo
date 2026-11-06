from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.assignment_config_legacy import AssignmentConfigLegacy
  from ..models.assignment_config_priority import AssignmentConfigPriority
  from ..models.assignment_config_random import AssignmentConfigRandom





T = TypeVar("T", bound="AssignmentScopeModel")



@_attrs_define
class AssignmentScopeModel:
    """ 
        Attributes:
            annotation_scheme_id (str | UUID):
            name (str):
            assignment_scope_id (None | str | Unset | UUID):
            time_created (datetime.datetime | None | Unset):
            description (None | str | Unset):
            config (AssignmentConfigLegacy | AssignmentConfigPriority | AssignmentConfigRandom | None | Unset):
     """

    annotation_scheme_id: str | UUID
    name: str
    assignment_scope_id: None | str | Unset | UUID = UNSET
    time_created: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    config: AssignmentConfigLegacy | AssignmentConfigPriority | AssignmentConfigRandom | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.assignment_config_legacy import AssignmentConfigLegacy # noqa: PLC0415
        from ..models.assignment_config_priority import AssignmentConfigPriority # noqa: PLC0415
        from ..models.assignment_config_random import AssignmentConfigRandom # noqa: PLC0415
        annotation_scheme_id: str
        if isinstance(self.annotation_scheme_id, UUID):
            annotation_scheme_id = str(self.annotation_scheme_id)
        else:
            annotation_scheme_id = self.annotation_scheme_id

        name = self.name

        assignment_scope_id: None | str | Unset
        if isinstance(self.assignment_scope_id, Unset):
            assignment_scope_id = UNSET
        elif isinstance(self.assignment_scope_id, UUID):
            assignment_scope_id = str(self.assignment_scope_id)
        else:
            assignment_scope_id = self.assignment_scope_id

        time_created: None | str | Unset
        if isinstance(self.time_created, Unset):
            time_created = UNSET
        elif isinstance(self.time_created, datetime.datetime):
            time_created = self.time_created.isoformat()
        else:
            time_created = self.time_created

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, AssignmentConfigRandom):
            config = self.config.to_dict()
        elif isinstance(self.config, AssignmentConfigPriority):
            config = self.config.to_dict()
        elif isinstance(self.config, AssignmentConfigLegacy):
            config = self.config.to_dict()
        else:
            config = self.config


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "annotation_scheme_id": annotation_scheme_id,
            "name": name,
        })
        if assignment_scope_id is not UNSET:
            field_dict["assignment_scope_id"] = assignment_scope_id
        if time_created is not UNSET:
            field_dict["time_created"] = time_created
        if description is not UNSET:
            field_dict["description"] = description
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assignment_config_legacy import AssignmentConfigLegacy # noqa: PLC0415
        from ..models.assignment_config_priority import AssignmentConfigPriority # noqa: PLC0415
        from ..models.assignment_config_random import AssignmentConfigRandom # noqa: PLC0415
        d = dict(src_dict)
        def _parse_annotation_scheme_id(data: object) -> str | UUID:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                annotation_scheme_id_type_1 = UUID(data)



                return annotation_scheme_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | UUID, data)

        annotation_scheme_id = _parse_annotation_scheme_id(d.pop("annotation_scheme_id"))


        name = d.pop("name")

        def _parse_assignment_scope_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignment_scope_id_type_1 = UUID(data)



                return assignment_scope_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        assignment_scope_id = _parse_assignment_scope_id(d.pop("assignment_scope_id", UNSET))


        def _parse_time_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_created_type_0 = datetime.datetime.fromisoformat(data)



                return time_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_created = _parse_time_created(d.pop("time_created", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_config(data: object) -> AssignmentConfigLegacy | AssignmentConfigPriority | AssignmentConfigRandom | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_0 = AssignmentConfigRandom.from_dict(data)



                return config_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_1 = AssignmentConfigPriority.from_dict(data)



                return config_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_2 = AssignmentConfigLegacy.from_dict(data)



                return config_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssignmentConfigLegacy | AssignmentConfigPriority | AssignmentConfigRandom | None | Unset, data)

        config = _parse_config(d.pop("config", UNSET))


        assignment_scope_model = cls(
            annotation_scheme_id=annotation_scheme_id,
            name=name,
            assignment_scope_id=assignment_scope_id,
            time_created=time_created,
            description=description,
            config=config,
        )


        assignment_scope_model.additional_properties = d
        return assignment_scope_model

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
