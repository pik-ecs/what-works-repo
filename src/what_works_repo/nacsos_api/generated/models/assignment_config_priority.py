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
  from ..models.assignment_config_priority_overlaps import AssignmentConfigPriorityOverlaps
  from ..models.assignment_config_priority_users import AssignmentConfigPriorityUsers





T = TypeVar("T", bound="AssignmentConfigPriority")



@_attrs_define
class AssignmentConfigPriority:
    """ 
        Attributes:
            users (AssignmentConfigPriorityUsers):
            overlaps (AssignmentConfigPriorityOverlaps):
            priority_id (str):
            prio_offset (int):
            random_seed (int | Unset):  Default: 1337.
            config_type (Literal['PRIORITY'] | Unset):  Default: 'PRIORITY'.
     """

    users: AssignmentConfigPriorityUsers
    overlaps: AssignmentConfigPriorityOverlaps
    priority_id: str
    prio_offset: int
    random_seed: int | Unset = 1337
    config_type: Literal['PRIORITY'] | Unset = 'PRIORITY'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.assignment_config_priority_overlaps import AssignmentConfigPriorityOverlaps # noqa: PLC0415
        from ..models.assignment_config_priority_users import AssignmentConfigPriorityUsers # noqa: PLC0415
        users = self.users.to_dict()

        overlaps = self.overlaps.to_dict()

        priority_id = self.priority_id

        prio_offset = self.prio_offset

        random_seed = self.random_seed

        config_type = self.config_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "users": users,
            "overlaps": overlaps,
            "priority_id": priority_id,
            "prio_offset": prio_offset,
        })
        if random_seed is not UNSET:
            field_dict["random_seed"] = random_seed
        if config_type is not UNSET:
            field_dict["config_type"] = config_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.assignment_config_priority_overlaps import AssignmentConfigPriorityOverlaps # noqa: PLC0415
        from ..models.assignment_config_priority_users import AssignmentConfigPriorityUsers # noqa: PLC0415
        d = dict(src_dict)
        users = AssignmentConfigPriorityUsers.from_dict(d.pop("users"))




        overlaps = AssignmentConfigPriorityOverlaps.from_dict(d.pop("overlaps"))




        priority_id = d.pop("priority_id")

        prio_offset = d.pop("prio_offset")

        random_seed = d.pop("random_seed", UNSET)

        config_type = cast(Literal['PRIORITY'] | Unset , d.pop("config_type", UNSET))
        if config_type != 'PRIORITY'and not isinstance(config_type, Unset):
            raise ValueError(f"config_type must match const 'PRIORITY', got '{config_type}'")

        assignment_config_priority = cls(
            users=users,
            overlaps=overlaps,
            priority_id=priority_id,
            prio_offset=prio_offset,
            random_seed=random_seed,
            config_type=config_type,
        )


        assignment_config_priority.additional_properties = d
        return assignment_config_priority

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
