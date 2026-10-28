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
  from ..models.lexis_nexis_item_source_model_meta_type_0 import LexisNexisItemSourceModelMetaType0





T = TypeVar("T", bound="LexisNexisItemSourceModel")



@_attrs_define
class LexisNexisItemSourceModel:
    """ 
        Attributes:
            lexis_id (str):
            item_source_id (None | str | Unset | UUID):
            item_id (None | str | Unset | UUID):
            name (None | str | Unset):
            title (None | str | Unset):
            section (None | str | Unset):
            jurisdiction (None | str | Unset):
            location (None | str | Unset):
            content_type (None | str | Unset):
            published_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            meta (LexisNexisItemSourceModelMetaType0 | None | Unset):
     """

    lexis_id: str
    item_source_id: None | str | Unset | UUID = UNSET
    item_id: None | str | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    section: None | str | Unset = UNSET
    jurisdiction: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    content_type: None | str | Unset = UNSET
    published_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    meta: LexisNexisItemSourceModelMetaType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lexis_nexis_item_source_model_meta_type_0 import LexisNexisItemSourceModelMetaType0 # noqa: PLC0415
        lexis_id = self.lexis_id

        item_source_id: None | str | Unset
        if isinstance(self.item_source_id, Unset):
            item_source_id = UNSET
        elif isinstance(self.item_source_id, UUID):
            item_source_id = str(self.item_source_id)
        else:
            item_source_id = self.item_source_id

        item_id: None | str | Unset
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        elif isinstance(self.item_id, UUID):
            item_id = str(self.item_id)
        else:
            item_id = self.item_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        section: None | str | Unset
        if isinstance(self.section, Unset):
            section = UNSET
        else:
            section = self.section

        jurisdiction: None | str | Unset
        if isinstance(self.jurisdiction, Unset):
            jurisdiction = UNSET
        else:
            jurisdiction = self.jurisdiction

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, LexisNexisItemSourceModelMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "lexis_id": lexis_id,
        })
        if item_source_id is not UNSET:
            field_dict["item_source_id"] = item_source_id
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if name is not UNSET:
            field_dict["name"] = name
        if title is not UNSET:
            field_dict["title"] = title
        if section is not UNSET:
            field_dict["section"] = section
        if jurisdiction is not UNSET:
            field_dict["jurisdiction"] = jurisdiction
        if location is not UNSET:
            field_dict["location"] = location
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lexis_nexis_item_source_model_meta_type_0 import LexisNexisItemSourceModelMetaType0 # noqa: PLC0415
        d = dict(src_dict)
        lexis_id = d.pop("lexis_id")

        def _parse_item_source_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                item_source_id_type_1 = UUID(data)



                return item_source_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        item_source_id = _parse_item_source_id(d.pop("item_source_id", UNSET))


        def _parse_item_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                item_id_type_1 = UUID(data)



                return item_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        item_id = _parse_item_id(d.pop("item_id", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_section(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section = _parse_section(d.pop("section", UNSET))


        def _parse_jurisdiction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jurisdiction = _parse_jurisdiction(d.pop("jurisdiction", UNSET))


        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))


        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("content_type", UNSET))


        def _parse_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)



                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_at = _parse_published_at(d.pop("published_at", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))


        def _parse_meta(data: object) -> LexisNexisItemSourceModelMetaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = LexisNexisItemSourceModelMetaType0.from_dict(data)



                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LexisNexisItemSourceModelMetaType0 | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))


        lexis_nexis_item_source_model = cls(
            lexis_id=lexis_id,
            item_source_id=item_source_id,
            item_id=item_id,
            name=name,
            title=title,
            section=section,
            jurisdiction=jurisdiction,
            location=location,
            content_type=content_type,
            published_at=published_at,
            updated_at=updated_at,
            meta=meta,
        )


        lexis_nexis_item_source_model.additional_properties = d
        return lexis_nexis_item_source_model

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
