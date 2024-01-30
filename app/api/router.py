from fastapi import APIRouter
from app.handlers.user import user_router
from app.api.auth.jwt import auth_router

router = APIRouter()
router.include_router(user_router, prefix='/users', tags=["users"])
router.include_router(auth_router, prefix='/auth', tags=["auth"])

