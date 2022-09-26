import collections
from bson.objectid import ObjectId
from fastapi import APIRouter, Request, Response, Body, HTTPException, status
from src.schemas.address import AddressSchema, Address
from fastapi.encoders import jsonable_encoder
from typing import List
from src.models.address import create_address
from src.models.address import *

router = APIRouter()



@router.put("/{user_id}", response_description="create a new address", status_code=status.HTTP_201_CREATED, response_model= List[Address])
async def route_address(user_id: str, request:Request, new_address: List[Address] = Body(...)):
    new_address = list(map(lambda end: jsonable_encoder(end), new_address))
    data_address = await create_address(request.app.database.address_collection,
                                        request.app.database.users_collection,
                                        ObjectId(str(user_id)), new_address)
    return data_address