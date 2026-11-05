from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.bot_kind import BotKind
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.bot_meta_resolve import BotMetaResolve





T = TypeVar("T", bound="BotAnnotationMetaDataModel")



@_attrs_define
class BotAnnotationMetaDataModel:
    """ 
        Attributes:
            name (str):
            kind (BotKind):
            project_id (str | UUID):
            bot_annotation_metadata_id (None | str | Unset | UUID):
            time_created (datetime.datetime | None | Unset):
            time_updated (datetime.datetime | None | Unset):
            assignment_scope_id (None | str | Unset | UUID):
            annotation_scheme_id (None | str | Unset | UUID):
            meta (BotMetaResolve | None | Unset):
     """

    name: str
    kind: BotKind
    project_id: str | UUID
    bot_annotation_metadata_id: None | str | Unset | UUID = UNSET
    time_created: datetime.datetime | None | Unset = UNSET
    time_updated: datetime.datetime | None | Unset = UNSET
    assignment_scope_id: None | str | Unset | UUID = UNSET
    annotation_scheme_id: None | str | Unset | UUID = UNSET
    meta: BotMetaResolve | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_meta_resolve import BotMetaResolve # noqa: PLC0415
        name = self.name

        kind = self.kind.value

        project_id: str
        if isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        bot_annotation_metadata_id: None | str | Unset
        if isinstance(self.bot_annotation_metadata_id, Unset):
            bot_annotation_metadata_id = UNSET
        elif isinstance(self.bot_annotation_metadata_id, UUID):
            bot_annotation_metadata_id = str(self.bot_annotation_metadata_id)
        else:
            bot_annotation_metadata_id = self.bot_annotation_metadata_id

        time_created: None | str | Unset
        if isinstance(self.time_created, Unset):
            time_created = UNSET
        elif isinstance(self.time_created, datetime.datetime):
            time_created = self.time_created.isoformat()
        else:
            time_created = self.time_created

        time_updated: None | str | Unset
        if isinstance(self.time_updated, Unset):
            time_updated = UNSET
        elif isinstance(self.time_updated, datetime.datetime):
            time_updated = self.time_updated.isoformat()
        else:
            time_updated = self.time_updated

        assignment_scope_id: None | str | Unset
        if isinstance(self.assignment_scope_id, Unset):
            assignment_scope_id = UNSET
        elif isinstance(self.assignment_scope_id, UUID):
            assignment_scope_id = str(self.assignment_scope_id)
        else:
            assignment_scope_id = self.assignment_scope_id

        annotation_scheme_id: None | str | Unset
        if isinstance(self.annotation_scheme_id, Unset):
            annotation_scheme_id = UNSET
        elif isinstance(self.annotation_scheme_id, UUID):
            annotation_scheme_id = str(self.annotation_scheme_id)
        else:
            annotation_scheme_id = self.annotation_scheme_id

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, BotMetaResolve):
            meta = self.meta.to_dict()
        else:
            meta = self.meta


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "kind": kind,
            "project_id": project_id,
        })
        if bot_annotation_metadata_id is not UNSET:
            field_dict["bot_annotation_metadata_id"] = bot_annotation_metadata_id
        if time_created is not UNSET:
            field_dict["time_created"] = time_created
        if time_updated is not UNSET:
            field_dict["time_updated"] = time_updated
        if assignment_scope_id is not UNSET:
            field_dict["assignment_scope_id"] = assignment_scope_id
        if annotation_scheme_id is not UNSET:
            field_dict["annotation_scheme_id"] = annotation_scheme_id
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_meta_resolve import BotMetaResolve # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        kind = BotKind(d.pop("kind"))




        def _parse_project_id(data: object) -> str | UUID:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_1 = UUID(data)



                return project_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | UUID, data)

        project_id = _parse_project_id(d.pop("project_id"))


        def _parse_bot_annotation_metadata_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bot_annotation_metadata_id_type_1 = UUID(data)



                return bot_annotation_metadata_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        bot_annotation_metadata_id = _parse_bot_annotation_metadata_id(d.pop("bot_annotation_metadata_id", UNSET))


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


        def _parse_time_updated(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_updated_type_0 = datetime.datetime.fromisoformat(data)



                return time_updated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_updated = _parse_time_updated(d.pop("time_updated", UNSET))


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


        def _parse_annotation_scheme_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                annotation_scheme_id_type_1 = UUID(data)



                return annotation_scheme_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        annotation_scheme_id = _parse_annotation_scheme_id(d.pop("annotation_scheme_id", UNSET))


        def _parse_meta(data: object) -> BotMetaResolve | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = BotMetaResolve.from_dict(data)



                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BotMetaResolve | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))


        bot_annotation_meta_data_model = cls(
            name=name,
            kind=kind,
            project_id=project_id,
            bot_annotation_metadata_id=bot_annotation_metadata_id,
            time_created=time_created,
            time_updated=time_updated,
            assignment_scope_id=assignment_scope_id,
            annotation_scheme_id=annotation_scheme_id,
            meta=meta,
        )


        bot_annotation_meta_data_model.additional_properties = d
        return bot_annotation_meta_data_model

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
