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

if TYPE_CHECKING:
  from ..models.academic_item_import import AcademicItemImport
  from ..models.open_alex_file_import import OpenAlexFileImport
  from ..models.open_alex_solr_import import OpenAlexSolrImport
  from ..models.scopus_api_import import ScopusAPIImport
  from ..models.scopus_import import ScopusImport
  from ..models.wo_s_import import WoSImport





T = TypeVar("T", bound="ImportModel")



@_attrs_define
class ImportModel:
    """ 
        Attributes:
            project_id (str | UUID):
            name (str):
            description (str):
            type_ (str):
            import_id (None | str | Unset | UUID):
            user_id (None | str | Unset | UUID):
            time_created (datetime.datetime | None | Unset):
            config (AcademicItemImport | None | OpenAlexFileImport | OpenAlexSolrImport | ScopusAPIImport | ScopusImport |
                Unset | WoSImport):
     """

    project_id: str | UUID
    name: str
    description: str
    type_: str
    import_id: None | str | Unset | UUID = UNSET
    user_id: None | str | Unset | UUID = UNSET
    time_created: datetime.datetime | None | Unset = UNSET
    config: AcademicItemImport | None | OpenAlexFileImport | OpenAlexSolrImport | ScopusAPIImport | ScopusImport | Unset | WoSImport = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.academic_item_import import AcademicItemImport # noqa: PLC0415
        from ..models.open_alex_file_import import OpenAlexFileImport # noqa: PLC0415
        from ..models.open_alex_solr_import import OpenAlexSolrImport # noqa: PLC0415
        from ..models.scopus_api_import import ScopusAPIImport # noqa: PLC0415
        from ..models.scopus_import import ScopusImport # noqa: PLC0415
        from ..models.wo_s_import import WoSImport # noqa: PLC0415
        project_id: str
        if isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        name = self.name

        description = self.description

        type_ = self.type_

        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        elif isinstance(self.import_id, UUID):
            import_id = str(self.import_id)
        else:
            import_id = self.import_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        time_created: None | str | Unset
        if isinstance(self.time_created, Unset):
            time_created = UNSET
        elif isinstance(self.time_created, datetime.datetime):
            time_created = self.time_created.isoformat()
        else:
            time_created = self.time_created

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, ScopusImport):
            config = self.config.to_dict()
        elif isinstance(self.config, ScopusAPIImport):
            config = self.config.to_dict()
        elif isinstance(self.config, AcademicItemImport):
            config = self.config.to_dict()
        elif isinstance(self.config, OpenAlexFileImport):
            config = self.config.to_dict()
        elif isinstance(self.config, OpenAlexSolrImport):
            config = self.config.to_dict()
        elif isinstance(self.config, WoSImport):
            config = self.config.to_dict()
        else:
            config = self.config


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "project_id": project_id,
            "name": name,
            "description": description,
            "type": type_,
        })
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if time_created is not UNSET:
            field_dict["time_created"] = time_created
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.academic_item_import import AcademicItemImport # noqa: PLC0415
        from ..models.open_alex_file_import import OpenAlexFileImport # noqa: PLC0415
        from ..models.open_alex_solr_import import OpenAlexSolrImport # noqa: PLC0415
        from ..models.scopus_api_import import ScopusAPIImport # noqa: PLC0415
        from ..models.scopus_import import ScopusImport # noqa: PLC0415
        from ..models.wo_s_import import WoSImport # noqa: PLC0415
        d = dict(src_dict)
        def _parse_project_id(data: object) -> str | UUID:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_0 = UUID(data)



                return project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | UUID, data)

        project_id = _parse_project_id(d.pop("project_id"))


        name = d.pop("name")

        description = d.pop("description")

        type_ = d.pop("type")

        def _parse_import_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                import_id_type_0 = UUID(data)



                return import_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        import_id = _parse_import_id(d.pop("import_id", UNSET))


        def _parse_user_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)



                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


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


        def _parse_config(data: object) -> AcademicItemImport | None | OpenAlexFileImport | OpenAlexSolrImport | ScopusAPIImport | ScopusImport | Unset | WoSImport:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_0 = ScopusImport.from_dict(data)



                return config_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_1 = ScopusAPIImport.from_dict(data)



                return config_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_2 = AcademicItemImport.from_dict(data)



                return config_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_3 = OpenAlexFileImport.from_dict(data)



                return config_type_0_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_4 = OpenAlexSolrImport.from_dict(data)



                return config_type_0_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0_type_5 = WoSImport.from_dict(data)



                return config_type_0_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AcademicItemImport | None | OpenAlexFileImport | OpenAlexSolrImport | ScopusAPIImport | ScopusImport | Unset | WoSImport, data)

        config = _parse_config(d.pop("config", UNSET))


        import_model = cls(
            project_id=project_id,
            name=name,
            description=description,
            type_=type_,
            import_id=import_id,
            user_id=user_id,
            time_created=time_created,
            config=config,
        )


        import_model.additional_properties = d
        return import_model

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
