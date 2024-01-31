import certifi
from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.user_model import User
from app.models.task_model import Task
from app.api.router import router

app = FastAPI(
    title = settings.PROJECT_NAME,
    openapi_url=f"{settings.API}/openapi.json",
)

async def initialize_database():
    """
        Initialize crucial app services
    """
    db_client = AsyncIOMotorClient(settings.MONGO_URI, tlsCAFile=certifi.where())
    db_name = db_client["tasklist"]
    await init_beanie(
        database=db_name,
        document_models=[
            User,
            Task
        ]
    )

app.include_router(router, prefix=settings.API)

@app.on_event("startup")
async def start_application():
    await initialize_database()
