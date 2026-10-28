from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.assignment_status import AssignmentStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="AssignmentModel")



@_attrs_define
class AssignmentModel:
    """ Corresponds to db.models.annotations.Assignment

    Assignment is used to request a user/annotator (User) to annotate a particular item (BaseItem) in the database
    following a pre-defined annotation scheme (AnnotationScheme).

    Each AnnotationScheme will have several Assignments.
    Each User will "receive" several Assignments.
    Each Item may have several Assignments (either in relation to different AnnotationSchemes or double-coding).
    The Project is implicit by the AnnotationScheme.

    The most common use-cases are:
      * Creating assignments in bulk at random (e.g. 3 users should annotate 50 documents each)
      * Creating assignments one at a time based on a set of rules (e.g. for double-coding, defined order, bias, ...)
      * Creating assignments in small batches or one-by-one in prioritised annotation settings

        Attributes:
            assignment_scope_id (str | UUID):
            user_id (str | UUID):
            item_id (str | UUID):
            annotation_scheme_id (str | UUID):
            status (AssignmentStatus):
            assignment_id (None | str | Unset | UUID):
            order (int | None | Unset):
     """

    assignment_scope_id: str | UUID
    user_id: str | UUID
    item_id: str | UUID
    annotation_scheme_id: str | UUID
    status: AssignmentStatus
    assignment_id: None | str | Unset | UUID = UNSET
    order: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        assignment_scope_id: str
        if isinstance(self.assignment_scope_id, UUID):
            assignment_scope_id = str(self.assignment_scope_id)
        else:
            assignment_scope_id = self.assignment_scope_id

        user_id: str
        if isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        item_id: str
        if isinstance(self.item_id, UUID):
            item_id = str(self.item_id)
        else:
            item_id = self.item_id

        annotation_scheme_id: str
        if isinstance(self.annotation_scheme_id, UUID):
            annotation_scheme_id = str(self.annotation_scheme_id)
        else:
            annotation_scheme_id = self.annotation_scheme_id

        status = self.status.value

        assignment_id: None | str | Unset
        if isinstance(self.assignment_id, Unset):
            assignment_id = UNSET
        elif isinstance(self.assignment_id, UUID):
            assignment_id = str(self.assignment_id)
        else:
            assignment_id = self.assignment_id

        order: int | None | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "assignment_scope_id": assignment_scope_id,
            "user_id": user_id,
            "item_id": item_id,
            "annotation_scheme_id": annotation_scheme_id,
            "status": status,
        })
        if assignment_id is not UNSET:
            field_dict["assignment_id"] = assignment_id
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_assignment_scope_id(data: object) -> str | UUID:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignment_scope_id_type_1 = UUID(data)



                return assignment_scope_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | UUID, data)

        assignment_scope_id = _parse_assignment_scope_id(d.pop("assignment_scope_id"))


        def _parse_user_id(data: object) -> str | UUID:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_1 = UUID(data)



                return user_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | UUID, data)

        user_id = _parse_user_id(d.pop("user_id"))


        def _parse_item_id(data: object) -> str | UUID:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                item_id_type_1 = UUID(data)



                return item_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | UUID, data)

        item_id = _parse_item_id(d.pop("item_id"))


        def _parse_annotation_scheme_id(data: object) -> str | UUID:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                annotation_scheme_id_type_1 = UUID(data)



                return annotation_scheme_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | UUID, data)

        annotation_scheme_id = _parse_annotation_scheme_id(d.pop("annotation_scheme_id"))


        status = AssignmentStatus(d.pop("status"))




        def _parse_assignment_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assignment_id_type_1 = UUID(data)



                return assignment_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        assignment_id = _parse_assignment_id(d.pop("assignment_id", UNSET))


        def _parse_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        order = _parse_order(d.pop("order", UNSET))


        assignment_model = cls(
            assignment_scope_id=assignment_scope_id,
            user_id=user_id,
            item_id=item_id,
            annotation_scheme_id=annotation_scheme_id,
            status=status,
            assignment_id=assignment_id,
            order=order,
        )


        assignment_model.additional_properties = d
        return assignment_model

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
