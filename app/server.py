from fastapi import FastAPI, Request
import os

from api.home.home import home_router
from api import router
from fastapi.middleware.cors import CORSMiddleware
from deta import Deta

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

deta = Deta(os.getenv("DETA_PROJECT_KEY"))

def init_routers(app_: FastAPI) -> None:
    app_.include_router(home_router)
    app_.include_router(router)


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Fake News API",
        description="The API for handling fake news prediction is written in Python using the FastAPI library",
        version="1.0.0",
    )
    app_.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # app_.mount("/public", StaticFiles(directory="public"), name="public")
    init_routers(app_=app_)
    return app_


app = create_app()
