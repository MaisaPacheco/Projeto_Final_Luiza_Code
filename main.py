from src.controllers.user_routes import router as user_route
from fastapi import FastAPI, Request
from os import environ
from pymongo import MongoClient


config = environ.get(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(environ.get("DATABASE_URI"))
    app.database = app.mongodb_client[str(environ.get("DB_NAME"))]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(user_route, tags=["users"], prefix="/users")

# @app.get("/")
# def teste_get(request: Request):
#     return "OK"

# import asyncio

# from src.controllers.users import users_crud
# # from src.controllers.products import products_crud
# # rom src.controllers.carrinho import carrinho_crud

# loop = asyncio.get_event_loop()
# loop.run_until_complete(users_crud())
