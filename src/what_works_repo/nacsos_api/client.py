"""Auth layer around the generated nacsos-core client.

Core stores one token row per user in `auth_tokens`; the token string survives
re-login, `valid_till` expiry is the only failure mode. A 401 triggers one re-login
(POST /api/login/token) and a replay, so runs longer than the token lifetime
(8 days by default) continue without intervention. Re-login requires the
NACSOS_API__API_USERNAME/PASSWORD env vars.
"""

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from typing import Any

import httpx

from what_works_repo.nacsos_api.generated.api.oauth.read_tokens_me_api_login_my_tokens_get import (  # noqa: E501
    sync as read_my_tokens,
)
from what_works_repo.nacsos_api.generated.api.oauth.read_users_me_api_login_me_get import (  # noqa: E501
    sync as read_users_me,
)
from what_works_repo.nacsos_api.generated.client import AuthenticatedClient
from what_works_repo.nacsos_api.generated.errors import UnexpectedStatus
from what_works_repo.nacsos_api.generated.models import (
    HTTPValidationError,
    UserModel,
)
from what_works_repo.settings import (
    DEFAULT_NACSOS_API_BASE_URL,
    nacsos_token,
    settings,
)


class NacsosApiError(RuntimeError):
    """A nacsos-core API call failed; the message carries status and response text."""


@dataclass
class _AuthState:
    base_url: str
    token: str
    username: str | None = None
    password: str | None = None

    @property
    def auth_header(self) -> str:
        return f"Bearer {self.token}"

    def relogin(self) -> None:
        if not self.username or not self.password:
            raise NacsosApiError(
                "nacsos token rejected - run `uv run nacsos-login` to store a "
                "fresh one (token shown at the NACSOS profile page), or set "
                "NACSOS_API__API_USERNAME/PASSWORD for auto-renewal"
            )
        with httpx.Client(base_url=self.base_url) as client:
            response = client.post(
                "/api/login/token",
                data={"username": self.username, "password": self.password},
            )
        if response.status_code != 200:
            raise NacsosApiError(
                f"nacsos re-login failed ({response.status_code}): "
                f"{response.text[:300]}"
            )
        self.token = response.json()["token_id"]


class _TokenRefreshTransport(httpx.BaseTransport):
    """Signs requests with the current token; on 401, re-logs in once and replays."""

    def __init__(self, state: _AuthState) -> None:
        self._state = state
        self._inner = httpx.HTTPTransport()

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        request.headers["Authorization"] = self._state.auth_header
        response = self._inner.handle_request(request)
        if response.status_code == 401:
            response.close()
            self._state.relogin()
            request.headers["Authorization"] = self._state.auth_header
            response = self._inner.handle_request(request)
        return response


_client: AuthenticatedClient | None = None


def get_client() -> AuthenticatedClient:
    global _client
    if _client is None:
        token = nacsos_token()
        if not token:
            raise NacsosApiError(
                "No nacsos API token configured - run `uv run nacsos-login`"
            )
        config = settings.nacsos_api
        state = _AuthState(
            base_url=config.base_url if config else DEFAULT_NACSOS_API_BASE_URL,
            username=config.api_username if config else None,
            password=config.api_password if config else None,
            token=token,
        )
        _client = AuthenticatedClient(
            base_url=state.base_url,
            token=token,
            timeout=httpx.Timeout(config.timeout_seconds if config else 600),
            raise_on_unexpected_status=True,
            httpx_args={"transport": _TokenRefreshTransport(state)},
        )
    return _client


def client_for_token(token: str, base_url: str | None = None) -> AuthenticatedClient:
    """Plain authenticated client for one token, no refresh transport.

    For validating a token before it is stored (nacsos-login).
    """
    if base_url is None:
        base_url = (
            settings.nacsos_api.base_url
            if settings.nacsos_api is not None
            else DEFAULT_NACSOS_API_BASE_URL
        )
    return AuthenticatedClient(
        base_url=base_url,
        token=token,
        timeout=httpx.Timeout(30),
        raise_on_unexpected_status=True,
    )


def whoami(client: AuthenticatedClient) -> tuple[UserModel, datetime | None]:
    """Identify the token's user and its expiry.

    Raises UnexpectedStatus (e.g. 401) when the token is missing or rejected.
    """
    user = read_users_me(client=client)
    if user is None:
        raise NacsosApiError("nacsos /api/login/me returned an empty body")
    valid_till = next(
        (
            token.valid_till
            for token in (read_my_tokens(client=client) or [])
            if str(token.token_id) == client.token
        ),
        None,
    )
    if not isinstance(valid_till, datetime):
        valid_till = None
    return user, valid_till


def call(endpoint: Callable[..., Any], **kwargs: Any) -> Any:
    """Invoke a generated endpoint function with the project header.

    Maps unexpected statuses and validation errors to NacsosApiError.
    """
    try:
        response = endpoint(
            client=get_client(), x_project_id=settings.nacsos.project_id, **kwargs
        )
    except UnexpectedStatus as error:
        raise NacsosApiError(
            f"nacsos API unexpected status {error.status_code}: "
            f"{error.content.decode(errors='ignore')[:500]}"
        ) from None
    if isinstance(response, HTTPValidationError):
        raise NacsosApiError(f"nacsos API validation error: {response.to_dict()}")
    return response
