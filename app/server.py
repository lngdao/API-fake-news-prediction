from fastapi import FastAPI, Request

from api.home.home import home_router
from api import router
# from pydantic import BaseModel

# class New(BaseModel):
#     title: str
#     description: str

# app = FastAPI()

# @app.get('/')
# async def root():
#   return "API fake-news"

#  get all
#  get one
#  update one
#  delete one
#  insert one
#  check

# @app.post('/news')
# async def getNews(new: New):
#   # check xem co phai fake new khong
#   return {"isFake": True, "data": {"title": "", "description": ""}}

def init_routers(app_: FastAPI) -> None:
  app_.include_router(home_router)
  app_.include_router(router)
  pass

def create_app() -> FastAPI:
  app_ = FastAPI(
    title="Fake News API",
    description="Fake News API",
    version="1.0.0",
  )
  init_routers(app_=app_)
  return app_

app = create_app()