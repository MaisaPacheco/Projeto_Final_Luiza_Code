from fastapi import APIRouter, Body, Request, status
from fastapi.encoders import jsonable_encoder
from typing import List
from bson.objectid import ObjectId

from src.models.user import (
    get_user,
    get_users,
    create_user,
    delete_user
)
from src.schemas.user import UserSchema


router = APIRouter()

# pegar usuarios


@router.get("/", response_model=List[UserSchema])
async def route_get_user(requests: Request):
    return await get_users(requests.app.database.users_collection, 0, 2)

# criar um usuário


@router.post("/", status_code=status.HTTP_201_CREATED)
async def route_create_user(requests: Request, new_user: UserSchema = Body(...)):
    new_user = jsonable_encoder(new_user)
    teste = await create_user(requests.app.database.users_collection, new_user)
    return teste

# Retornar um usuário pelo id


@router.get("/{id}",
            response_description="Get a user by id",
            response_model=UserSchema)
async def route_get_by_id(id: str, request: Request):
    return await get_user(request.app.database.users_collection, ObjectId(str(id)))

# deletar um usuário


@router.delete("/{id}", response_description="delete a user")
async def route_delete_user(id: str, requests: Request):
    return await delete_user(requests.app.database.users_collection, ObjectId(str(id)))
