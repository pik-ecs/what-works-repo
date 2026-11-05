from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bot_annotation_meta_data_model import BotAnnotationMetaDataModel
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    only_resolve: bool | Unset = False,
    x_project_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-project-id"] = x_project_id



    

    params: dict[str, Any] = {}

    params["only_resolve"] = only_resolve


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/annotations/bot/scopes",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | list[BotAnnotationMetaDataModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = BotAnnotationMetaDataModel.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | list[BotAnnotationMetaDataModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    only_resolve: bool | Unset = False,
    x_project_id: str,

) -> Response[HTTPValidationError | list[BotAnnotationMetaDataModel]]:
    """ Get Bot Scopes

    Args:
        only_resolve (bool | Unset):  Default: False.
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[BotAnnotationMetaDataModel]]
     """


    kwargs = _get_kwargs(
        only_resolve=only_resolve,
x_project_id=x_project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    only_resolve: bool | Unset = False,
    x_project_id: str,

) -> HTTPValidationError | list[BotAnnotationMetaDataModel] | None:
    """ Get Bot Scopes

    Args:
        only_resolve (bool | Unset):  Default: False.
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[BotAnnotationMetaDataModel]
     """


    return sync_detailed(
        client=client,
only_resolve=only_resolve,
x_project_id=x_project_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    only_resolve: bool | Unset = False,
    x_project_id: str,

) -> Response[HTTPValidationError | list[BotAnnotationMetaDataModel]]:
    """ Get Bot Scopes

    Args:
        only_resolve (bool | Unset):  Default: False.
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[BotAnnotationMetaDataModel]]
     """


    kwargs = _get_kwargs(
        only_resolve=only_resolve,
x_project_id=x_project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    only_resolve: bool | Unset = False,
    x_project_id: str,

) -> HTTPValidationError | list[BotAnnotationMetaDataModel] | None:
    """ Get Bot Scopes

    Args:
        only_resolve (bool | Unset):  Default: False.
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[BotAnnotationMetaDataModel]
     """


    return (await asyncio_detailed(
        client=client,
only_resolve=only_resolve,
x_project_id=x_project_id,

    )).parsed
