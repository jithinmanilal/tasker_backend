from beanie import Document, Indexed, Link, before_event, Replace, Insert
from uuid import UUID, uuid4
from pydantic import Field, EmailStr
from datetime import datetime, date
from typing import Optional
from .user_model import User


class Task(Document):
    task_id: UUID = Field(default_factory=uuid4)
    status: bool = False
    title: Indexed(str)
    description: str
    task_date: Optional[date] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]

    def __repr__(self) -> str:
        return f"<Task {self.title}>"
    
    def __str__(self) -> str:
        return self.title
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Task):
            return self.task_id == other.task_id
        return False
    
    @before_event([Replace, Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Settings:
        name = "tasks"