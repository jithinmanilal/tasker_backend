from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    password: str = Field(..., min_length=8, max_length=24, description="user password")
    first_name: str = Field(..., min_length=3, max_length=24, description="user first name")
    last_name: str = Field(..., min_length=3, max_length=24, description="user last name")


class UserResponse(BaseModel):
    user_id: UUID
    email: EmailStr
    first_name: str
    last_name: str
    disabled: Optional[bool] = False
    