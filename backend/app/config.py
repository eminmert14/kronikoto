from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Geliştirmede SQLite (kurulum gerektirmez), prod/Docker'da PostgreSQL:
    # postgresql+psycopg://kronikoto:kronikoto@localhost:5432/kronikoto
    database_url: str = "sqlite:///./kronikoto.db"
    cors_origins: str = "http://localhost:3000,https://kronikoto.vercel.app,*"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
