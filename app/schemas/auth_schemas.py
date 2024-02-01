from pydantic import BaseModel, EmailStr
from fastapi import Response
from uuid import UUID

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

def TokenSchemaResponse(data: dict, **kwargs):
    return Response(content=data, media_type="application/json")

class TokenPayload(BaseModel):
    sub: UUID = None
    exp: int = None

class EmailBody(BaseModel):
    email: EmailStr