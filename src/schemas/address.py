from typing import List
from pydantic import BaseModel, Field
from bson import ObjectId
from bson.objectid import ObjectId

from src.schemas.user import UserSchema


class Address(BaseModel):
    street: str
    zipcode: str
    district: str
    city: str
    state: str
    is_delivery: bool = Field(default=True)
    


class AddressSchema(BaseModel):
    user: UserSchema
    address: List[Address] = []
    
class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                  "user": {
                        "name": "iron Man",
                        "email": "ironMan@starkavengers.com",
                        "password": "hero123!",
                        "is_active": True,
                        "is_admin": False
                    },
                    "address" : [
                        {
                            "street": "i dont know",
                            "zipcode": "9999-030",
                            "district": "Grass Lands",
                            "city": "stark tower",
                            "state": "Parallel Universe", 
                            "is_delivery": True
                        }, 
                        {
                            "street": "testing",
                            "zipcode": "01020-040",
                            "district": "testing ",
                            "city": "example testing",
                            "state": "Parallel Universe", 
                            "is_delivery": False
                        }
                      ]
            }
        }
