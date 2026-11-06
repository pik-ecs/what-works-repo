import os
from pathlib import Path

import numpy as np
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict, YamlConfigSettingsSource


class NacsosSettings(BaseModel):
    project_id: str
    scheme_id: str
    import_id: str
    inclusion_key: str
    comment_key: str | None = None
    deet_check_users: list[str] = Field(
        default_factory=list,
        description=(
            "User Ids of humans who check DEET predicted positives."
            " Leave empty to skip verification of positives."
        ),
    )
    deet_user_id: str
    deet_username: str


DEFAULT_NACSOS_API_BASE_URL = "https://nacsos.pik-potsdam.de/nacsos-core"


def nacsos_token_file() -> Path:
    """Per-user token file written by `nacsos-login`."""
    config_home = Path(os.environ.get("XDG_CONFIG_HOME", "~/.config")).expanduser()
    return config_home / "nacsos" / "token"


def nacsos_token() -> str | None:
    """Resolve the API token: env var, then the per-user token file."""
    if settings.nacsos_api and settings.nacsos_api.api_token:
        return settings.nacsos_api.api_token
    token_file = nacsos_token_file()
    if token_file.is_file():
        return token_file.read_text().strip() or None
    return None


class NacsosApiSettings(BaseModel):
    """Settings for the nacsos-core REST API (base_url from config/snakemake.yaml).

    The personal token comes from `nacsos_token()`: the NACSOS_API__API_TOKEN
    env var, else the file written by `uv run nacsos-login`.
    NACSOS_API__API_USERNAME/PASSWORD env vars additionally enable auto-renewal
    on expiry, for unattended runs.
    """

    base_url: str = DEFAULT_NACSOS_API_BASE_URL
    api_token: str | None = None
    api_username: str | None = None
    api_password: str | None = None
    timeout_seconds: int = 600


class TransformerModel(BaseModel):
    name: str
    label: str
    threshold: float


class MLSettings(BaseModel):
    train_model: bool
    pretrained_models: list[TransformerModel]
    triage_predictions: bool = False
    prediction_precision: int = 4

    def _prediction_storage(self) -> tuple[int, np.dtype]:
        """
        Return a multiplier and data type given the number of decimal places required.
        """
        multiplier = 10**self.prediction_precision
        if multiplier <= 255:
            return multiplier, np.dtype("uint8")
        elif multiplier <= 65535:
            return multiplier, np.dtype("uint16")
        else:
            return 1, np.dtype("float32")

    @property
    def pred_multiplier(self) -> int:
        return self._prediction_storage()[0]

    @property
    def pred_dtype(self) -> np.dtype:
        return self._prediction_storage()[1]


class DeetEvalSettings(BaseModel):
    megabatch_start: int
    megabatch_end: int


class Settings(BaseSettings):
    """Settings for the what works repo."""

    model_config = SettingsConfigDict(env_nested_delimiter="__", extra="ignore")

    ts01_username: str = Field(default_factory=lambda: os.getenv("USER", ""))

    nacsos: NacsosSettings
    nacsos_api: NacsosApiSettings | None = None
    ml: MLSettings
    sample_size: int = 20000

    deet_eval: DeetEvalSettings

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (
            env_settings,
            YamlConfigSettingsSource(settings_cls, yaml_file="config/snakemake.yaml"),
        )


settings = Settings()
