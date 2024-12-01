from typing import Any, Callable, Protocol
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from common.config import AppConfig
from common.router import BaseRouter
from utils import Singleton


class AbstractApp(Protocol):
    def run(self) -> None:
        pass

    def add_route(self, path: str, route_handler: Callable[..., Any]) -> None:
        pass


class App(Singleton[AbstractApp]):
    def __init__(self):
        config = AppConfig().get_instance()

        self._app = FastAPI()
        self._host = config.HOST
        self._port = config.PORT

    def run(self) -> None:
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        uvicorn.run(self._app, host=self._host, port=self._port)

    def include_router(self, router: BaseRouter) -> None:
        self._app.include_router(router.router)
