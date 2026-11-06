from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.label_filter_bool_type import LabelFilterBoolType
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.users_filter import UsersFilter





T = TypeVar("T", bound="LabelFilterBool")



@_attrs_define
class LabelFilterBool:
    """ 
        Attributes:
            key (str):
            type_ (LabelFilterBoolType):
            scopes (list[str] | None | Unset):
            scheme (None | str | Unset):
            users (None | Unset | UsersFilter):
            repeats (list[int] | None | Unset):
            filter_ (Literal['label_bool'] | Unset):  Default: 'label_bool'.
            value_type (Literal['bool'] | Unset):  Default: 'bool'.
            comp (Literal['='] | Unset):  Default: '='.
            value_bool (bool | None | Unset):
     """

    key: str
    type_: LabelFilterBoolType
    scopes: list[str] | None | Unset = UNSET
    scheme: None | str | Unset = UNSET
    users: None | Unset | UsersFilter = UNSET
    repeats: list[int] | None | Unset = UNSET
    filter_: Literal['label_bool'] | Unset = 'label_bool'
    value_type: Literal['bool'] | Unset = 'bool'
    comp: Literal['='] | Unset = '='
    value_bool: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.users_filter import UsersFilter # noqa: PLC0415
        key = self.key

        type_ = self.type_.value

        scopes: list[str] | None | Unset
        if isinstance(self.scopes, Unset):
            scopes = UNSET
        elif isinstance(self.scopes, list):
            scopes = self.scopes


        else:
            scopes = self.scopes

        scheme: None | str | Unset
        if isinstance(self.scheme, Unset):
            scheme = UNSET
        else:
            scheme = self.scheme

        users: dict[str, Any] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, UsersFilter):
            users = self.users.to_dict()
        else:
            users = self.users

        repeats: list[int] | None | Unset
        if isinstance(self.repeats, Unset):
            repeats = UNSET
        elif isinstance(self.repeats, list):
            repeats = self.repeats


        else:
            repeats = self.repeats

        filter_ = self.filter_

        value_type = self.value_type

        comp = self.comp

        value_bool: bool | None | Unset
        if isinstance(self.value_bool, Unset):
            value_bool = UNSET
        else:
            value_bool = self.value_bool


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "type": type_,
        })
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if users is not UNSET:
            field_dict["users"] = users
        if repeats is not UNSET:
            field_dict["repeats"] = repeats
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if value_type is not UNSET:
            field_dict["value_type"] = value_type
        if comp is not UNSET:
            field_dict["comp"] = comp
        if value_bool is not UNSET:
            field_dict["value_bool"] = value_bool

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.users_filter import UsersFilter # noqa: PLC0415
        d = dict(src_dict)
        key = d.pop("key")

        type_ = LabelFilterBoolType(d.pop("type"))




        def _parse_scopes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = cast(list[str], data)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scopes = _parse_scopes(d.pop("scopes", UNSET))


        def _parse_scheme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheme = _parse_scheme(d.pop("scheme", UNSET))


        def _parse_users(data: object) -> None | Unset | UsersFilter:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                users_type_0 = UsersFilter.from_dict(data)



                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UsersFilter, data)

        users = _parse_users(d.pop("users", UNSET))


        def _parse_repeats(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                repeats_type_0 = cast(list[int], data)

                return repeats_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        repeats = _parse_repeats(d.pop("repeats", UNSET))


        filter_ = cast(Literal['label_bool'] | Unset , d.pop("filter", UNSET))
        if filter_ != 'label_bool'and not isinstance(filter_, Unset):
            raise ValueError(f"filter must match const 'label_bool', got '{filter_}'")

        value_type = cast(Literal['bool'] | Unset , d.pop("value_type", UNSET))
        if value_type != 'bool'and not isinstance(value_type, Unset):
            raise ValueError(f"value_type must match const 'bool', got '{value_type}'")

        comp = cast(Literal['='] | Unset , d.pop("comp", UNSET))
        if comp != '='and not isinstance(comp, Unset):
            raise ValueError(f"comp must match const '=', got '{comp}'")

        def _parse_value_bool(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        value_bool = _parse_value_bool(d.pop("value_bool", UNSET))


        label_filter_bool = cls(
            key=key,
            type_=type_,
            scopes=scopes,
            scheme=scheme,
            users=users,
            repeats=repeats,
            filter_=filter_,
            value_type=value_type,
            comp=comp,
            value_bool=value_bool,
        )


        label_filter_bool.additional_properties = d
        return label_filter_bool

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
