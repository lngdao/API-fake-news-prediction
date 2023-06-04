from fastapi import FastAPI, Request

from api.home.home import home_router
from api import router
import motor.motor_asyncio

def init_routers(app_: FastAPI) -> None:
  app_.include_router(home_router)
  app_.include_router(router)

def create_app() -> FastAPI:
  app_ = FastAPI(
    title="Fake News API",
    description="The API for handling fake news prediction is written in Python using the FastAPI library",
    version="1.0.0",
  )
  init_routers(app_=app_)
  return app_

app = create_app()