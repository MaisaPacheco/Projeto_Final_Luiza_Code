from ast import Return
from pickle import STACK_GLOBAL
from telnetlib import STATUS
from winreg import ExpandEnvironmentStrings
from xml.dom.minidom import Identified
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from src.models import user
from bson.objectid import ObjectId

from src.models.user import *
from src.schemas.user import UserSchema, UserUpdate
    

router = APIRouter()

# pegar usuarios
@router.get("/")
async def route_get_user(requests: Request):
   return await get_users(requests.app.database["users"],0,2)

#criar um usuário
@router.post("/", status_code=status.HTTP_201_CREATED)
async def route_create_user(requests: Request, new_user:UserSchema = Body(...)):
    new_user = jsonable_encoder(new_user)
    teste = await create_user(requests.app.database["users"], new_user)
    return teste

# Retornar um usuário pelo id
@router.get("/{id}", response_description = "Get a user by id")
async def route_get_by_id(id: str, request: Request):
     if (get_user := await request.app.database["users"].find_one({"_id": ObjectId(id)})):
         return  get_user
       
    
 
    
    # return await get_user(requests.app.database["_id"])
    
    # print(ObjectId)
    # object_id = ObjectId(id)
    # return await get_user(request.app.database["users"], object_id)

    #if (get_user := request.app.database["users"].find_one({'_id': ObjectId(id)})):
        


    # return await get_user(request.app.database["users"], id)
    
   
    

#raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f" user with ID {id} not found")

    # if (get_user := request.app.database["users"].find_one({"_id": id})):
    #     return get_user
    # print(get_user)
    
 
    # return await get_user(requests.app.database["_id"])

#atualizar um usuário
@router.put("/{id}", response_description="Update a user", response_model=UserSchema)
async def route_update_user(id:str, request: Request, user: UserUpdate = Body(...)):
    user = {k: v for k, v in user.dict().items() if v is not None}
    
    if len(user) > 1:
        update_result = request.app.database["users"].update_one(
            {"_id": id}, {"$set": user}
        )
    if update_result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"user with {id} not found")
    
    if (
        existing_user := request.app.database["users"].find_one({"_id": id})
    ) is not None:
        return existing_user
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with ID {id} not found")

#deletar um usuário
@router.delete("/{id}", response_description="delete a user")
async def delete_user(id: str, request: Request, response: Response):
    delete_result = request.app.database["users"].delete_one({"_id": id})
    
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"user with id {id} not found")
    
