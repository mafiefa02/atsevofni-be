from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Atsevofni Backend"
    app_health_check_route: str = "/health"
    default_item_per_page: int = 50
    api_key_header_name: str = "X-ATSEVOFNI-KEY"
    api_key: str
    cors_origins: list[str] = ["http://localhost:5173"]

    model_config = SettingsConfigDict(env_file=".env.local")


settings = Settings()
