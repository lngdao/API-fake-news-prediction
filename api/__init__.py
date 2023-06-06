from fastapi import APIRouter

from api.post.post import post_router
from api.user.user import user_router
from api.auth.auth import auth_router
from api.upload.upload import upload_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(post_router, prefix="/post", tags=["Post"])
router.include_router(user_router, prefix="/user", tags=["User"])
router.include_router(upload_router, prefix="/upload", tags=["Upload"])

__all__ = ["router"]