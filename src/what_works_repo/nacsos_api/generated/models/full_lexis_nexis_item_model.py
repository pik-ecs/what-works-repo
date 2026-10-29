from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.item_type import ItemType
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.lexis_nexis_item_source_model import LexisNexisItemSourceModel





T = TypeVar("T", bound="FullLexisNexisItemModel")



@_attrs_define
class FullLexisNexisItemModel:
    """ 
        Attributes:
            item_id (None | str | Unset | UUID):
            project_id (None | str | Unset | UUID):
            type_ (ItemType | Unset):
            time_edited (datetime.datetime | None | Unset):
            text (None | str | Unset):
            teaser (None | str | Unset):
            authors (list[str] | None | Unset):
            sources (list[LexisNexisItemSourceModel] | None | Unset):
     """

    item_id: None | str | Unset | UUID = UNSET
    project_id: None | str | Unset | UUID = UNSET
    type_: ItemType | Unset = UNSET
    time_edited: datetime.datetime | None | Unset = UNSET
    text: None | str | Unset = UNSET
    teaser: None | str | Unset = UNSET
    authors: list[str] | None | Unset = UNSET
    sources: list[LexisNexisItemSourceModel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.lexis_nexis_item_source_model import LexisNexisItemSourceModel # noqa: PLC0415
        item_id: None | str | Unset
        if isinstance(self.item_id, Unset):
            item_id = UNSET
        elif isinstance(self.item_id, UUID):
            item_id = str(self.item_id)
        else:
            item_id = self.item_id

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        time_edited: None | str | Unset
        if isinstance(self.time_edited, Unset):
            time_edited = UNSET
        elif isinstance(self.time_edited, datetime.datetime):
            time_edited = self.time_edited.isoformat()
        else:
            time_edited = self.time_edited

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        teaser: None | str | Unset
        if isinstance(self.teaser, Unset):
            teaser = UNSET
        else:
            teaser = self.teaser

        authors: list[str] | None | Unset
        if isinstance(self.authors, Unset):
            authors = UNSET
        elif isinstance(self.authors, list):
            authors = self.authors


        else:
            authors = self.authors

        sources: list[dict[str, Any]] | None | Unset
        if isinstance(self.sources, Unset):
            sources = UNSET
        elif isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)


        else:
            sources = self.sources


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if time_edited is not UNSET:
            field_dict["time_edited"] = time_edited
        if text is not UNSET:
            field_dict["text"] = text
        if teaser is not UNSET:
            field_dict["teaser"] = teaser
        if authors is not UNSET:
            field_dict["authors"] = authors
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lexis_nexis_item_source_model import LexisNexisItemSourceModel # noqa: PLC0415
        d = dict(src_dict)
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


        def _parse_project_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_1 = UUID(data)



                return project_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))


        _type_ = d.pop("type", UNSET)
        type_: ItemType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = ItemType(_type_)




        def _parse_time_edited(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_edited_type_0 = datetime.datetime.fromisoformat(data)



                return time_edited_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_edited = _parse_time_edited(d.pop("time_edited", UNSET))


        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))


        def _parse_teaser(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        teaser = _parse_teaser(d.pop("teaser", UNSET))


        def _parse_authors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                authors_type_0 = cast(list[str], data)

                return authors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        authors = _parse_authors(d.pop("authors", UNSET))


        def _parse_sources(data: object) -> list[LexisNexisItemSourceModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in (_sources_type_0):
                    sources_type_0_item = LexisNexisItemSourceModel.from_dict(sources_type_0_item_data)



                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LexisNexisItemSourceModel] | None | Unset, data)

        sources = _parse_sources(d.pop("sources", UNSET))


        full_lexis_nexis_item_model = cls(
            item_id=item_id,
            project_id=project_id,
            type_=type_,
            time_edited=time_edited,
            text=text,
            teaser=teaser,
            authors=authors,
            sources=sources,
        )


        full_lexis_nexis_item_model.additional_properties = d
        return full_lexis_nexis_item_model

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
