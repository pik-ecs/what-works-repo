from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.label_filter_multi_type import LabelFilterMultiType
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.users_filter import UsersFilter





T = TypeVar("T", bound="LabelFilterMulti")



@_attrs_define
class LabelFilterMulti:
    """ 
        Attributes:
            key (str):
            type_ (LabelFilterMultiType):
            comp (str):
            scopes (list[str] | None | Unset):
            scheme (None | str | Unset):
            users (None | Unset | UsersFilter):
            repeats (list[int] | None | Unset):
            filter_ (Literal['label_multi'] | Unset):  Default: 'label_multi'.
            value_type (Literal['multi'] | Unset):  Default: 'multi'.
            multi_int (list[int] | None | Unset):
     """

    key: str
    type_: LabelFilterMultiType
    comp: str
    scopes: list[str] | None | Unset = UNSET
    scheme: None | str | Unset = UNSET
    users: None | Unset | UsersFilter = UNSET
    repeats: list[int] | None | Unset = UNSET
    filter_: Literal['label_multi'] | Unset = 'label_multi'
    value_type: Literal['multi'] | Unset = 'multi'
    multi_int: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.users_filter import UsersFilter # noqa: PLC0415
        key = self.key

        type_ = self.type_.value

        comp = self.comp

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

        multi_int: list[int] | None | Unset
        if isinstance(self.multi_int, Unset):
            multi_int = UNSET
        elif isinstance(self.multi_int, list):
            multi_int = self.multi_int


        else:
            multi_int = self.multi_int


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "type": type_,
            "comp": comp,
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
        if multi_int is not UNSET:
            field_dict["multi_int"] = multi_int

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.users_filter import UsersFilter # noqa: PLC0415
        d = dict(src_dict)
        key = d.pop("key")

        type_ = LabelFilterMultiType(d.pop("type"))




        comp = d.pop("comp")

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


        filter_ = cast(Literal['label_multi'] | Unset , d.pop("filter", UNSET))
        if filter_ != 'label_multi'and not isinstance(filter_, Unset):
            raise ValueError(f"filter must match const 'label_multi', got '{filter_}'")

        value_type = cast(Literal['multi'] | Unset , d.pop("value_type", UNSET))
        if value_type != 'multi'and not isinstance(value_type, Unset):
            raise ValueError(f"value_type must match const 'multi', got '{value_type}'")

        def _parse_multi_int(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                multi_int_type_0 = cast(list[int], data)

                return multi_int_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        multi_int = _parse_multi_int(d.pop("multi_int", UNSET))


        label_filter_multi = cls(
            key=key,
            type_=type_,
            comp=comp,
            scopes=scopes,
            scheme=scheme,
            users=users,
            repeats=repeats,
            filter_=filter_,
            value_type=value_type,
            multi_int=multi_int,
        )


        label_filter_multi.additional_properties = d
        return label_filter_multi

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
