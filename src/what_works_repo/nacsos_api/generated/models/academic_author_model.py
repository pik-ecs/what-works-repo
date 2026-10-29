from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.academic_author_model_meta_type_0 import AcademicAuthorModelMetaType0
  from ..models.affiliation_model import AffiliationModel





T = TypeVar("T", bound="AcademicAuthorModel")



@_attrs_define
class AcademicAuthorModel:
    """ 
        Attributes:
            name (str):
            surname_initials (None | str | Unset):
            email (None | str | Unset):
            orcid (None | str | Unset):
            scopus_id (None | str | Unset):
            openalex_id (None | str | Unset):
            s2_id (None | str | Unset):
            dimensions_id (None | str | Unset):
            affiliations (list[AffiliationModel] | None | Unset):
            meta (AcademicAuthorModelMetaType0 | None | Unset):
     """

    name: str
    surname_initials: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    orcid: None | str | Unset = UNSET
    scopus_id: None | str | Unset = UNSET
    openalex_id: None | str | Unset = UNSET
    s2_id: None | str | Unset = UNSET
    dimensions_id: None | str | Unset = UNSET
    affiliations: list[AffiliationModel] | None | Unset = UNSET
    meta: AcademicAuthorModelMetaType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.academic_author_model_meta_type_0 import AcademicAuthorModelMetaType0 # noqa: PLC0415
        from ..models.affiliation_model import AffiliationModel # noqa: PLC0415
        name = self.name

        surname_initials: None | str | Unset
        if isinstance(self.surname_initials, Unset):
            surname_initials = UNSET
        else:
            surname_initials = self.surname_initials

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        orcid: None | str | Unset
        if isinstance(self.orcid, Unset):
            orcid = UNSET
        else:
            orcid = self.orcid

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

        dimensions_id: None | str | Unset
        if isinstance(self.dimensions_id, Unset):
            dimensions_id = UNSET
        else:
            dimensions_id = self.dimensions_id

        affiliations: list[dict[str, Any]] | None | Unset
        if isinstance(self.affiliations, Unset):
            affiliations = UNSET
        elif isinstance(self.affiliations, list):
            affiliations = []
            for affiliations_type_0_item_data in self.affiliations:
                affiliations_type_0_item = affiliations_type_0_item_data.to_dict()
                affiliations.append(affiliations_type_0_item)


        else:
            affiliations = self.affiliations

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, AcademicAuthorModelMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if surname_initials is not UNSET:
            field_dict["surname_initials"] = surname_initials
        if email is not UNSET:
            field_dict["email"] = email
        if orcid is not UNSET:
            field_dict["orcid"] = orcid
        if scopus_id is not UNSET:
            field_dict["scopus_id"] = scopus_id
        if openalex_id is not UNSET:
            field_dict["openalex_id"] = openalex_id
        if s2_id is not UNSET:
            field_dict["s2_id"] = s2_id
        if dimensions_id is not UNSET:
            field_dict["dimensions_id"] = dimensions_id
        if affiliations is not UNSET:
            field_dict["affiliations"] = affiliations
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.academic_author_model_meta_type_0 import AcademicAuthorModelMetaType0 # noqa: PLC0415
        from ..models.affiliation_model import AffiliationModel # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_surname_initials(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        surname_initials = _parse_surname_initials(d.pop("surname_initials", UNSET))


        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_orcid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        orcid = _parse_orcid(d.pop("orcid", UNSET))


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


        def _parse_dimensions_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dimensions_id = _parse_dimensions_id(d.pop("dimensions_id", UNSET))


        def _parse_affiliations(data: object) -> list[AffiliationModel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                affiliations_type_0 = []
                _affiliations_type_0 = data
                for affiliations_type_0_item_data in (_affiliations_type_0):
                    affiliations_type_0_item = AffiliationModel.from_dict(affiliations_type_0_item_data)



                    affiliations_type_0.append(affiliations_type_0_item)

                return affiliations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AffiliationModel] | None | Unset, data)

        affiliations = _parse_affiliations(d.pop("affiliations", UNSET))


        def _parse_meta(data: object) -> AcademicAuthorModelMetaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = AcademicAuthorModelMetaType0.from_dict(data)



                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AcademicAuthorModelMetaType0 | None | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))


        academic_author_model = cls(
            name=name,
            surname_initials=surname_initials,
            email=email,
            orcid=orcid,
            scopus_id=scopus_id,
            openalex_id=openalex_id,
            s2_id=s2_id,
            dimensions_id=dimensions_id,
            affiliations=affiliations,
            meta=meta,
        )


        academic_author_model.additional_properties = d
        return academic_author_model

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
