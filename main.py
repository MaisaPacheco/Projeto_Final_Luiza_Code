from itertools import product
from src.controllers.user_routes_async import router as user_route
from src.controllers.routes_products_async import router as product_route
from src.controllers.routes_address_async import router as address_route
from src.controllers.routes_order_async import router as order_route
from src.controllers.routes_order_item_async import router as order_item_route
from fastapi import FastAPI, Request
from os import environ
from pymongo import MongoClient
from src.server.database import connect_db, db, disconnect_db

config = environ.get(".env")

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    await connect_db()
    app.database = db
    # app.mongodb_client = MongoClient(environ.get("DATABASE_URI"))
    # app.database = app.mongodb_client[str(environ.get("DB_NAME"))]

@app.on_event("shutdown")
async def shutdown_db_client():
    await disconnect_db()
    # app.mongodb_client.close()

app.include_router(user_route, tags=["users"], prefix="/users")
app.include_router(product_route, tags=["products"], prefix="/products")
app.include_router(address_route, tags=["address"], prefix="/address")
app.include_router(order_route, tags=["cart"], prefix="/cart")
app.include_router(order_item_route, tags=["cart_item"], prefix="/cart_item")


# @app.get("/")
# def teste_get(request: Request):
#     return "OK"

# import asyncio

# from src.controllers.users import users_crud
# # from src.controllers.products import products_crud
# # rom src.controllers.carrinho import carrinho_crud

# loop = asyncio.get_event_loop()
# loop.run_until_complete(users_crud())
