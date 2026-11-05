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





T = TypeVar("T", bound="SubQuery")



@_attrs_define
class SubQuery:
    """ 
        Attributes:
            filter_ (Literal['sub'] | Unset):  Default: 'sub'.
            and_ (list[AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter |
                LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | SubQuery]
                | None | Unset):
            or_ (list[AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter |
                LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | SubQuery]
                | None | Unset):
            not_ (AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter |
                LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None |
                SubQuery | Unset):
     """

    filter_: Literal['sub'] | Unset = 'sub'
    and_: list[AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | SubQuery] | None | Unset = UNSET
    or_: list[AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | SubQuery] | None | Unset = UNSET
    not_: AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None | SubQuery | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.abstract_filter import AbstractFilter # noqa: PLC0415
        from ..models.annotation_filter import AnnotationFilter # noqa: PLC0415
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
        filter_ = self.filter_

        and_: list[dict[str, Any]] | None | Unset
        if isinstance(self.and_, Unset):
            and_ = UNSET
        elif isinstance(self.and_, list):
            and_ = []
            for and_type_0_item_data in self.and_:
                and_type_0_item: dict[str, Any]
                if isinstance(and_type_0_item_data, FieldFilter):
                    and_type_0_item = and_type_0_item_data.to_dict()
                elif isinstance(and_type_0_item_data, FieldFilters):
                    and_type_0_item = and_type_0_item_data.to_dict()
                elif isinstance(and_type_0_item_data, LabelFilterMulti):
                    and_type_0_item = and_type_0_item_data.to_dict()
                elif isinstance(and_type_0_item_data, LabelFilterBool):
                    and_type_0_item = and_type_0_item_data.to_dict()
                elif isinstance(and_type_0_item_data, LabelFilterInt):
                    and_type_0_item = and_type_0_item_data.to_dict()
                elif isinstance(and_type_0_item_data, AssignmentFilter):
                    and_type_0_item = and_type_0_item_data.to_dict()
                elif isinstance(and_type_0_item_data, AnnotationFilter):
                    and_type_0_item = and_type_0_item_data.to_dict()
                elif isinstance(and_type_0_item_data, AbstractFilter):
                    and_type_0_item = and_type_0_item_data.to_dict()
                elif isinstance(and_type_0_item_data, ImportFilter):
                    and_type_0_item = and_type_0_item_data.to_dict()
                elif isinstance(and_type_0_item_data, MetaFilterBool):
                    and_type_0_item = and_type_0_item_data.to_dict()
                elif isinstance(and_type_0_item_data, MetaFilterInt):
                    and_type_0_item = and_type_0_item_data.to_dict()
                elif isinstance(and_type_0_item_data, MetaFilterStr):
                    and_type_0_item = and_type_0_item_data.to_dict()
                else:
                    and_type_0_item = and_type_0_item_data.to_dict()

                and_.append(and_type_0_item)


        else:
            and_ = self.and_

        or_: list[dict[str, Any]] | None | Unset
        if isinstance(self.or_, Unset):
            or_ = UNSET
        elif isinstance(self.or_, list):
            or_ = []
            for or_type_0_item_data in self.or_:
                or_type_0_item: dict[str, Any]
                if isinstance(or_type_0_item_data, FieldFilter):
                    or_type_0_item = or_type_0_item_data.to_dict()
                elif isinstance(or_type_0_item_data, FieldFilters):
                    or_type_0_item = or_type_0_item_data.to_dict()
                elif isinstance(or_type_0_item_data, LabelFilterMulti):
                    or_type_0_item = or_type_0_item_data.to_dict()
                elif isinstance(or_type_0_item_data, LabelFilterBool):
                    or_type_0_item = or_type_0_item_data.to_dict()
                elif isinstance(or_type_0_item_data, LabelFilterInt):
                    or_type_0_item = or_type_0_item_data.to_dict()
                elif isinstance(or_type_0_item_data, AssignmentFilter):
                    or_type_0_item = or_type_0_item_data.to_dict()
                elif isinstance(or_type_0_item_data, AnnotationFilter):
                    or_type_0_item = or_type_0_item_data.to_dict()
                elif isinstance(or_type_0_item_data, AbstractFilter):
                    or_type_0_item = or_type_0_item_data.to_dict()
                elif isinstance(or_type_0_item_data, ImportFilter):
                    or_type_0_item = or_type_0_item_data.to_dict()
                elif isinstance(or_type_0_item_data, MetaFilterBool):
                    or_type_0_item = or_type_0_item_data.to_dict()
                elif isinstance(or_type_0_item_data, MetaFilterInt):
                    or_type_0_item = or_type_0_item_data.to_dict()
                elif isinstance(or_type_0_item_data, MetaFilterStr):
                    or_type_0_item = or_type_0_item_data.to_dict()
                else:
                    or_type_0_item = or_type_0_item_data.to_dict()

                or_.append(or_type_0_item)


        else:
            or_ = self.or_

        not_: dict[str, Any] | None | Unset
        if isinstance(self.not_, Unset):
            not_ = UNSET
        elif isinstance(self.not_, FieldFilter):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, FieldFilters):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, LabelFilterMulti):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, LabelFilterBool):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, LabelFilterInt):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, AssignmentFilter):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, AnnotationFilter):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, AbstractFilter):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, ImportFilter):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, MetaFilterBool):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, MetaFilterInt):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, MetaFilterStr):
            not_ = self.not_.to_dict()
        elif isinstance(self.not_, SubQuery):
            not_ = self.not_.to_dict()
        else:
            not_ = self.not_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if and_ is not UNSET:
            field_dict["and_"] = and_
        if or_ is not UNSET:
            field_dict["or_"] = or_
        if not_ is not UNSET:
            field_dict["not_"] = not_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_filter import AbstractFilter # noqa: PLC0415
        from ..models.annotation_filter import AnnotationFilter # noqa: PLC0415
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
        d = dict(src_dict)
        filter_ = cast(Literal['sub'] | Unset , d.pop("filter", UNSET))
        if filter_ != 'sub'and not isinstance(filter_, Unset):
            raise ValueError(f"filter must match const 'sub', got '{filter_}'")

        def _parse_and_(data: object) -> list[AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | SubQuery] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                and_type_0 = []
                _and_type_0 = data
                for and_type_0_item_data in (_and_type_0):
                    def _parse_and_type_0_item(data: object) -> AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | SubQuery:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_0 = FieldFilter.from_dict(data)



                            return and_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_1 = FieldFilters.from_dict(data)



                            return and_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_2 = LabelFilterMulti.from_dict(data)



                            return and_type_0_item_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_3 = LabelFilterBool.from_dict(data)



                            return and_type_0_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_4 = LabelFilterInt.from_dict(data)



                            return and_type_0_item_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_5 = AssignmentFilter.from_dict(data)



                            return and_type_0_item_type_5
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_6 = AnnotationFilter.from_dict(data)



                            return and_type_0_item_type_6
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_7 = AbstractFilter.from_dict(data)



                            return and_type_0_item_type_7
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_8 = ImportFilter.from_dict(data)



                            return and_type_0_item_type_8
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_9 = MetaFilterBool.from_dict(data)



                            return and_type_0_item_type_9
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_10 = MetaFilterInt.from_dict(data)



                            return and_type_0_item_type_10
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            and_type_0_item_type_11 = MetaFilterStr.from_dict(data)



                            return and_type_0_item_type_11
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        and_type_0_item_type_12 = SubQuery.from_dict(data)



                        return and_type_0_item_type_12

                    and_type_0_item = _parse_and_type_0_item(and_type_0_item_data)

                    and_type_0.append(and_type_0_item)

                return and_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | SubQuery] | None | Unset, data)

        and_ = _parse_and_(d.pop("and_", UNSET))


        def _parse_or_(data: object) -> list[AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | SubQuery] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                or_type_0 = []
                _or_type_0 = data
                for or_type_0_item_data in (_or_type_0):
                    def _parse_or_type_0_item(data: object) -> AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | SubQuery:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_0 = FieldFilter.from_dict(data)



                            return or_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_1 = FieldFilters.from_dict(data)



                            return or_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_2 = LabelFilterMulti.from_dict(data)



                            return or_type_0_item_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_3 = LabelFilterBool.from_dict(data)



                            return or_type_0_item_type_3
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_4 = LabelFilterInt.from_dict(data)



                            return or_type_0_item_type_4
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_5 = AssignmentFilter.from_dict(data)



                            return or_type_0_item_type_5
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_6 = AnnotationFilter.from_dict(data)



                            return or_type_0_item_type_6
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_7 = AbstractFilter.from_dict(data)



                            return or_type_0_item_type_7
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_8 = ImportFilter.from_dict(data)



                            return or_type_0_item_type_8
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_9 = MetaFilterBool.from_dict(data)



                            return or_type_0_item_type_9
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_10 = MetaFilterInt.from_dict(data)



                            return or_type_0_item_type_10
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            or_type_0_item_type_11 = MetaFilterStr.from_dict(data)



                            return or_type_0_item_type_11
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        or_type_0_item_type_12 = SubQuery.from_dict(data)



                        return or_type_0_item_type_12

                    or_type_0_item = _parse_or_type_0_item(or_type_0_item_data)

                    or_type_0.append(or_type_0_item)

                return or_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | SubQuery] | None | Unset, data)

        or_ = _parse_or_(d.pop("or_", UNSET))


        def _parse_not_(data: object) -> AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None | SubQuery | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_0 = FieldFilter.from_dict(data)



                return not_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_1 = FieldFilters.from_dict(data)



                return not_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_2 = LabelFilterMulti.from_dict(data)



                return not_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_3 = LabelFilterBool.from_dict(data)



                return not_type_0_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_4 = LabelFilterInt.from_dict(data)



                return not_type_0_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_5 = AssignmentFilter.from_dict(data)



                return not_type_0_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_6 = AnnotationFilter.from_dict(data)



                return not_type_0_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_7 = AbstractFilter.from_dict(data)



                return not_type_0_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_8 = ImportFilter.from_dict(data)



                return not_type_0_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_9 = MetaFilterBool.from_dict(data)



                return not_type_0_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_10 = MetaFilterInt.from_dict(data)



                return not_type_0_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_11 = MetaFilterStr.from_dict(data)



                return not_type_0_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                not_type_0_type_12 = SubQuery.from_dict(data)



                return not_type_0_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None | SubQuery | Unset, data)

        not_ = _parse_not_(d.pop("not_", UNSET))


        sub_query = cls(
            filter_=filter_,
            and_=and_,
            or_=or_,
            not_=not_,
        )


        sub_query.additional_properties = d
        return sub_query

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
