from app.schemas.user_schema import UserAuth
from app.models.user_model import User
from app.core.security import get_password, verify_password
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException, status
from typing import Optional
from uuid import UUID

class UserService:
    @staticmethod
    async def create_user(user:UserAuth):
        user_in = User(
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            hashed_password=get_password(user.password)
        )
        try:
            await user_in.insert()
        except DuplicateKeyError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this mail already exists"
            )
        return user_in
    
    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(password=password, hashed_password=user.hashed_password):
            return None
        return user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user
    
    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[User]:
        user = await User.find_one(User.user_id == id)
        return user