from fastapi import FastAPI
from .routers import user


user_app = FastAPI()
user_app.include_router(user.router, prefix="/user", tags=["user"])