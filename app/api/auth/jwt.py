from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from app.services.user_services import UserService
from app.core.security import create_access_token, create_refresh_token
from app.api.dependencies.user_dependencies import get_current_user
from app.schemas.auth_schemas import TokenSchema
from app.schemas.user_schema import UserResponse
from app.models.user_model import User
from app.core.config import settings
from app.schemas.auth_schemas import TokenPayload
from pydantic import ValidationError
from jose import jwt

auth_router = APIRouter()

@auth_router.post("/login", summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(email= form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id),
    }

@auth_router.post('/test', summary="Test if the token is valid", response_model=UserResponse)
async def test_token(user: User = Depends(get_current_user)):
    return user

@auth_router.post('/refresh', summary="Get new tokens with Refresh Token", response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_token, settings.JWT_REFRESH_SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid Token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    user = await UserService.get_user_by_id(token_data.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user"
        )
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id),
    }