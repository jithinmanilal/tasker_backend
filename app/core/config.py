from typing import List
from pydantic.v1 import BaseSettings, AnyHttpUrl
from decouple import config


class Settings(BaseSettings):
    API: str = "/api"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Task"

    MONGO_URI: str = config("MONGO_URI", cast=str)

    class Config:
        case_sensitive = True

settings = Settings()
