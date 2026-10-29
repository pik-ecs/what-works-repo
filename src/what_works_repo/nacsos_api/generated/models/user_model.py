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






T = TypeVar("T", bound="UserModel")



@_attrs_define
class UserModel:
    """ 
        Attributes:
            user_id (None | str | Unset | UUID):
            username (None | str | Unset):
            full_name (None | str | Unset):
            email (None | str | Unset):
            affiliation (None | str | Unset):
            is_superuser (bool | None | Unset):  Default: False.
            is_active (bool | None | Unset):  Default: True.
            setting_newsletter (bool | None | Unset):  Default: False.
            time_created (datetime.datetime | None | Unset):
            time_updated (datetime.datetime | None | Unset):
     """

    user_id: None | str | Unset | UUID = UNSET
    username: None | str | Unset = UNSET
    full_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    affiliation: None | str | Unset = UNSET
    is_superuser: bool | None | Unset = False
    is_active: bool | None | Unset = True
    setting_newsletter: bool | None | Unset = False
    time_created: datetime.datetime | None | Unset = UNSET
    time_updated: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        affiliation: None | str | Unset
        if isinstance(self.affiliation, Unset):
            affiliation = UNSET
        else:
            affiliation = self.affiliation

        is_superuser: bool | None | Unset
        if isinstance(self.is_superuser, Unset):
            is_superuser = UNSET
        else:
            is_superuser = self.is_superuser

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        setting_newsletter: bool | None | Unset
        if isinstance(self.setting_newsletter, Unset):
            setting_newsletter = UNSET
        else:
            setting_newsletter = self.setting_newsletter

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if username is not UNSET:
            field_dict["username"] = username
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if email is not UNSET:
            field_dict["email"] = email
        if affiliation is not UNSET:
            field_dict["affiliation"] = affiliation
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if setting_newsletter is not UNSET:
            field_dict["setting_newsletter"] = setting_newsletter
        if time_created is not UNSET:
            field_dict["time_created"] = time_created
        if time_updated is not UNSET:
            field_dict["time_updated"] = time_updated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_user_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_1 = UUID(data)



                return user_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))


        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_affiliation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        affiliation = _parse_affiliation(d.pop("affiliation", UNSET))


        def _parse_is_superuser(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_superuser = _parse_is_superuser(d.pop("is_superuser", UNSET))


        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))


        def _parse_setting_newsletter(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        setting_newsletter = _parse_setting_newsletter(d.pop("setting_newsletter", UNSET))


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


        user_model = cls(
            user_id=user_id,
            username=username,
            full_name=full_name,
            email=email,
            affiliation=affiliation,
            is_superuser=is_superuser,
            is_active=is_active,
            setting_newsletter=setting_newsletter,
            time_created=time_created,
            time_updated=time_updated,
        )


        user_model.additional_properties = d
        return user_model

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
