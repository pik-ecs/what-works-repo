from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.assignment_model import AssignmentModel
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    assignment_scope_id: str,
    *,
    x_project_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-project-id"] = x_project_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/annotations/annotate/assignments/scope/{assignment_scope_id}".format(assignment_scope_id=quote(str(assignment_scope_id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | list[AssignmentModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = AssignmentModel.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | list[AssignmentModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    assignment_scope_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[HTTPValidationError | list[AssignmentModel]]:
    """ Get Assignments For Scope

    Args:
        assignment_scope_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[AssignmentModel]]
     """


    kwargs = _get_kwargs(
        assignment_scope_id=assignment_scope_id,
x_project_id=x_project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    assignment_scope_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> HTTPValidationError | list[AssignmentModel] | None:
    """ Get Assignments For Scope

    Args:
        assignment_scope_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[AssignmentModel]
     """


    return sync_detailed(
        assignment_scope_id=assignment_scope_id,
client=client,
x_project_id=x_project_id,

    ).parsed

async def asyncio_detailed(
    assignment_scope_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[HTTPValidationError | list[AssignmentModel]]:
    """ Get Assignments For Scope

    Args:
        assignment_scope_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[AssignmentModel]]
     """


    kwargs = _get_kwargs(
        assignment_scope_id=assignment_scope_id,
x_project_id=x_project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    assignment_scope_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> HTTPValidationError | list[AssignmentModel] | None:
    """ Get Assignments For Scope

    Args:
        assignment_scope_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[AssignmentModel]
     """


    return (await asyncio_detailed(
        assignment_scope_id=assignment_scope_id,
client=client,
x_project_id=x_project_id,

    )).parsed
