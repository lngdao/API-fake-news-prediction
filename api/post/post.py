from fastapi import APIRouter, Depends

from app.post.service.post import PostService
from security import permission
import helper
from pydantic import BaseModel

post_router = APIRouter()


class CreatePostRequest(BaseModel):
    title: str
    description: str
    content: str
    image: str


class PredictionRequest(BaseModel):
    content: str


@post_router.get("")
async def get_post_list():
    posts = await PostService().get_post_list()
    return helper.transformData(posts)


@post_router.get("/{post_id}")
async def get_post_detail(
    post_id: str, token_data=Depends(permission.is_authenticated)
):
    post = await PostService().get_post_detail(post_id)
    return helper.transformData(post)


@post_router.post("")
async def create_post(
    req_data: CreatePostRequest, token_data=Depends(permission.is_admin)
):
    post = await PostService().create_post(req_data)
    return helper.transformData(post)


@post_router.post("/prediction")
async def prediction_post_content(
    req_data: PredictionRequest, token_data=Depends(permission.is_admin)
):
    status = await PostService().prediction_post_content(req_data)
    return helper.transformData(status)


@post_router.delete("/{post_id}")
async def prediction_post_content(
    post_id: str, token_data=Depends(permission.is_admin)
):
    post = await PostService().delete_post(post_id)
    return helper.transformData(post)
