from typing import Any, Callable, Protocol
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_events.middleware import EventHandlerASGIMiddleware
from fastapi_events.handlers.local import local_handler
import uvicorn

from common.config import AppConfig
from common.events import handle_user_action  # noqa
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
        self._app.add_middleware(EventHandlerASGIMiddleware, handlers=[local_handler])
        uvicorn.run(self._app, host=self._host, port=self._port)

    def include_router(self, router: BaseRouter) -> None:
        self._app.include_router(router.router)
