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
  from ..models.ieuuid import IEUUID





T = TypeVar("T", bound="ImportFilter")



@_attrs_define
class ImportFilter:
    """ 
        Attributes:
            import_ids (list[IEUUID]):
            filter_ (Literal['import'] | Unset):  Default: 'import'.
     """

    import_ids: list[IEUUID]
    filter_: Literal['import'] | Unset = 'import'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ieuuid import IEUUID # noqa: PLC0415
        import_ids = []
        for import_ids_item_data in self.import_ids:
            import_ids_item = import_ids_item_data.to_dict()
            import_ids.append(import_ids_item)



        filter_ = self.filter_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "import_ids": import_ids,
        })
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ieuuid import IEUUID # noqa: PLC0415
        d = dict(src_dict)
        import_ids = []
        _import_ids = d.pop("import_ids")
        for import_ids_item_data in (_import_ids):
            import_ids_item = IEUUID.from_dict(import_ids_item_data)



            import_ids.append(import_ids_item)


        filter_ = cast(Literal['import'] | Unset , d.pop("filter", UNSET))
        if filter_ != 'import'and not isinstance(filter_, Unset):
            raise ValueError(f"filter must match const 'import', got '{filter_}'")

        import_filter = cls(
            import_ids=import_ids,
            filter_=filter_,
        )


        import_filter.additional_properties = d
        return import_filter

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
