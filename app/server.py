from fastapi import FastAPI, Request

from api.home.home import home_router
from api import router

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