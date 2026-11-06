from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auth_token_model import AuthTokenModel
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    token_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/login/token/{token_id}".format(token_id=quote(str(token_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuthTokenModel | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AuthTokenModel.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuthTokenModel | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    token_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[AuthTokenModel | HTTPValidationError]:
    """ Refresh Token

    Args:
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthTokenModel | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        token_id=token_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    token_id: str,
    *,
    client: AuthenticatedClient,

) -> AuthTokenModel | HTTPValidationError | None:
    """ Refresh Token

    Args:
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthTokenModel | HTTPValidationError
     """


    return sync_detailed(
        token_id=token_id,
client=client,

    ).parsed

async def asyncio_detailed(
    token_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[AuthTokenModel | HTTPValidationError]:
    """ Refresh Token

    Args:
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthTokenModel | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        token_id=token_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    token_id: str,
    *,
    client: AuthenticatedClient,

) -> AuthTokenModel | HTTPValidationError | None:
    """ Refresh Token

    Args:
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthTokenModel | HTTPValidationError
     """


    return (await asyncio_detailed(
        token_id=token_id,
client=client,

    )).parsed
