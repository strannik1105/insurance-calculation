from typing import Any, Callable, Protocol
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from common.config import Config
from utils import Singleton


class AbstractApp(Protocol):
    def run(self) -> None:
        pass

    def add_route(self, path: str, route_handler: Callable[..., Any]) -> None:
        pass


class App(Singleton[AbstractApp]):
    def __init__(self):
        config = Config().get_instance()

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

    def add_route(self, path: str, route_handler: Callable[..., Any]) -> None:
        self._app.add_api_route(path, route_handler)
