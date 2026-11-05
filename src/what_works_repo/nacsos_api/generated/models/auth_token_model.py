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






T = TypeVar("T", bound="AuthTokenModel")



@_attrs_define
class AuthTokenModel:
    """ 
        Attributes:
            token_id (str | UUID):
            username (str):
            time_created (datetime.datetime | None | Unset):
            time_updated (datetime.datetime | None | Unset):
            valid_till (datetime.datetime | None | Unset):
     """

    token_id: str | UUID
    username: str
    time_created: datetime.datetime | None | Unset = UNSET
    time_updated: datetime.datetime | None | Unset = UNSET
    valid_till: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        token_id: str
        if isinstance(self.token_id, UUID):
            token_id = str(self.token_id)
        else:
            token_id = self.token_id

        username = self.username

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

        valid_till: None | str | Unset
        if isinstance(self.valid_till, Unset):
            valid_till = UNSET
        elif isinstance(self.valid_till, datetime.datetime):
            valid_till = self.valid_till.isoformat()
        else:
            valid_till = self.valid_till


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "token_id": token_id,
            "username": username,
        })
        if time_created is not UNSET:
            field_dict["time_created"] = time_created
        if time_updated is not UNSET:
            field_dict["time_updated"] = time_updated
        if valid_till is not UNSET:
            field_dict["valid_till"] = valid_till

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_token_id(data: object) -> str | UUID:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                token_id_type_1 = UUID(data)



                return token_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | UUID, data)

        token_id = _parse_token_id(d.pop("token_id"))


        username = d.pop("username")

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


        def _parse_valid_till(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_till_type_0 = datetime.datetime.fromisoformat(data)



                return valid_till_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        valid_till = _parse_valid_till(d.pop("valid_till", UNSET))


        auth_token_model = cls(
            token_id=token_id,
            username=username,
            time_created=time_created,
            time_updated=time_updated,
            valid_till=valid_till,
        )


        auth_token_model.additional_properties = d
        return auth_token_model

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
