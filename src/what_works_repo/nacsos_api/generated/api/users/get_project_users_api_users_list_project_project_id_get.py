from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.user_base_model import UserBaseModel
from typing import cast



def _get_kwargs(
    project_id: str,
    *,
    x_project_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-project-id"] = x_project_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/users/list/project/{project_id}".format(project_id=quote(str(project_id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | list[UserBaseModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = UserBaseModel.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | list[UserBaseModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[HTTPValidationError | list[UserBaseModel]]:
    """ Get Project Users

    Args:
        project_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[UserBaseModel]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
x_project_id=x_project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> HTTPValidationError | list[UserBaseModel] | None:
    """ Get Project Users

    Args:
        project_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[UserBaseModel]
     """


    return sync_detailed(
        project_id=project_id,
client=client,
x_project_id=x_project_id,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[HTTPValidationError | list[UserBaseModel]]:
    """ Get Project Users

    Args:
        project_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[UserBaseModel]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
x_project_id=x_project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> HTTPValidationError | list[UserBaseModel] | None:
    """ Get Project Users

    Args:
        project_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[UserBaseModel]
     """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,
x_project_id=x_project_id,

    )).parsed
