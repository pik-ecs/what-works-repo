from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.assignment_counts import AssignmentCounts
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
        "url": "/api/annotations/annotate/scope/counts/{assignment_scope_id}".format(assignment_scope_id=quote(str(assignment_scope_id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AssignmentCounts | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AssignmentCounts.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AssignmentCounts | HTTPValidationError]:
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

) -> Response[AssignmentCounts | HTTPValidationError]:
    """ Get Num Assignments For Scope

    Args:
        assignment_scope_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignmentCounts | HTTPValidationError]
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

) -> AssignmentCounts | HTTPValidationError | None:
    """ Get Num Assignments For Scope

    Args:
        assignment_scope_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignmentCounts | HTTPValidationError
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

) -> Response[AssignmentCounts | HTTPValidationError]:
    """ Get Num Assignments For Scope

    Args:
        assignment_scope_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignmentCounts | HTTPValidationError]
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

) -> AssignmentCounts | HTTPValidationError | None:
    """ Get Num Assignments For Scope

    Args:
        assignment_scope_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignmentCounts | HTTPValidationError
     """


    return (await asyncio_detailed(
        assignment_scope_id=assignment_scope_id,
client=client,
x_project_id=x_project_id,

    )).parsed
