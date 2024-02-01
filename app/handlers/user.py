from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user_schema import UserAuth, UserResponse
from app.models.user_model import User
from app.services.user_services import UserService
from app.api.dependencies.user_dependencies import get_current_user
from pymongo.errors import DuplicateKeyError

user_router = APIRouter()

@user_router.post('/register', summary="Register new user", response_model=UserResponse)
async def register_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this mail already exists"
        )
    
@user_router.get("/me", summary="Test if the token is valid", response_model=UserResponse)
async def test_token(current_user: User = Depends(get_current_user)):
    return current_user