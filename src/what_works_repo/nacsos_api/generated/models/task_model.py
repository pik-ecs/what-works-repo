from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.task_status import TaskStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.task_model_params_type_0 import TaskModelParamsType0





T = TypeVar("T", bound="TaskModel")



@_attrs_define
class TaskModel:
    """ 
        Attributes:
            function_name (str):
            fingerprint (str):
            task_id (None | str | Unset | UUID):
            user_id (None | str | Unset | UUID):
            project_id (None | str | Unset | UUID):
            message_id (None | str | Unset | UUID):
            comment (None | str | Unset):
            params (None | str | TaskModelParamsType0 | Unset):
            time_created (datetime.datetime | None | Unset):
            time_started (datetime.datetime | None | Unset):
            time_finished (datetime.datetime | None | Unset):
            rec_expunge (datetime.datetime | None | Unset):
            status (TaskStatus | Unset):
     """

    function_name: str
    fingerprint: str
    task_id: None | str | Unset | UUID = UNSET
    user_id: None | str | Unset | UUID = UNSET
    project_id: None | str | Unset | UUID = UNSET
    message_id: None | str | Unset | UUID = UNSET
    comment: None | str | Unset = UNSET
    params: None | str | TaskModelParamsType0 | Unset = UNSET
    time_created: datetime.datetime | None | Unset = UNSET
    time_started: datetime.datetime | None | Unset = UNSET
    time_finished: datetime.datetime | None | Unset = UNSET
    rec_expunge: datetime.datetime | None | Unset = UNSET
    status: TaskStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.task_model_params_type_0 import TaskModelParamsType0 # noqa: PLC0415
        function_name = self.function_name

        fingerprint = self.fingerprint

        task_id: None | str | Unset
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        elif isinstance(self.task_id, UUID):
            task_id = str(self.task_id)
        else:
            task_id = self.task_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        message_id: None | str | Unset
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        elif isinstance(self.message_id, UUID):
            message_id = str(self.message_id)
        else:
            message_id = self.message_id

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        params: dict[str, Any] | None | str | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, TaskModelParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params

        time_created: None | str | Unset
        if isinstance(self.time_created, Unset):
            time_created = UNSET
        elif isinstance(self.time_created, datetime.datetime):
            time_created = self.time_created.isoformat()
        else:
            time_created = self.time_created

        time_started: None | str | Unset
        if isinstance(self.time_started, Unset):
            time_started = UNSET
        elif isinstance(self.time_started, datetime.datetime):
            time_started = self.time_started.isoformat()
        else:
            time_started = self.time_started

        time_finished: None | str | Unset
        if isinstance(self.time_finished, Unset):
            time_finished = UNSET
        elif isinstance(self.time_finished, datetime.datetime):
            time_finished = self.time_finished.isoformat()
        else:
            time_finished = self.time_finished

        rec_expunge: None | str | Unset
        if isinstance(self.rec_expunge, Unset):
            rec_expunge = UNSET
        elif isinstance(self.rec_expunge, datetime.datetime):
            rec_expunge = self.rec_expunge.isoformat()
        else:
            rec_expunge = self.rec_expunge

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "function_name": function_name,
            "fingerprint": fingerprint,
        })
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if params is not UNSET:
            field_dict["params"] = params
        if time_created is not UNSET:
            field_dict["time_created"] = time_created
        if time_started is not UNSET:
            field_dict["time_started"] = time_started
        if time_finished is not UNSET:
            field_dict["time_finished"] = time_finished
        if rec_expunge is not UNSET:
            field_dict["rec_expunge"] = rec_expunge
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_model_params_type_0 import TaskModelParamsType0 # noqa: PLC0415
        d = dict(src_dict)
        function_name = d.pop("function_name")

        fingerprint = d.pop("fingerprint")

        def _parse_task_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                task_id_type_1 = UUID(data)



                return task_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        task_id = _parse_task_id(d.pop("task_id", UNSET))


        def _parse_user_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_1 = UUID(data)



                return user_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


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


        def _parse_message_id(data: object) -> None | str | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                message_id_type_1 = UUID(data)



                return message_id_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | UUID, data)

        message_id = _parse_message_id(d.pop("message_id", UNSET))


        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        def _parse_params(data: object) -> None | str | TaskModelParamsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = TaskModelParamsType0.from_dict(data)



                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | TaskModelParamsType0 | Unset, data)

        params = _parse_params(d.pop("params", UNSET))


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


        def _parse_time_started(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_started_type_0 = datetime.datetime.fromisoformat(data)



                return time_started_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_started = _parse_time_started(d.pop("time_started", UNSET))


        def _parse_time_finished(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_finished_type_0 = datetime.datetime.fromisoformat(data)



                return time_finished_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_finished = _parse_time_finished(d.pop("time_finished", UNSET))


        def _parse_rec_expunge(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rec_expunge_type_0 = datetime.datetime.fromisoformat(data)



                return rec_expunge_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        rec_expunge = _parse_rec_expunge(d.pop("rec_expunge", UNSET))


        _status = d.pop("status", UNSET)
        status: TaskStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = TaskStatus(_status)




        task_model = cls(
            function_name=function_name,
            fingerprint=fingerprint,
            task_id=task_id,
            user_id=user_id,
            project_id=project_id,
            message_id=message_id,
            comment=comment,
            params=params,
            time_created=time_created,
            time_started=time_started,
            time_finished=time_finished,
            rec_expunge=rec_expunge,
            status=status,
        )


        task_model.additional_properties = d
        return task_model

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
