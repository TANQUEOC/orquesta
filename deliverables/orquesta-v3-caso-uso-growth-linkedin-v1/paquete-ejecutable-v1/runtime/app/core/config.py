from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "orquesta-linkedin-growth-campaign"
    app_env: str = "development"
    host: str = "0.0.0.0"
    port: int = 8010
    default_language: str = "es"
    default_timezone: str = "Europe/Madrid"
    default_channel: str = "linkedin"
    supabase_url: str = "https://rxuknfjovwvqrlxzyxye.supabase.co"
    supabase_service_role_key: str = ""
    linkedin_approval_required: bool = True
    cors_origins: list[str] = Field(default_factory=lambda: ["*"])
    runtime_public_base_url: str = "http://127.0.0.1:8010"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)


settings = Settings()
