from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
from src.models.order import create_cart, delete_cart, get_cart
from src.models.order_item import create_cart_item
from src.schemas.order import OrderSchema
from src.schemas.order_item import OrderItemSchema
from src.schemas.product import ProductSchema
from src.models.user import get_user
from bson.objectid import ObjectId
from fastapi import APIRouter, Request, Response, Body, HTTPException, status


router = APIRouter()

@router.post("/{cart_item_id}", status_code=status.HTTP_201_CREATED, response_model=OrderItemSchema)
async def route_create_cart_item(cart_item_id: str, request: Request, new_product: ProductSchema = Body(...) ):
    new_product = jsonable_encoder(new_product) 
    data = await create_cart_item(request.app.database.order_collection, 
                            request.app.database.order_items_collection,
                            ObjectId(str(cart_item_id)), new_product)
    return data