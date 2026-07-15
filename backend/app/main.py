from fastapi import FastAPI

app = FastAPI()

# uvicorn app.main:app --reload

from app.auth_routes import auth_router
from app.order_routes import order_router

# roteamento das rotas
app.include_router(auth_router)
app.include_router(order_router)