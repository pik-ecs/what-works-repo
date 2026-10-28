from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.open_alex_solr_import_def_type import OpenAlexSolrImportDefType
from ..models.open_alex_solr_import_field import OpenAlexSolrImportField
from ..models.open_alex_solr_import_op import OpenAlexSolrImportOp
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.open_alex_solr_import_params_type_0 import OpenAlexSolrImportParamsType0





T = TypeVar("T", bound="OpenAlexSolrImport")



@_attrs_define
class OpenAlexSolrImport:
    """ 
        Attributes:
            query (str):
            kind (Literal['oa-solr'] | Unset):  Default: 'oa-solr'.
            def_type (OpenAlexSolrImportDefType | Unset):  Default: OpenAlexSolrImportDefType.LUCENE.
            field (OpenAlexSolrImportField | Unset):  Default: OpenAlexSolrImportField.TITLE_ABSTRACT.
            op (OpenAlexSolrImportOp | Unset):  Default: OpenAlexSolrImportOp.AND.
            params (None | OpenAlexSolrImportParamsType0 | Unset):
     """

    query: str
    kind: Literal['oa-solr'] | Unset = 'oa-solr'
    def_type: OpenAlexSolrImportDefType | Unset = OpenAlexSolrImportDefType.LUCENE
    field: OpenAlexSolrImportField | Unset = OpenAlexSolrImportField.TITLE_ABSTRACT
    op: OpenAlexSolrImportOp | Unset = OpenAlexSolrImportOp.AND
    params: None | OpenAlexSolrImportParamsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.open_alex_solr_import_params_type_0 import OpenAlexSolrImportParamsType0 # noqa: PLC0415
        query = self.query

        kind = self.kind

        def_type: str | Unset = UNSET
        if not isinstance(self.def_type, Unset):
            def_type = self.def_type.value


        field: str | Unset = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.value


        op: str | Unset = UNSET
        if not isinstance(self.op, Unset):
            op = self.op.value


        params: dict[str, Any] | None | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        elif isinstance(self.params, OpenAlexSolrImportParamsType0):
            params = self.params.to_dict()
        else:
            params = self.params


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "query": query,
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if def_type is not UNSET:
            field_dict["def_type"] = def_type
        if field is not UNSET:
            field_dict["field"] = field
        if op is not UNSET:
            field_dict["op"] = op
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_alex_solr_import_params_type_0 import OpenAlexSolrImportParamsType0 # noqa: PLC0415
        d = dict(src_dict)
        query = d.pop("query")

        kind = cast(Literal['oa-solr'] | Unset , d.pop("kind", UNSET))
        if kind != 'oa-solr'and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'oa-solr', got '{kind}'")

        _def_type = d.pop("def_type", UNSET)
        def_type: OpenAlexSolrImportDefType | Unset
        if isinstance(_def_type,  Unset):
            def_type = UNSET
        else:
            def_type = OpenAlexSolrImportDefType(_def_type)




        _field = d.pop("field", UNSET)
        field: OpenAlexSolrImportField | Unset
        if isinstance(_field,  Unset):
            field = UNSET
        else:
            field = OpenAlexSolrImportField(_field)




        _op = d.pop("op", UNSET)
        op: OpenAlexSolrImportOp | Unset
        if isinstance(_op,  Unset):
            op = UNSET
        else:
            op = OpenAlexSolrImportOp(_op)




        def _parse_params(data: object) -> None | OpenAlexSolrImportParamsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                params_type_0 = OpenAlexSolrImportParamsType0.from_dict(data)



                return params_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OpenAlexSolrImportParamsType0 | Unset, data)

        params = _parse_params(d.pop("params", UNSET))


        open_alex_solr_import = cls(
            query=query,
            kind=kind,
            def_type=def_type,
            field=field,
            op=op,
            params=params,
        )


        open_alex_solr_import.additional_properties = d
        return open_alex_solr_import

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
