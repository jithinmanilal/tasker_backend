from typing import List
from pydantic.v1 import BaseSettings, AnyHttpUrl, EmailStr
from decouple import config
from fastapi_mail import ConnectionConfig, FastMail

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

    MAIL_USERNAME: str = config("MAIL_USERNAME", cast=str)
    MAIL_PASSWORD: str = config("MAIL_PASSWORD", cast=str)
    MAIL_FROM: EmailStr = config("MAIL_FROM", cast=EmailStr)
    MAIL_PORT: int = config("MAIL_PORT", default=587, cast=int)
    MAIL_SERVER: str = config("MAIL_SERVER", cast=str)

    class Config:
        case_sensitive = True

settings = Settings()

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)