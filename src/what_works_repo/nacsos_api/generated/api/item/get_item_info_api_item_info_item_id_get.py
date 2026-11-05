from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.academic_item_model import AcademicItemModel
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    item_id: str,
    *,
    x_project_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-project-id"] = x_project_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/item/info/{item_id}".format(item_id=quote(str(item_id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AcademicItemModel | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AcademicItemModel.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AcademicItemModel | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[AcademicItemModel | HTTPValidationError]:
    """ Get Item Info

    Args:
        item_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcademicItemModel | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        item_id=item_id,
x_project_id=x_project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> AcademicItemModel | HTTPValidationError | None:
    """ Get Item Info

    Args:
        item_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcademicItemModel | HTTPValidationError
     """


    return sync_detailed(
        item_id=item_id,
client=client,
x_project_id=x_project_id,

    ).parsed

async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[AcademicItemModel | HTTPValidationError]:
    """ Get Item Info

    Args:
        item_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcademicItemModel | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        item_id=item_id,
x_project_id=x_project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> AcademicItemModel | HTTPValidationError | None:
    """ Get Item Info

    Args:
        item_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcademicItemModel | HTTPValidationError
     """


    return (await asyncio_detailed(
        item_id=item_id,
client=client,
x_project_id=x_project_id,

    )).parsed
