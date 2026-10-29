from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.body_upload_file_api_pipes_artefacts_files_upload_post import BodyUploadFileApiPipesArtefactsFilesUploadPost
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: BodyUploadFileApiPipesArtefactsFilesUploadPost,
    folder: None | str | Unset = UNSET,
    x_project_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-project-id"] = x_project_id



    

    params: dict[str, Any] = {}

    json_folder: None | str | Unset
    if isinstance(folder, Unset):
        json_folder = UNSET
    else:
        json_folder = folder
    params["folder"] = json_folder


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/pipes/artefacts/files/upload",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileApiPipesArtefactsFilesUploadPost,
    folder: None | str | Unset = UNSET,
    x_project_id: str,

) -> Response[HTTPValidationError | str]:
    """ Upload File

    Args:
        folder (None | str | Unset):
        x_project_id (str):
        body (BodyUploadFileApiPipesArtefactsFilesUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
     """


    kwargs = _get_kwargs(
        body=body,
folder=folder,
x_project_id=x_project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileApiPipesArtefactsFilesUploadPost,
    folder: None | str | Unset = UNSET,
    x_project_id: str,

) -> HTTPValidationError | str | None:
    """ Upload File

    Args:
        folder (None | str | Unset):
        x_project_id (str):
        body (BodyUploadFileApiPipesArtefactsFilesUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
     """


    return sync_detailed(
        client=client,
body=body,
folder=folder,
x_project_id=x_project_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileApiPipesArtefactsFilesUploadPost,
    folder: None | str | Unset = UNSET,
    x_project_id: str,

) -> Response[HTTPValidationError | str]:
    """ Upload File

    Args:
        folder (None | str | Unset):
        x_project_id (str):
        body (BodyUploadFileApiPipesArtefactsFilesUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | str]
     """


    kwargs = _get_kwargs(
        body=body,
folder=folder,
x_project_id=x_project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileApiPipesArtefactsFilesUploadPost,
    folder: None | str | Unset = UNSET,
    x_project_id: str,

) -> HTTPValidationError | str | None:
    """ Upload File

    Args:
        folder (None | str | Unset):
        x_project_id (str):
        body (BodyUploadFileApiPipesArtefactsFilesUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | str
     """


    return (await asyncio_detailed(
        client=client,
body=body,
folder=folder,
x_project_id=x_project_id,

    )).parsed
