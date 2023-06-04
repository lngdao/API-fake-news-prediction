from fastapi import APIRouter

from api.post.post import post_router

router = APIRouter()
router.include_router(post_router, prefix="/post", tags=["Post"])

__all__ = ["router"]