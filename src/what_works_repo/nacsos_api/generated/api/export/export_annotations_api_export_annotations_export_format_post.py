from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.export_request import ExportRequest
from ...models.export_type_enum import ExportTypeEnum
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    export_format: ExportTypeEnum,
    *,
    body: ExportRequest,
    max_results: int | Unset = 15000,
    x_project_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-project-id"] = x_project_id



    

    params: dict[str, Any] = {}

    params["max_results"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/export/annotations/{export_format}".format(export_format=quote(str(export_format), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    export_format: ExportTypeEnum,
    *,
    client: AuthenticatedClient,
    body: ExportRequest,
    max_results: int | Unset = 15000,
    x_project_id: str,

) -> Response[Any | HTTPValidationError]:
    """ Export Annotations

    Args:
        export_format (ExportTypeEnum):
        max_results (int | Unset):  Default: 15000.
        x_project_id (str):
        body (ExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        export_format=export_format,
body=body,
max_results=max_results,
x_project_id=x_project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    export_format: ExportTypeEnum,
    *,
    client: AuthenticatedClient,
    body: ExportRequest,
    max_results: int | Unset = 15000,
    x_project_id: str,

) -> Any | HTTPValidationError | None:
    """ Export Annotations

    Args:
        export_format (ExportTypeEnum):
        max_results (int | Unset):  Default: 15000.
        x_project_id (str):
        body (ExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return sync_detailed(
        export_format=export_format,
client=client,
body=body,
max_results=max_results,
x_project_id=x_project_id,

    ).parsed

async def asyncio_detailed(
    export_format: ExportTypeEnum,
    *,
    client: AuthenticatedClient,
    body: ExportRequest,
    max_results: int | Unset = 15000,
    x_project_id: str,

) -> Response[Any | HTTPValidationError]:
    """ Export Annotations

    Args:
        export_format (ExportTypeEnum):
        max_results (int | Unset):  Default: 15000.
        x_project_id (str):
        body (ExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        export_format=export_format,
body=body,
max_results=max_results,
x_project_id=x_project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    export_format: ExportTypeEnum,
    *,
    client: AuthenticatedClient,
    body: ExportRequest,
    max_results: int | Unset = 15000,
    x_project_id: str,

) -> Any | HTTPValidationError | None:
    """ Export Annotations

    Args:
        export_format (ExportTypeEnum):
        max_results (int | Unset):  Default: 15000.
        x_project_id (str):
        body (ExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
     """


    return (await asyncio_detailed(
        export_format=export_format,
client=client,
body=body,
max_results=max_results,
x_project_id=x_project_id,

    )).parsed
