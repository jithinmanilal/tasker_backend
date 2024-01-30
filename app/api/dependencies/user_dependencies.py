from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from app.models.user_model import User
from app.schemas.auth_schemas import TokenPayload
from jose import jwt
from pydantic import ValidationError
from datetime import datetime

reusable_oauth = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API}/auth/login",
    scheme_name="JWT"
)

async def get_current_user(token: str = Depends(reusable_oauth)) -> User:
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp < datetime.now()):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError)
