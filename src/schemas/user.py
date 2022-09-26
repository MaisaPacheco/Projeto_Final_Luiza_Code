from typing import Optional
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from bson.objectid import ObjectId
from src.utils.pydantic_objectId import PyObjectId


class UserSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr = Field(unique=True, index=True)
    password: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)
    
    def __str__(self) -> str:
        return str(self.id)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True  # required for the _id
        json_encoders = {ObjectId: str}

class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str]