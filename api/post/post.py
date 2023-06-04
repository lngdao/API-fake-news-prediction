from fastapi import APIRouter

from app.post.service.post import PostService

post_router = APIRouter()

@post_router.get('')
async def get_post_list():
  return await PostService().get_post_list()