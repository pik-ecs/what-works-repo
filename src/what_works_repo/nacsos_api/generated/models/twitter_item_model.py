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
  from ..models.cashtag import Cashtag
  from ..models.context_annotation import ContextAnnotation
  from ..models.hashtag import Hashtag
  from ..models.mention import Mention
  from ..models.referenced_tweet import ReferencedTweet
  from ..models.twitter_user_model import TwitterUserModel
  from ..models.url import URL





T = TypeVar("T", bound="TwitterItemModel")



@_attrs_define
class TwitterItemModel:
    """ Corresponds to db.models.items.TwitterItem

    For more in-depth documentation, please refer to:
    https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet

        Attributes:
            created_at (datetime.datetime):
            retweet_count (int):
            reply_count (int):
            like_count (int):
            quote_count (int):
            item_id (None | str | Unset | UUID):
            project_id (None | str | Unset | UUID):
            type_ (ItemType | Unset):
            time_edited (datetime.datetime | None | Unset):
            text (None | str | Unset):
            twitter_id (None | str | Unset):
            twitter_author_id (None | str | Unset):
            language (None | str | Unset):
            conversation_id (None | str | Unset):
            referenced_tweets (list[ReferencedTweet] | None | Unset):
            latitude (float | None | Unset):
            longitude (float | None | Unset):
            hashtags (list[Hashtag] | None | Unset):
            mentions (list[Mention] | None | Unset):
            urls (list[URL] | None | Unset):
            cashtags (list[Cashtag] | None | Unset):
            context_annotations (list[ContextAnnotation] | None | Unset):
            user (None | TwitterUserModel | Unset):
     """

    created_at: datetime.datetime
    retweet_count: int
    reply_count: int
    like_count: int
    quote_count: int
    item_id: None | str | Unset | UUID = UNSET
    project_id: None | str | Unset | UUID = UNSET
    type_: ItemType | Unset = UNSET
    time_edited: datetime.datetime | None | Unset = UNSET
    text: None | str | Unset = UNSET
    twitter_id: None | str | Unset = UNSET
    twitter_author_id: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    conversation_id: None | str | Unset = UNSET
    referenced_tweets: list[ReferencedTweet] | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    hashtags: list[Hashtag] | None | Unset = UNSET
    mentions: list[Mention] | None | Unset = UNSET
    urls: list[URL] | None | Unset = UNSET
    cashtags: list[Cashtag] | None | Unset = UNSET
    context_annotations: list[ContextAnnotation] | None | Unset = UNSET
    user: None | TwitterUserModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cashtag import Cashtag # noqa: PLC0415
        from ..models.context_annotation import ContextAnnotation # noqa: PLC0415
        from ..models.hashtag import Hashtag # noqa: PLC0415
        from ..models.mention import Mention # noqa: PLC0415
        from ..models.referenced_tweet import ReferencedTweet # noqa: PLC0415
        from ..models.twitter_user_model import TwitterUserModel # noqa: PLC0415
        from ..models.url import URL # noqa: PLC0415
        created_at = self.created_at.isoformat()

        retweet_count = self.retweet_count

        reply_count = self.reply_count

        like_count = self.like_count

        quote_count = self.quote_count

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

        twitter_id: None | str | Unset
        if isinstance(self.twitter_id, Unset):
            twitter_id = UNSET
        else:
            twitter_id = self.twitter_id

        twitter_author_id: None | str | Unset
        if isinstance(self.twitter_author_id, Unset):
            twitter_author_id = UNSET
        else:
            twitter_author_id = self.twitter_author_id

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        conversation_id: None | str | Unset
        if isinstance(self.conversation_id, Unset):
            conversation_id = UNSET
        else:
            conversation_id = self.conversation_id

        referenced_tweets: list[dict[str, Any]] | None | Unset
        if isinstance(self.referenced_tweets, Unset):
            referenced_tweets = UNSET
        elif isinstance(self.referenced_tweets, list):
            referenced_tweets = []
            for referenced_tweets_type_0_item_data in self.referenced_tweets:
                referenced_tweets_type_0_item = referenced_tweets_type_0_item_data.to_dict()
                referenced_tweets.append(referenced_tweets_type_0_item)


        else:
            referenced_tweets = self.referenced_tweets

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        hashtags: list[dict[str, Any]] | None | Unset
        if isinstance(self.hashtags, Unset):
            hashtags = UNSET
        elif isinstance(self.hashtags, list):
            hashtags = []
            for hashtags_type_0_item_data in self.hashtags:
                hashtags_type_0_item = hashtags_type_0_item_data.to_dict()
                hashtags.append(hashtags_type_0_item)


        else:
            hashtags = self.hashtags

        mentions: list[dict[str, Any]] | None | Unset
        if isinstance(self.mentions, Unset):
            mentions = UNSET
        elif isinstance(self.mentions, list):
            mentions = []
            for mentions_type_0_item_data in self.mentions:
                mentions_type_0_item = mentions_type_0_item_data.to_dict()
                mentions.append(mentions_type_0_item)


        else:
            mentions = self.mentions

        urls: list[dict[str, Any]] | None | Unset
        if isinstance(self.urls, Unset):
            urls = UNSET
        elif isinstance(self.urls, list):
            urls = []
            for urls_type_0_item_data in self.urls:
                urls_type_0_item = urls_type_0_item_data.to_dict()
                urls.append(urls_type_0_item)


        else:
            urls = self.urls

        cashtags: list[dict[str, Any]] | None | Unset
        if isinstance(self.cashtags, Unset):
            cashtags = UNSET
        elif isinstance(self.cashtags, list):
            cashtags = []
            for cashtags_type_0_item_data in self.cashtags:
                cashtags_type_0_item = cashtags_type_0_item_data.to_dict()
                cashtags.append(cashtags_type_0_item)


        else:
            cashtags = self.cashtags

        context_annotations: list[dict[str, Any]] | None | Unset
        if isinstance(self.context_annotations, Unset):
            context_annotations = UNSET
        elif isinstance(self.context_annotations, list):
            context_annotations = []
            for context_annotations_type_0_item_data in self.context_annotations:
                context_annotations_type_0_item = context_annotations_type_0_item_data.to_dict()
                context_annotations.append(context_annotations_type_0_item)


        else:
            context_annotations = self.context_annotations

        user: dict[str, Any] | None | Unset
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, TwitterUserModel):
            user = self.user.to_dict()
        else:
            user = self.user


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_at": created_at,
            "retweet_count": retweet_count,
            "reply_count": reply_count,
            "like_count": like_count,
            "quote_count": quote_count,
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
        if twitter_id is not UNSET:
            field_dict["twitter_id"] = twitter_id
        if twitter_author_id is not UNSET:
            field_dict["twitter_author_id"] = twitter_author_id
        if language is not UNSET:
            field_dict["language"] = language
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if referenced_tweets is not UNSET:
            field_dict["referenced_tweets"] = referenced_tweets
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if hashtags is not UNSET:
            field_dict["hashtags"] = hashtags
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if urls is not UNSET:
            field_dict["urls"] = urls
        if cashtags is not UNSET:
            field_dict["cashtags"] = cashtags
        if context_annotations is not UNSET:
            field_dict["context_annotations"] = context_annotations
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cashtag import Cashtag # noqa: PLC0415
        from ..models.context_annotation import ContextAnnotation # noqa: PLC0415
        from ..models.hashtag import Hashtag # noqa: PLC0415
        from ..models.mention import Mention # noqa: PLC0415
        from ..models.referenced_tweet import ReferencedTweet # noqa: PLC0415
        from ..models.twitter_user_model import TwitterUserModel # noqa: PLC0415
        from ..models.url import URL # noqa: PLC0415
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))




        retweet_count = d.pop("retweet_count")

        reply_count = d.pop("reply_count")

        like_count = d.pop("like_count")

        quote_count = d.pop("quote_count")

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


        def _parse_twitter_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        twitter_id = _parse_twitter_id(d.pop("twitter_id", UNSET))


        def _parse_twitter_author_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        twitter_author_id = _parse_twitter_author_id(d.pop("twitter_author_id", UNSET))


        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))


        def _parse_conversation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conversation_id = _parse_conversation_id(d.pop("conversation_id", UNSET))


        def _parse_referenced_tweets(data: object) -> list[ReferencedTweet] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                referenced_tweets_type_0 = []
                _referenced_tweets_type_0 = data
                for referenced_tweets_type_0_item_data in (_referenced_tweets_type_0):
                    referenced_tweets_type_0_item = ReferencedTweet.from_dict(referenced_tweets_type_0_item_data)



                    referenced_tweets_type_0.append(referenced_tweets_type_0_item)

                return referenced_tweets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReferencedTweet] | None | Unset, data)

        referenced_tweets = _parse_referenced_tweets(d.pop("referenced_tweets", UNSET))


        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))


        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))


        def _parse_hashtags(data: object) -> list[Hashtag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hashtags_type_0 = []
                _hashtags_type_0 = data
                for hashtags_type_0_item_data in (_hashtags_type_0):
                    hashtags_type_0_item = Hashtag.from_dict(hashtags_type_0_item_data)



                    hashtags_type_0.append(hashtags_type_0_item)

                return hashtags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Hashtag] | None | Unset, data)

        hashtags = _parse_hashtags(d.pop("hashtags", UNSET))


        def _parse_mentions(data: object) -> list[Mention] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mentions_type_0 = []
                _mentions_type_0 = data
                for mentions_type_0_item_data in (_mentions_type_0):
                    mentions_type_0_item = Mention.from_dict(mentions_type_0_item_data)



                    mentions_type_0.append(mentions_type_0_item)

                return mentions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Mention] | None | Unset, data)

        mentions = _parse_mentions(d.pop("mentions", UNSET))


        def _parse_urls(data: object) -> list[URL] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                urls_type_0 = []
                _urls_type_0 = data
                for urls_type_0_item_data in (_urls_type_0):
                    urls_type_0_item = URL.from_dict(urls_type_0_item_data)



                    urls_type_0.append(urls_type_0_item)

                return urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[URL] | None | Unset, data)

        urls = _parse_urls(d.pop("urls", UNSET))


        def _parse_cashtags(data: object) -> list[Cashtag] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cashtags_type_0 = []
                _cashtags_type_0 = data
                for cashtags_type_0_item_data in (_cashtags_type_0):
                    cashtags_type_0_item = Cashtag.from_dict(cashtags_type_0_item_data)



                    cashtags_type_0.append(cashtags_type_0_item)

                return cashtags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Cashtag] | None | Unset, data)

        cashtags = _parse_cashtags(d.pop("cashtags", UNSET))


        def _parse_context_annotations(data: object) -> list[ContextAnnotation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                context_annotations_type_0 = []
                _context_annotations_type_0 = data
                for context_annotations_type_0_item_data in (_context_annotations_type_0):
                    context_annotations_type_0_item = ContextAnnotation.from_dict(context_annotations_type_0_item_data)



                    context_annotations_type_0.append(context_annotations_type_0_item)

                return context_annotations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContextAnnotation] | None | Unset, data)

        context_annotations = _parse_context_annotations(d.pop("context_annotations", UNSET))


        def _parse_user(data: object) -> None | TwitterUserModel | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = TwitterUserModel.from_dict(data)



                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TwitterUserModel | Unset, data)

        user = _parse_user(d.pop("user", UNSET))


        twitter_item_model = cls(
            created_at=created_at,
            retweet_count=retweet_count,
            reply_count=reply_count,
            like_count=like_count,
            quote_count=quote_count,
            item_id=item_id,
            project_id=project_id,
            type_=type_,
            time_edited=time_edited,
            text=text,
            twitter_id=twitter_id,
            twitter_author_id=twitter_author_id,
            language=language,
            conversation_id=conversation_id,
            referenced_tweets=referenced_tweets,
            latitude=latitude,
            longitude=longitude,
            hashtags=hashtags,
            mentions=mentions,
            urls=urls,
            cashtags=cashtags,
            context_annotations=context_annotations,
            user=user,
        )


        twitter_item_model.additional_properties = d
        return twitter_item_model

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
