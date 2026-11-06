from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.abstract_filter import AbstractFilter
  from ..models.annotation_filter import AnnotationFilter
  from ..models.assignment_config_random_overlaps import AssignmentConfigRandomOverlaps
  from ..models.assignment_config_random_users import AssignmentConfigRandomUsers
  from ..models.assignment_filter import AssignmentFilter
  from ..models.field_filter import FieldFilter
  from ..models.field_filters import FieldFilters
  from ..models.import_filter import ImportFilter
  from ..models.label_filter_bool import LabelFilterBool
  from ..models.label_filter_int import LabelFilterInt
  from ..models.label_filter_multi import LabelFilterMulti
  from ..models.meta_filter_bool import MetaFilterBool
  from ..models.meta_filter_int import MetaFilterInt
  from ..models.meta_filter_str import MetaFilterStr
  from ..models.sub_query import SubQuery





T = TypeVar("T", bound="AssignmentConfigRandom")



@_attrs_define
class AssignmentConfigRandom:
    """ 
        Attributes:
            users (AssignmentConfigRandomUsers):
            overlaps (AssignmentConfigRandomOverlaps):
            nql (str):
            random_seed (int | Unset):  Default: 1337.
            config_type (Literal['RANDOM'] | Unset):  Default: 'RANDOM'.
            nql_parsed (AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter |
                LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None |
                SubQuery | Unset):
     """

    users: AssignmentConfigRandomUsers
    overlaps: AssignmentConfigRandomOverlaps
    nql: str
    random_seed: int | Unset = 1337
    config_type: Literal['RANDOM'] | Unset = 'RANDOM'
    nql_parsed: AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None | SubQuery | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.abstract_filter import AbstractFilter # noqa: PLC0415
        from ..models.annotation_filter import AnnotationFilter # noqa: PLC0415
        from ..models.assignment_config_random_overlaps import AssignmentConfigRandomOverlaps # noqa: PLC0415
        from ..models.assignment_config_random_users import AssignmentConfigRandomUsers # noqa: PLC0415
        from ..models.assignment_filter import AssignmentFilter # noqa: PLC0415
        from ..models.field_filter import FieldFilter # noqa: PLC0415
        from ..models.field_filters import FieldFilters # noqa: PLC0415
        from ..models.import_filter import ImportFilter # noqa: PLC0415
        from ..models.label_filter_bool import LabelFilterBool # noqa: PLC0415
        from ..models.label_filter_int import LabelFilterInt # noqa: PLC0415
        from ..models.label_filter_multi import LabelFilterMulti # noqa: PLC0415
        from ..models.meta_filter_bool import MetaFilterBool # noqa: PLC0415
        from ..models.meta_filter_int import MetaFilterInt # noqa: PLC0415
        from ..models.meta_filter_str import MetaFilterStr # noqa: PLC0415
        from ..models.sub_query import SubQuery # noqa: PLC0415
        users = self.users.to_dict()

        overlaps = self.overlaps.to_dict()

        nql = self.nql

        random_seed = self.random_seed

        config_type = self.config_type

        nql_parsed: dict[str, Any] | None | Unset
        if isinstance(self.nql_parsed, Unset):
            nql_parsed = UNSET
        elif isinstance(self.nql_parsed, FieldFilter):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, FieldFilters):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, LabelFilterMulti):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, LabelFilterBool):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, LabelFilterInt):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, AssignmentFilter):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, AnnotationFilter):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, AbstractFilter):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, ImportFilter):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, MetaFilterBool):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, MetaFilterInt):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, MetaFilterStr):
            nql_parsed = self.nql_parsed.to_dict()
        elif isinstance(self.nql_parsed, SubQuery):
            nql_parsed = self.nql_parsed.to_dict()
        else:
            nql_parsed = self.nql_parsed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "users": users,
            "overlaps": overlaps,
            "nql": nql,
        })
        if random_seed is not UNSET:
            field_dict["random_seed"] = random_seed
        if config_type is not UNSET:
            field_dict["config_type"] = config_type
        if nql_parsed is not UNSET:
            field_dict["nql_parsed"] = nql_parsed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_filter import AbstractFilter # noqa: PLC0415
        from ..models.annotation_filter import AnnotationFilter # noqa: PLC0415
        from ..models.assignment_config_random_overlaps import AssignmentConfigRandomOverlaps # noqa: PLC0415
        from ..models.assignment_config_random_users import AssignmentConfigRandomUsers # noqa: PLC0415
        from ..models.assignment_filter import AssignmentFilter # noqa: PLC0415
        from ..models.field_filter import FieldFilter # noqa: PLC0415
        from ..models.field_filters import FieldFilters # noqa: PLC0415
        from ..models.import_filter import ImportFilter # noqa: PLC0415
        from ..models.label_filter_bool import LabelFilterBool # noqa: PLC0415
        from ..models.label_filter_int import LabelFilterInt # noqa: PLC0415
        from ..models.label_filter_multi import LabelFilterMulti # noqa: PLC0415
        from ..models.meta_filter_bool import MetaFilterBool # noqa: PLC0415
        from ..models.meta_filter_int import MetaFilterInt # noqa: PLC0415
        from ..models.meta_filter_str import MetaFilterStr # noqa: PLC0415
        from ..models.sub_query import SubQuery # noqa: PLC0415
        d = dict(src_dict)
        users = AssignmentConfigRandomUsers.from_dict(d.pop("users"))




        overlaps = AssignmentConfigRandomOverlaps.from_dict(d.pop("overlaps"))




        nql = d.pop("nql")

        random_seed = d.pop("random_seed", UNSET)

        config_type = cast(Literal['RANDOM'] | Unset , d.pop("config_type", UNSET))
        if config_type != 'RANDOM'and not isinstance(config_type, Unset):
            raise ValueError(f"config_type must match const 'RANDOM', got '{config_type}'")

        def _parse_nql_parsed(data: object) -> AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None | SubQuery | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_0 = FieldFilter.from_dict(data)



                return nql_parsed_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_1 = FieldFilters.from_dict(data)



                return nql_parsed_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_2 = LabelFilterMulti.from_dict(data)



                return nql_parsed_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_3 = LabelFilterBool.from_dict(data)



                return nql_parsed_type_0_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_4 = LabelFilterInt.from_dict(data)



                return nql_parsed_type_0_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_5 = AssignmentFilter.from_dict(data)



                return nql_parsed_type_0_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_6 = AnnotationFilter.from_dict(data)



                return nql_parsed_type_0_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_7 = AbstractFilter.from_dict(data)



                return nql_parsed_type_0_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_8 = ImportFilter.from_dict(data)



                return nql_parsed_type_0_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_9 = MetaFilterBool.from_dict(data)



                return nql_parsed_type_0_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_10 = MetaFilterInt.from_dict(data)



                return nql_parsed_type_0_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_11 = MetaFilterStr.from_dict(data)



                return nql_parsed_type_0_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_parsed_type_0_type_12 = SubQuery.from_dict(data)



                return nql_parsed_type_0_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None | SubQuery | Unset, data)

        nql_parsed = _parse_nql_parsed(d.pop("nql_parsed", UNSET))


        assignment_config_random = cls(
            users=users,
            overlaps=overlaps,
            nql=nql,
            random_seed=random_seed,
            config_type=config_type,
            nql_parsed=nql_parsed,
        )


        assignment_config_random.additional_properties = d
        return assignment_config_random

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
