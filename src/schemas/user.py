from typing import Optional
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from src.utils.pydantic_objectId import PyObjectId


class UserSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr = Field(unique=True, index=True)
    password: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)

class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]