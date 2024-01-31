from fastapi import APIRouter
from app.handlers.user import user_router
from app.handlers.task import task_router
from app.api.auth.jwt import auth_router

router = APIRouter()
router.include_router(user_router, prefix='/users', tags=["users"])
router.include_router(task_router, prefix='/task', tags=["task"])
router.include_router(auth_router, prefix='/auth', tags=["auth"])
