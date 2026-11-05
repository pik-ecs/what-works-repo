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
  from ..models.academic_author_model import AcademicAuthorModel
  from ..models.academic_item_model_meta_type_0 import AcademicItemModelMetaType0





T = TypeVar("T", bound="AcademicItemModel")



@_attrs_define
class AcademicItemModel:
    """ Corresponds to db.schema.items.academic.AcademicItem

        Attributes:
            item_id (None | str | Unset | UUID):
            project_id (None | str | Unset | UUID):
            type_ (ItemType | Unset):
            time_edited (datetime.datetime | None | Unset):
            text (None | str | Unset):
            doi (None | str | Unset):
            wos_id (None | str | Unset):
            scopus_id (None | str | Unset):
            openalex_id (None | str | Unset):
            s2_id (None | str | Unset):
            pubmed_id (None | str | Unset):
            dimensions_id (None | str | Unset):
            title (None | str | Unset):
            title_slug (None | str | Unset):
            publication_year (int | None | Unset):
            source (None | str | Unset):
            keywords (list[str] | None | Unset):
            authors (list[AcademicAuthorModel] | None | Unset):
            meta (AcademicItemModelMetaType0 | None | Unset):
     """

    item_id: None | str | Unset | UUID = UNSET
    project_id: None | str | Unset | UUID = UNSET
    type_: ItemType | Unset = UNSET
    time_edited: datetime.datetime | None | Unset = UNSET
    text: None | str | Unset = UNSET
    doi: None | str | Unset = UNSET
    wos_id: None | str | Unset = UNSET
    scopus_id: None | str | Unset = UNSET
    openalex_id: None | str | Unset = UNSET
    s2_id: None | str | Unset = UNSET
    pubmed_id: None | str | Unset = UNSET
    dimensions_id: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    title_slug: None | str | Unset = UNSET
    publication_year: int | None | Unset = UNSET
    source: None | str | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    authors: list[AcademicAuthorModel] | None | Unset = UNSET
    meta: AcademicItemModelMetaType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.academic_author_model import AcademicAuthorModel # noqa: PLC0415
        from ..models.academic_item_model_meta_type_0 import AcademicItemModelMetaType0 # noqa: PLC0415
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

        doi: None | str | Unset
        if isinstance(self.doi, Unset):
            doi = UNSET
        else:
            doi = self.doi

        wos_id: None | str | Unset
        if isinstance(self.wos_id, Unset):
            wos_id = UNSET
        else:
            wos_id = self.wos_id

        scopus_id: None | str | Unset
        if isinstance(self.scopus_id, Unset):
            scopus_id = UNSET
        else:
            scopus_id = self.scopus_id

        openalex_id: None | str | Unset
        if isinstance(self.openalex_id, Unset):
            openalex_id = UNSET
        else:
            openalex_id = self.openalex_id

        s2_id: None | str | Unset
        if isinstance(self.s2_id, Unset):
            s2_id = UNSET
        else:
            s2_id = self.s2_id

        pubmed_id: None | str | Unset
        if isinstance(self.pubmed_id, Unset):
            pubmed_id = UNSET
        else:
            pubmed_id = self.pubmed_id

        dimensions_id: None | str | Unset
        if isinstance(self.dimensions_id, Unset):
            dimensions_id = UNSET
        else:
            dimensions_id = self.dimensions_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        title_slug: None | str | Unset
        if isinstance(self.title_slug, Unset):
            title_slug = UNSET
        else:
            title_slug = self.title_slug

        publication_year: int | None | Unset
        if isinstance(self.publication_year, Unset):
            publication_year = UNSET
        else:
            publication_year = self.publication_year

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords


        else:
            keywords = self.keywords

        authors: list[dict[str, Any]] | None | Unset
        if isinstance(self.authors, Unset):
            authors = UNSET
        elif isinstance(self.authors, list):
            authors = []
            for authors_type_0_item_data in self.authors:
                authors_type_0_item = authors_type_0_item_data.to_dict()
                authors.append(authors_type_0_item)


        else:
            authors = self.authors

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, AcademicItemModelMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta


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
        if doi is not UNSET:
            field_dict["doi"] = doi
        if wos_id is not UNSET:
            field_dict["wos_id"] = wos_id
        if scopus_id is not UNSET:
            field_dict["scopus_id"] = scopus_id
        if openalex_id is not UNSET:
            field_dict["openalex_id"] = openalex_id
        if s2_id is not UNSET:
            field_dict["s2_id"] = s2_id
        if pubmed_id is not UNSET:
            field_dict["pubmed_id"] = pubmed_id
        if dimensions_id is not UNSET:
            field_dict["dimensions_id"] = dimensions_id
        if title is not UNSET:
            field_dict["title"] = title
        if title_slug is not UNSET:
            field_dict["title_slug"] = title_slug
        if publication_year is not UNSET:
            field_dict["publication_year"] = publication_year
        if source is not UNSET:
            field_dict["source"] = source
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if authors is not UNSET:
            field_dict["authors"] = authors
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.academic_author_model import AcademicAuthorModel # noqa: PLC0415
        from ..models.academic_item_model_meta_type_0 import AcademicItemModelMetaType0 # noqa: PLC0415
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


        def _parse_doi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        doi = _parse_doi(d.pop("doi", UNSET))


        def _parse_wos_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wos_id = _parse_wos_id(d.pop("wos_id", UNSET))


        def _parse_scopus_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scopus_id = _parse_scopus_id(d.pop("scopus_id", UNSET))


        def _parse_openalex_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        openalex_id = _parse_openalex_id(d.pop("openalex_id", UNSET))


        def _parse_s2_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s2_id = _parse_s2_id(d.pop("s2_id", UNSET))


        def _parse_pubmed_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pubmed_id = _parse_pubmed_id(d.pop("pubmed_id", UNSET))


        def _parse_dimensions_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dimensions_id = _parse_dimensions_id(d.pop("dimensions_id", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_title_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title_slug = _parse_title_slug(d.pop("title_slug", UNSET))


        def _parse_publication_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        publication_year = _parse_publication_year(d.pop("publication_year", UNSET))


        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))


        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))


        def _parse_authors(data: object) -> list[AcademicAuthorModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                authors_type_0 = []
                _authors_type_0 = data
                for authors_type_0_item_data in (_authors_type_0):
                    authors_type_0_item = AcademicAuthorModel.from_dict(authors_type_0_item_data)



                    authors_type_0.append(authors_type_0_item)

                return authors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AcademicAuthorModel] | None | Unset, data)

        authors = _parse_authors(d.pop("authors", UNSET))


        def _parse_meta(data: object) -> AcademicItemModelMetaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = AcademicItemModelMetaType0.from_dict(data)



                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AcademicItemModelMetaType0 | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))


        academic_item_model = cls(
            item_id=item_id,
            project_id=project_id,
            type_=type_,
            time_edited=time_edited,
            text=text,
            doi=doi,
            wos_id=wos_id,
            scopus_id=scopus_id,
            openalex_id=openalex_id,
            s2_id=s2_id,
            pubmed_id=pubmed_id,
            dimensions_id=dimensions_id,
            title=title,
            title_slug=title_slug,
            publication_year=publication_year,
            source=source,
            keywords=keywords,
            authors=authors,
            meta=meta,
        )


        academic_item_model.additional_properties = d
        return academic_item_model

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
