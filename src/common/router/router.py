from fastapi import APIRouter
from sqlalchemy import Enum


class BaseRouter:
    def __init__(self, name: str) -> None:
        self._router = APIRouter(prefix=f"/{name}")
        self.register_handlers()

    def register_handlers(self) -> None:
        pass

    @property
    def router(self):
        return self._router


class HttpMethod(str, Enum):
    GET: str = "GET"
    POST: str = "POST"
    PUT: str = "PUT"
    DELETE: str = "DELETE"
