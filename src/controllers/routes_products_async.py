from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Request, Body, status

from src.models.product import create_product, delete_product, get_product
from src.schemas.product import ProductSchema


router = APIRouter()


# create product

@router.post("/", response_description="Create a new product", status_code=status.HTTP_201_CREATED,
             response_model=ProductSchema)
async def route_post_product(requests: Request, new_product: ProductSchema = Body(...)):
    new_product = jsonable_encoder(new_product)
    creating = await create_product(requests.app.database.product_collection, new_product)
    return creating

# delete product by id


@router.delete("/{id}", response_description="Delete a product")
async def route_delete_product(id: str, request: Request):
    return await delete_product(request.app.database.product_collection, id)


# get product by id
@router.get("/{id}", response_model=ProductSchema)
async def route_get_product_by_id(id: str, request: Request):
    return await get_product(request.app.database.product_collection, id)