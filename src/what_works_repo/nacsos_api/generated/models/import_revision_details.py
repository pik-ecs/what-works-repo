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
  from ..models.task_model import TaskModel





T = TypeVar("T", bound="ImportRevisionDetails")



@_attrs_define
class ImportRevisionDetails:
    """ 
        Attributes:
            import_revision_counter (int):
            time_created (datetime.datetime):
            import_revision_id (None | str | Unset | UUID):
            pipeline_task_id (None | str | Unset):
            import_id (None | str | Unset | UUID):
            num_items_retrieved (int | None | Unset):
            num_items (int | None | Unset):
            num_items_new (int | None | Unset):
            num_items_updated (int | None | Unset):
            num_items_removed (int | None | Unset):
            task (None | TaskModel | Unset):
     """

    import_revision_counter: int
    time_created: datetime.datetime
    import_revision_id: None | str | Unset | UUID = UNSET
    pipeline_task_id: None | str | Unset = UNSET
    import_id: None | str | Unset | UUID = UNSET
    num_items_retrieved: int | None | Unset = UNSET
    num_items: int | None | Unset = UNSET
    num_items_new: int | None | Unset = UNSET
    num_items_updated: int | None | Unset = UNSET
    num_items_removed: int | None | Unset = UNSET
    task: None | TaskModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.task_model import TaskModel # noqa: PLC0415
        import_revision_counter = self.import_revision_counter

        time_created = self.time_created.isoformat()

        import_revision_id: None | str | Unset
        if isinstance(self.import_revision_id, Unset):
            import_revision_id = UNSET
        elif isinstance(self.import_revision_id, UUID):
            import_revision_id = str(self.import_revision_id)
        else:
            import_revision_id = self.import_revision_id

        pipeline_task_id: None | str | Unset
        if isinstance(self.pipeline_task_id, Unset):
            pipeline_task_id = UNSET
        else:
            pipeline_task_id = self.pipeline_task_id

        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        elif isinstance(self.import_id, UUID):
            import_id = str(self.import_id)
        else:
            import_id = self.import_id

        num_items_retrieved: int | None | Unset
        if isinstance(self.num_items_retrieved, Unset):
            num_items_retrieved = UNSET
        else:
            num_items_retrieved = self.num_items_retrieved

        num_items: int | None | Unset
        if isinstance(self.num_items, Unset):
            num_items = UNSET
        else:
            num_items = self.num_items

        num_items_new: int | None | Unset
        if isinstance(self.num_items_new, Unset):
            num_items_new = UNSET
        else:
            num_items_new = self.num_items_new

        num_items_updated: int | None | Unset
        if isinstance(self.num_items_updated, Unset):
            num_items_updated = UNSET
        else:
            num_items_updated = self.num_items_updated

        num_items_removed: int | None | Unset
        if isinstance(self.num_items_removed, Unset):
            num_items_removed = UNSET
        else:
            num_items_removed = self.num_items_removed

        task: dict[str, Any] | None | Unset
        if isinstance(self.task, Unset):
            task = UNSET
        elif isinstance(self.task, TaskModel):
            task = self.task.to_dict()
        else:
            task = self.task


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "import_revision_counter": import_revision_counter,
            "time_created": time_created,
        })
        if import_revision_id is not UNSET:
            field_dict["import_revision_id"] = import_revision_id
        if pipeline_task_id is not UNSET:
            field_dict["pipeline_task_id"] = pipeline_task_id
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if num_items_retrieved is not UNSET:
            field_dict["num_items_retrieved"] = num_items_retrieved
        if num_items is not UNSET:
            field_dict["num_items"] = num_items
        if num_items_new is not UNSET:
            field_dict["num_items_new"] = num_items_new
        if num_items_updated is not UNSET:
            field_dict["num_items_updated"] = num_items_updated
        if num_items_removed is not UNSET:
            field_dict["num_items_removed"] = num_items_removed
        if task is not UNSET:
            field_dict["task"] = task

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_model import TaskModel # noqa: PLC0415
        d = dict(src_dict)
        import_revision_counter = d.pop("import_revision_counter")

        time_created = datetime.datetime.fromisoformat(d.pop("time_created"))




        def _parse_import_revision_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                import_revision_id_type_0 = UUID(data)



                return import_revision_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        import_revision_id = _parse_import_revision_id(d.pop("import_revision_id", UNSET))


        def _parse_pipeline_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pipeline_task_id = _parse_pipeline_task_id(d.pop("pipeline_task_id", UNSET))


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


        def _parse_num_items_retrieved(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_items_retrieved = _parse_num_items_retrieved(d.pop("num_items_retrieved", UNSET))


        def _parse_num_items(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_items = _parse_num_items(d.pop("num_items", UNSET))


        def _parse_num_items_new(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_items_new = _parse_num_items_new(d.pop("num_items_new", UNSET))


        def _parse_num_items_updated(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_items_updated = _parse_num_items_updated(d.pop("num_items_updated", UNSET))


        def _parse_num_items_removed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_items_removed = _parse_num_items_removed(d.pop("num_items_removed", UNSET))


        def _parse_task(data: object) -> None | TaskModel | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                task_type_0 = TaskModel.from_dict(data)



                return task_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TaskModel | Unset, data)

        task = _parse_task(d.pop("task", UNSET))


        import_revision_details = cls(
            import_revision_counter=import_revision_counter,
            time_created=time_created,
            import_revision_id=import_revision_id,
            pipeline_task_id=pipeline_task_id,
            import_id=import_id,
            num_items_retrieved=num_items_retrieved,
            num_items=num_items,
            num_items_new=num_items_new,
            num_items_updated=num_items_updated,
            num_items_removed=num_items_removed,
            task=task,
        )


        import_revision_details.additional_properties = d
        return import_revision_details

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
