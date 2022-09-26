from pydantic import BaseModel, Field
from bson import ObjectId
from bson.objectid import ObjectId
from src.utils.pydantic_objectId import PyObjectId


class ProductSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(max_length=100)
    description: str
    price: float
    image: str
    code: int 

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Book Alice in the wonderland",
                "description": "It details the story of a young girl named Alice who falls through a rabbit hole into a fantasy world of anthropomorphic creatures",
                "price": 569.9,
                "image": "http://127.0.0.1:8000/produto/aliceinthewordeland.png",
                "code": 123456789
            }
        }