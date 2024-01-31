from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from uuid import UUID

class TaskCreate(BaseModel):
    title: str = Field(..., title = "Title", min_length=3, max_length=50)
    description: str = Field(..., title="Description", min_length=5, max_length=5000)
    status: Optional[bool] = False
    task_date: Optional[date] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(..., title = "Title", min_length=3, max_length=50)
    description: Optional[str] = Field(..., title="Description", min_length=5, max_length=5000)
    status: Optional[bool] = False
    task_date: Optional[date] = None

class TaskResponse(BaseModel):
    task_id: UUID
    status: bool
    title: str
    description: str
    task_date: Optional[date] = None
    created_at: datetime
    updated_at: datetime
