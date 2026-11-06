from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ris_label_format import RISLabelFormat
from ..types import UNSET, Unset
from typing import cast

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
  from ..models.label_options import LabelOptions
  from ..models.meta_filter_bool import MetaFilterBool
  from ..models.meta_filter_int import MetaFilterInt
  from ..models.meta_filter_str import MetaFilterStr
  from ..models.sub_query import SubQuery





T = TypeVar("T", bound="ExportRequest")



@_attrs_define
class ExportRequest:
    """ 
        Attributes:
            labels (list[LabelOptions]):
            nql_filter (AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter |
                LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None |
                SubQuery | Unset):
            bot_annotation_metadata_ids (list[str] | None | Unset):
            assignment_scope_ids (list[str] | None | Unset):
            user_ids (list[str] | None | Unset):
            ignore_hierarchy (bool | Unset):  Default: True.
            ignore_repeat (bool | Unset):  Default: True.
            columns_to_drop (list[str] | Unset):
            ris_label_format (RISLabelFormat | Unset):
     """

    labels: list[LabelOptions]
    nql_filter: AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None | SubQuery | Unset = UNSET
    bot_annotation_metadata_ids: list[str] | None | Unset = UNSET
    assignment_scope_ids: list[str] | None | Unset = UNSET
    user_ids: list[str] | None | Unset = UNSET
    ignore_hierarchy: bool | Unset = True
    ignore_repeat: bool | Unset = True
    columns_to_drop: list[str] | Unset = UNSET
    ris_label_format: RISLabelFormat | Unset = UNSET
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
        from ..models.label_options import LabelOptions # noqa: PLC0415
        from ..models.meta_filter_bool import MetaFilterBool # noqa: PLC0415
        from ..models.meta_filter_int import MetaFilterInt # noqa: PLC0415
        from ..models.meta_filter_str import MetaFilterStr # noqa: PLC0415
        from ..models.sub_query import SubQuery # noqa: PLC0415
        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)



        nql_filter: dict[str, Any] | None | Unset
        if isinstance(self.nql_filter, Unset):
            nql_filter = UNSET
        elif isinstance(self.nql_filter, FieldFilter):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, FieldFilters):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, LabelFilterMulti):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, LabelFilterBool):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, LabelFilterInt):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, AssignmentFilter):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, AnnotationFilter):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, AbstractFilter):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, ImportFilter):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, MetaFilterBool):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, MetaFilterInt):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, MetaFilterStr):
            nql_filter = self.nql_filter.to_dict()
        elif isinstance(self.nql_filter, SubQuery):
            nql_filter = self.nql_filter.to_dict()
        else:
            nql_filter = self.nql_filter

        bot_annotation_metadata_ids: list[str] | None | Unset
        if isinstance(self.bot_annotation_metadata_ids, Unset):
            bot_annotation_metadata_ids = UNSET
        elif isinstance(self.bot_annotation_metadata_ids, list):
            bot_annotation_metadata_ids = self.bot_annotation_metadata_ids


        else:
            bot_annotation_metadata_ids = self.bot_annotation_metadata_ids

        assignment_scope_ids: list[str] | None | Unset
        if isinstance(self.assignment_scope_ids, Unset):
            assignment_scope_ids = UNSET
        elif isinstance(self.assignment_scope_ids, list):
            assignment_scope_ids = self.assignment_scope_ids


        else:
            assignment_scope_ids = self.assignment_scope_ids

        user_ids: list[str] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = self.user_ids


        else:
            user_ids = self.user_ids

        ignore_hierarchy = self.ignore_hierarchy

        ignore_repeat = self.ignore_repeat

        columns_to_drop: list[str] | Unset = UNSET
        if not isinstance(self.columns_to_drop, Unset):
            columns_to_drop = self.columns_to_drop



        ris_label_format: str | Unset = UNSET
        if not isinstance(self.ris_label_format, Unset):
            ris_label_format = self.ris_label_format.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "labels": labels,
        })
        if nql_filter is not UNSET:
            field_dict["nql_filter"] = nql_filter
        if bot_annotation_metadata_ids is not UNSET:
            field_dict["bot_annotation_metadata_ids"] = bot_annotation_metadata_ids
        if assignment_scope_ids is not UNSET:
            field_dict["assignment_scope_ids"] = assignment_scope_ids
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids
        if ignore_hierarchy is not UNSET:
            field_dict["ignore_hierarchy"] = ignore_hierarchy
        if ignore_repeat is not UNSET:
            field_dict["ignore_repeat"] = ignore_repeat
        if columns_to_drop is not UNSET:
            field_dict["columns_to_drop"] = columns_to_drop
        if ris_label_format is not UNSET:
            field_dict["ris_label_format"] = ris_label_format

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
        from ..models.label_options import LabelOptions # noqa: PLC0415
        from ..models.meta_filter_bool import MetaFilterBool # noqa: PLC0415
        from ..models.meta_filter_int import MetaFilterInt # noqa: PLC0415
        from ..models.meta_filter_str import MetaFilterStr # noqa: PLC0415
        from ..models.sub_query import SubQuery # noqa: PLC0415
        d = dict(src_dict)
        labels = []
        _labels = d.pop("labels")
        for labels_item_data in (_labels):
            labels_item = LabelOptions.from_dict(labels_item_data)



            labels.append(labels_item)


        def _parse_nql_filter(data: object) -> AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None | SubQuery | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_0 = FieldFilter.from_dict(data)



                return nql_filter_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_1 = FieldFilters.from_dict(data)



                return nql_filter_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_2 = LabelFilterMulti.from_dict(data)



                return nql_filter_type_0_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_3 = LabelFilterBool.from_dict(data)



                return nql_filter_type_0_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_4 = LabelFilterInt.from_dict(data)



                return nql_filter_type_0_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_5 = AssignmentFilter.from_dict(data)



                return nql_filter_type_0_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_6 = AnnotationFilter.from_dict(data)



                return nql_filter_type_0_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_7 = AbstractFilter.from_dict(data)



                return nql_filter_type_0_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_8 = ImportFilter.from_dict(data)



                return nql_filter_type_0_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_9 = MetaFilterBool.from_dict(data)



                return nql_filter_type_0_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_10 = MetaFilterInt.from_dict(data)



                return nql_filter_type_0_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_11 = MetaFilterStr.from_dict(data)



                return nql_filter_type_0_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                nql_filter_type_0_type_12 = SubQuery.from_dict(data)



                return nql_filter_type_0_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AbstractFilter | AnnotationFilter | AssignmentFilter | FieldFilter | FieldFilters | ImportFilter | LabelFilterBool | LabelFilterInt | LabelFilterMulti | MetaFilterBool | MetaFilterInt | MetaFilterStr | None | SubQuery | Unset, data)

        nql_filter = _parse_nql_filter(d.pop("nql_filter", UNSET))


        def _parse_bot_annotation_metadata_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bot_annotation_metadata_ids_type_0 = cast(list[str], data)

                return bot_annotation_metadata_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        bot_annotation_metadata_ids = _parse_bot_annotation_metadata_ids(d.pop("bot_annotation_metadata_ids", UNSET))


        def _parse_assignment_scope_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assignment_scope_ids_type_0 = cast(list[str], data)

                return assignment_scope_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        assignment_scope_ids = _parse_assignment_scope_ids(d.pop("assignment_scope_ids", UNSET))


        def _parse_user_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = cast(list[str], data)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("user_ids", UNSET))


        ignore_hierarchy = d.pop("ignore_hierarchy", UNSET)

        ignore_repeat = d.pop("ignore_repeat", UNSET)

        columns_to_drop = cast(list[str], d.pop("columns_to_drop", UNSET))


        _ris_label_format = d.pop("ris_label_format", UNSET)
        ris_label_format: RISLabelFormat | Unset
        if isinstance(_ris_label_format,  Unset):
            ris_label_format = UNSET
        else:
            ris_label_format = RISLabelFormat(_ris_label_format)




        export_request = cls(
            labels=labels,
            nql_filter=nql_filter,
            bot_annotation_metadata_ids=bot_annotation_metadata_ids,
            assignment_scope_ids=assignment_scope_ids,
            user_ids=user_ids,
            ignore_hierarchy=ignore_hierarchy,
            ignore_repeat=ignore_repeat,
            columns_to_drop=columns_to_drop,
            ris_label_format=ris_label_format,
        )


        export_request.additional_properties = d
        return export_request

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
