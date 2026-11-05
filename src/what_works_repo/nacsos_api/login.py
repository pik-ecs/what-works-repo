"""`nacsos-login`: store a personal NACSOS API token.

The token is shown at the NACSOS profile page (linked per deployment). The
command validates it against /api/login/me before writing it, so a bad paste
fails there instead of mid-pipeline. Re-running with a still-valid token is a
successful no-op; pass --force to replace it. The token is stored at
~/.config/nacsos/token (chmod 600), shared by all checkouts of this user.
"""

import os
from datetime import datetime

import httpx
import typer

from what_works_repo.nacsos_api.client import (
    NacsosApiError,
    client_for_token,
    whoami,
)
from what_works_repo.nacsos_api.generated.errors import UnexpectedStatus
from what_works_repo.nacsos_api.generated.models import UserModel
from what_works_repo.settings import (
    DEFAULT_NACSOS_API_BASE_URL,
    nacsos_token,
    nacsos_token_file,
    settings,
)

app = typer.Typer(help="Configure NACSOS API access for this user.")


def _base_url() -> str:
    return (
        settings.nacsos_api.base_url
        if settings.nacsos_api is not None
        else DEFAULT_NACSOS_API_BASE_URL
    )


def _profile_url(base_url: str) -> str:
    """Web profile page hosting the token, derived from the API base URL."""
    origin = base_url.split("/nacsos-core")[0].rstrip("/")
    return f"{origin}/#/user/profile"


def _fmt_expiry(valid_till: datetime | None) -> str:
    return valid_till.strftime("%Y-%m-%d") if valid_till else "unknown date"


def _check_token(token: str, base_url: str) -> tuple[UserModel, datetime | None]:
    """Return (user, expiry), or raise NacsosApiError if the token is rejected."""
    try:
        return whoami(client_for_token(token, base_url))
    except UnexpectedStatus as error:
        raise NacsosApiError(
            f"token rejected by the server (HTTP {error.status_code})"
        ) from None
    except httpx.RequestError as error:
        raise NacsosApiError(f"could not reach {base_url}: {error}") from None


def _store_token(token: str) -> None:
    """Write the token file owner-only (0600), creating the parent dir."""
    token_file = nacsos_token_file()
    token_file.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(token_file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as handle:
        handle.write(f"{token}\n")


@app.command()
def login(
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Replace the stored token even if it is still valid.",
    ),
) -> None:
    """Log in to the NACSOS API, storing the token in ~/.config/nacsos/token."""
    base_url = _base_url()
    stored = nacsos_token()
    if stored and not force:
        try:
            user, valid_till = _check_token(stored, base_url)
        except NacsosApiError as error:
            typer.secho(
                f"Stored token rejected ({error}); paste a fresh one.",
                fg=typer.colors.YELLOW,
            )
        else:
            typer.echo(
                f"Already logged in as {user.username} "
                f"(token valid until {_fmt_expiry(valid_till)}). "
                "Nothing to do. Use --force to replace the token."
            )
            raise typer.Exit(0)

    typer.echo(f"Open {_profile_url(base_url)} and copy your API token.")
    token = typer.prompt("Token").strip().strip('"').strip("'")
    if not token:
        typer.secho("No token pasted.", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)
    try:
        user, valid_till = _check_token(token, base_url)
    except NacsosApiError as error:
        typer.secho(
            f"{error} - check you copied the whole token from the profile page.",
            fg=typer.colors.RED,
            err=True,
        )
        raise typer.Exit(1) from None
    _store_token(token)
    typer.echo(
        f"Logged in as {user.username} "
        f"(token valid until {_fmt_expiry(valid_till)}); "
        f"stored in {nacsos_token_file()}."
    )


if __name__ == "__main__":
    app()
