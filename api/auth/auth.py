from fastapi import APIRouter, Depends

from app.auth.service.auth import AuthService
import helper
from security import permission
from pydantic import BaseModel

auth_router = APIRouter()


class RegisterRequest(BaseModel):
    username: str
    password: str
    name: str


class LoginRequest(BaseModel):
    username: str
    password: str


@auth_router.post("/register")
async def register(request_data: RegisterRequest):
    data = await AuthService().register(request_data)
    return helper.transformData(data)


@auth_router.post("/login")
async def login(request_data: LoginRequest):
    data = await AuthService().login(request_data)
    return helper.transformData(data)
