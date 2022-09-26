from pydantic import BaseModel

from src.schemas.order import OrderSchema
from src.schemas.product import ProductSchema
from bson.objectid import ObjectId


class OrderItemSchema(BaseModel):
    order: OrderSchema
    product: ProductSchema
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True  # required for the _id
        json_encoders = {ObjectId: str}
