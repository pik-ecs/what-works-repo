from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_export_label_options_api_export_project_label_options_scheme_id_get_response_get_export_label_options_api_export_project_label_options_scheme_id_get import GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet
from ...models.http_validation_error import HTTPValidationError
from typing import cast



def _get_kwargs(
    scheme_id: str,
    *,
    x_project_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-project-id"] = x_project_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/export/project/label_options/{scheme_id}".format(scheme_id=quote(str(scheme_id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scheme_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet | HTTPValidationError]:
    """ Get Export Label Options

    Args:
        scheme_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        scheme_id=scheme_id,
x_project_id=x_project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    scheme_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet | HTTPValidationError | None:
    """ Get Export Label Options

    Args:
        scheme_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet | HTTPValidationError
     """


    return sync_detailed(
        scheme_id=scheme_id,
client=client,
x_project_id=x_project_id,

    ).parsed

async def asyncio_detailed(
    scheme_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet | HTTPValidationError]:
    """ Get Export Label Options

    Args:
        scheme_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet | HTTPValidationError]
     """


    kwargs = _get_kwargs(
        scheme_id=scheme_id,
x_project_id=x_project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    scheme_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet | HTTPValidationError | None:
    """ Get Export Label Options

    Args:
        scheme_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGetResponseGetExportLabelOptionsApiExportProjectLabelOptionsSchemeIdGet | HTTPValidationError
     """


    return (await asyncio_detailed(
        scheme_id=scheme_id,
client=client,
x_project_id=x_project_id,

    )).parsed
