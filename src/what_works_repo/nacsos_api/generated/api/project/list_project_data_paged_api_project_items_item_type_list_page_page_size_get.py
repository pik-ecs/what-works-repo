from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.academic_item_model import AcademicItemModel
from ...models.full_lexis_nexis_item_model import FullLexisNexisItemModel
from ...models.generic_item_model import GenericItemModel
from ...models.http_validation_error import HTTPValidationError
from ...models.lexis_nexis_item_model import LexisNexisItemModel
from ...models.list_project_data_paged_api_project_items_item_type_list_page_page_size_get_item_type import ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType
from ...models.twitter_item_model import TwitterItemModel
from typing import cast



def _get_kwargs(
    item_type: ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType,
    page: int,
    page_size: int,
    *,
    x_project_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-project-id"] = x_project_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/project/items/{item_type}/list/{page}/{page_size}".format(item_type=quote(str(item_type), safe=""),page=quote(str(page), safe=""),page_size=quote(str(page_size), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | list[AcademicItemModel] | list[FullLexisNexisItemModel] | list[GenericItemModel] | list[LexisNexisItemModel] | list[TwitterItemModel] | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> list[AcademicItemModel] | list[FullLexisNexisItemModel] | list[GenericItemModel] | list[LexisNexisItemModel] | list[TwitterItemModel]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in (_response_200_type_0):
                    response_200_type_0_item = TwitterItemModel.from_dict(response_200_type_0_item_data)



                    response_200_type_0.append(response_200_type_0_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_1 = []
                _response_200_type_1 = data
                for response_200_type_1_item_data in (_response_200_type_1):
                    response_200_type_1_item = AcademicItemModel.from_dict(response_200_type_1_item_data)



                    response_200_type_1.append(response_200_type_1_item)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_2 = []
                _response_200_type_2 = data
                for response_200_type_2_item_data in (_response_200_type_2):
                    response_200_type_2_item = LexisNexisItemModel.from_dict(response_200_type_2_item_data)



                    response_200_type_2.append(response_200_type_2_item)

                return response_200_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_3 = []
                _response_200_type_3 = data
                for response_200_type_3_item_data in (_response_200_type_3):
                    response_200_type_3_item = FullLexisNexisItemModel.from_dict(response_200_type_3_item_data)



                    response_200_type_3.append(response_200_type_3_item)

                return response_200_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_4 = []
            _response_200_type_4 = data
            for response_200_type_4_item_data in (_response_200_type_4):
                response_200_type_4_item = GenericItemModel.from_dict(response_200_type_4_item_data)



                response_200_type_4.append(response_200_type_4_item)

            return response_200_type_4

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | list[AcademicItemModel] | list[FullLexisNexisItemModel] | list[GenericItemModel] | list[LexisNexisItemModel] | list[TwitterItemModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_type: ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType,
    page: int,
    page_size: int,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[HTTPValidationError | list[AcademicItemModel] | list[FullLexisNexisItemModel] | list[GenericItemModel] | list[LexisNexisItemModel] | list[TwitterItemModel]]:
    """ List Project Data Paged

    Args:
        item_type (ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType):
        page (int):
        page_size (int):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[AcademicItemModel] | list[FullLexisNexisItemModel] | list[GenericItemModel] | list[LexisNexisItemModel] | list[TwitterItemModel]]
     """


    kwargs = _get_kwargs(
        item_type=item_type,
page=page,
page_size=page_size,
x_project_id=x_project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    item_type: ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType,
    page: int,
    page_size: int,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> HTTPValidationError | list[AcademicItemModel] | list[FullLexisNexisItemModel] | list[GenericItemModel] | list[LexisNexisItemModel] | list[TwitterItemModel] | None:
    """ List Project Data Paged

    Args:
        item_type (ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType):
        page (int):
        page_size (int):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[AcademicItemModel] | list[FullLexisNexisItemModel] | list[GenericItemModel] | list[LexisNexisItemModel] | list[TwitterItemModel]
     """


    return sync_detailed(
        item_type=item_type,
page=page,
page_size=page_size,
client=client,
x_project_id=x_project_id,

    ).parsed

async def asyncio_detailed(
    item_type: ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType,
    page: int,
    page_size: int,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[HTTPValidationError | list[AcademicItemModel] | list[FullLexisNexisItemModel] | list[GenericItemModel] | list[LexisNexisItemModel] | list[TwitterItemModel]]:
    """ List Project Data Paged

    Args:
        item_type (ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType):
        page (int):
        page_size (int):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[AcademicItemModel] | list[FullLexisNexisItemModel] | list[GenericItemModel] | list[LexisNexisItemModel] | list[TwitterItemModel]]
     """


    kwargs = _get_kwargs(
        item_type=item_type,
page=page,
page_size=page_size,
x_project_id=x_project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    item_type: ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType,
    page: int,
    page_size: int,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> HTTPValidationError | list[AcademicItemModel] | list[FullLexisNexisItemModel] | list[GenericItemModel] | list[LexisNexisItemModel] | list[TwitterItemModel] | None:
    """ List Project Data Paged

    Args:
        item_type (ListProjectDataPagedApiProjectItemsItemTypeListPagePageSizeGetItemType):
        page (int):
        page_size (int):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[AcademicItemModel] | list[FullLexisNexisItemModel] | list[GenericItemModel] | list[LexisNexisItemModel] | list[TwitterItemModel]
     """


    return (await asyncio_detailed(
        item_type=item_type,
page=page,
page_size=page_size,
client=client,
x_project_id=x_project_id,

    )).parsed
