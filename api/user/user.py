from fastapi import APIRouter, Depends

from app.user.service.user import UserService
import helper
from security import permission

user_router = APIRouter()

@user_router.get('')
async def get_profile(token_data = Depends(permission.is_authenticated)):
  idetifier = token_data.sub
  profile = await UserService().get_profile(idetifier)
  return helper.transformData(profile)