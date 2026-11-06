from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="TwitterUserModel")



@_attrs_define
class TwitterUserModel:
    """ Flattened and reduced representation of a Twitter User Object
    https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user

    NOTE:
        - In the context of a `TwitterItemModel`, the `id` is not set as it can be inferred from `twitter_author_id`
        - `name` is None if `name` == `username` to save space

        Attributes:
            created_at (datetime.datetime):
            username (str):
            verified (bool):
            id (None | str | Unset):
            name (None | str | Unset):
            description (None | str | Unset):
            location (None | str | Unset):
            followers_count (int | None | Unset):
            following_count (int | None | Unset):
            tweet_count (int | None | Unset):
            listed_count (int | None | Unset):
     """

    created_at: datetime.datetime
    username: str
    verified: bool
    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    followers_count: int | None | Unset = UNSET
    following_count: int | None | Unset = UNSET
    tweet_count: int | None | Unset = UNSET
    listed_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        username = self.username

        verified = self.verified

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        followers_count: int | None | Unset
        if isinstance(self.followers_count, Unset):
            followers_count = UNSET
        else:
            followers_count = self.followers_count

        following_count: int | None | Unset
        if isinstance(self.following_count, Unset):
            following_count = UNSET
        else:
            following_count = self.following_count

        tweet_count: int | None | Unset
        if isinstance(self.tweet_count, Unset):
            tweet_count = UNSET
        else:
            tweet_count = self.tweet_count

        listed_count: int | None | Unset
        if isinstance(self.listed_count, Unset):
            listed_count = UNSET
        else:
            listed_count = self.listed_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "username": username,
            "verified": verified,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if followers_count is not UNSET:
            field_dict["followers_count"] = followers_count
        if following_count is not UNSET:
            field_dict["following_count"] = following_count
        if tweet_count is not UNSET:
            field_dict["tweet_count"] = tweet_count
        if listed_count is not UNSET:
            field_dict["listed_count"] = listed_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        username = d.pop("username")

        verified = d.pop("verified")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))


        def _parse_followers_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        followers_count = _parse_followers_count(d.pop("followers_count", UNSET))


        def _parse_following_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        following_count = _parse_following_count(d.pop("following_count", UNSET))


        def _parse_tweet_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tweet_count = _parse_tweet_count(d.pop("tweet_count", UNSET))


        def _parse_listed_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        listed_count = _parse_listed_count(d.pop("listed_count", UNSET))


        twitter_user_model = cls(
            created_at=created_at,
            username=username,
            verified=verified,
            id=id,
            name=name,
            description=description,
            location=location,
            followers_count=followers_count,
            following_count=following_count,
            tweet_count=tweet_count,
            listed_count=listed_count,
        )


        twitter_user_model.additional_properties = d
        return twitter_user_model

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
