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
  from ..models.generic_item_model_meta import GenericItemModelMeta





T = TypeVar("T", bound="GenericItemModel")



@_attrs_define
class GenericItemModel:
    """ Corresponds to db.models.items.generic.GenericItem

        Attributes:
            meta (GenericItemModelMeta):
            item_id (None | str | Unset | UUID):
            project_id (None | str | Unset | UUID):
            type_ (ItemType | Unset):
            time_edited (datetime.datetime | None | Unset):
            text (None | str | Unset):
     """

    meta: GenericItemModelMeta
    item_id: None | str | Unset | UUID = UNSET
    project_id: None | str | Unset | UUID = UNSET
    type_: ItemType | Unset = UNSET
    time_edited: datetime.datetime | None | Unset = UNSET
    text: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.generic_item_model_meta import GenericItemModelMeta # noqa: PLC0415
        meta = self.meta.to_dict()

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "meta": meta,
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generic_item_model_meta import GenericItemModelMeta # noqa: PLC0415
        d = dict(src_dict)
        meta = GenericItemModelMeta.from_dict(d.pop("meta"))




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


        generic_item_model = cls(
            meta=meta,
            item_id=item_id,
            project_id=project_id,
            type_=type_,
            time_edited=time_edited,
            text=text,
        )


        generic_item_model.additional_properties = d
        return generic_item_model

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
