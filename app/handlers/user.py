from fastapi import APIRouter, HTTPException, status
from app.schemas.user_schema import UserAuth, UserResponse
from app.services.user_services import UserService
from pymongo.errors import DuplicateKeyError

user_router = APIRouter()

@user_router.post('/register', summary="Register new user.", response_model=UserResponse)
async def register_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this mail already exists"
        )