from src.models.order import create_cart, delete_cart
from src.schemas.order import OrderSchema
from bson.objectid import ObjectId
from fastapi import APIRouter, Request, status

router = APIRouter()


@router.post("/{user_id}",
             status_code=status.HTTP_201_CREATED,
             response_model=OrderSchema)
async def route_create_cart(user_id: str, request: Request):
    data = await create_cart(request.app.database.order_collection,
                             request.app.database.users_collection,
                             request.app.database.address_collection,
                             ObjectId(str(user_id)))
    return data


@router.delete("/{cart_id}")
async def route_delete_cart(cart_id: str, request: Request):
    return await delete_cart(request.app.database.order_collection, ObjectId(cart_id))
