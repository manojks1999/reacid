from typing import Any, Dict, List, Optional
from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    # Backend Server Settings
    BACKEND_SERVER_HOST: str
    BACKEND_SERVER_PORT: int
    BACKEND_SERVER_WORKERS: int

    # PostgreSQL Database Settings
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_SCHEMA: str
    DB_MAX_POOL_CON: int
    DB_POOL_SIZE: int
    DB_POOL_OVERFLOW: int
    DB_TIMEOUT: int
    IS_DB_ECHO_LOG: bool
    IS_DB_FORCE_ROLLBACK: bool
    IS_DB_EXPIRE_ON_COMMIT: bool

    # JWT and Authentication Settings
    API_TOKEN: str
    AUTH_TOKEN: str
    JWT_TOKEN_PREFIX: str
    JWT_SECRET_KEY: str
    JWT_SUBJECT: str
    JWT_MIN: int
    JWT_HOUR: int
    JWT_DAY: int
    IS_ALLOWED_CREDENTIALS: bool

    # Hashing and Security Settings
    HASHING_ALGORITHM_LAYER_1: str
    HASHING_ALGORITHM_LAYER_2: str
    HASHING_SALT: str
    JWT_ALGORITHM: str

    # Database URL
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USERNAME}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()