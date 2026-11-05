from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.import_revision_details import ImportRevisionDetails
from typing import cast



def _get_kwargs(
    import_id: str,
    *,
    x_project_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-project-id"] = x_project_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/imports/import/{import_id}/revisions".format(import_id=quote(str(import_id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | list[ImportRevisionDetails] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ImportRevisionDetails.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError | list[ImportRevisionDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    import_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[HTTPValidationError | list[ImportRevisionDetails]]:
    """ Get Import Revisions

    Args:
        import_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ImportRevisionDetails]]
     """


    kwargs = _get_kwargs(
        import_id=import_id,
x_project_id=x_project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    import_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> HTTPValidationError | list[ImportRevisionDetails] | None:
    """ Get Import Revisions

    Args:
        import_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ImportRevisionDetails]
     """


    return sync_detailed(
        import_id=import_id,
client=client,
x_project_id=x_project_id,

    ).parsed

async def asyncio_detailed(
    import_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> Response[HTTPValidationError | list[ImportRevisionDetails]]:
    """ Get Import Revisions

    Args:
        import_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ImportRevisionDetails]]
     """


    kwargs = _get_kwargs(
        import_id=import_id,
x_project_id=x_project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    import_id: str,
    *,
    client: AuthenticatedClient,
    x_project_id: str,

) -> HTTPValidationError | list[ImportRevisionDetails] | None:
    """ Get Import Revisions

    Args:
        import_id (str):
        x_project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ImportRevisionDetails]
     """


    return (await asyncio_detailed(
        import_id=import_id,
client=client,
x_project_id=x_project_id,

    )).parsed
