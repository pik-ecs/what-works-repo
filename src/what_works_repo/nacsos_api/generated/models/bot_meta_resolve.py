from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.resolution_method import ResolutionMethod
from typing import cast

if TYPE_CHECKING:
  from ..models.resolution_snapshot_entry import ResolutionSnapshotEntry
  from ..models.snapshot_entry import SnapshotEntry





T = TypeVar("T", bound="BotMetaResolve")



@_attrs_define
class BotMetaResolve:
    """ 
        Attributes:
            algorithm (ResolutionMethod):
            ignore_hierarchy (bool):
            ignore_repeat (bool):
            snapshot (list[SnapshotEntry]):
            resolutions (list[ResolutionSnapshotEntry]):
     """

    algorithm: ResolutionMethod
    ignore_hierarchy: bool
    ignore_repeat: bool
    snapshot: list[SnapshotEntry]
    resolutions: list[ResolutionSnapshotEntry]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.resolution_snapshot_entry import ResolutionSnapshotEntry # noqa: PLC0415
        from ..models.snapshot_entry import SnapshotEntry # noqa: PLC0415
        algorithm = self.algorithm.value

        ignore_hierarchy = self.ignore_hierarchy

        ignore_repeat = self.ignore_repeat

        snapshot = []
        for snapshot_item_data in self.snapshot:
            snapshot_item = snapshot_item_data.to_dict()
            snapshot.append(snapshot_item)



        resolutions = []
        for resolutions_item_data in self.resolutions:
            resolutions_item = resolutions_item_data.to_dict()
            resolutions.append(resolutions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "algorithm": algorithm,
            "ignore_hierarchy": ignore_hierarchy,
            "ignore_repeat": ignore_repeat,
            "snapshot": snapshot,
            "resolutions": resolutions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resolution_snapshot_entry import ResolutionSnapshotEntry # noqa: PLC0415
        from ..models.snapshot_entry import SnapshotEntry # noqa: PLC0415
        d = dict(src_dict)
        algorithm = ResolutionMethod(d.pop("algorithm"))




        ignore_hierarchy = d.pop("ignore_hierarchy")

        ignore_repeat = d.pop("ignore_repeat")

        snapshot = []
        _snapshot = d.pop("snapshot")
        for snapshot_item_data in (_snapshot):
            snapshot_item = SnapshotEntry.from_dict(snapshot_item_data)



            snapshot.append(snapshot_item)


        resolutions = []
        _resolutions = d.pop("resolutions")
        for resolutions_item_data in (_resolutions):
            resolutions_item = ResolutionSnapshotEntry.from_dict(resolutions_item_data)



            resolutions.append(resolutions_item)


        bot_meta_resolve = cls(
            algorithm=algorithm,
            ignore_hierarchy=ignore_hierarchy,
            ignore_repeat=ignore_repeat,
            snapshot=snapshot,
            resolutions=resolutions,
        )


        bot_meta_resolve.additional_properties = d
        return bot_meta_resolve

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
