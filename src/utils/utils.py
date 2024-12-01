from typing import Generic, TypeVar

from fastapi import HTTPException

T = TypeVar("T")


class Singleton(Generic[T]):
    _instance: T
    _instance = None

    @classmethod
    def get_instance(cls) -> T:
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance


class UrlMaker:
    @staticmethod
    def pg_url(
        pg_user: str, pg_password: str, pg_host: str, pg_port: str, pg_db: str
    ) -> str:
        return f"{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}"

    @staticmethod
    def sync_pg_url(
        pg_user: str, pg_password: str, pg_host: str, pg_port: str, pg_db: str
    ) -> str:
        return f"postgresql+psycopg2://{UrlMaker.pg_url(pg_user, pg_password, pg_host, pg_port, pg_db)}"

    @staticmethod
    def async_pg_url(
        pg_user: str, pg_password: str, pg_host: str, pg_port: str, pg_db: str
    ) -> str:
        return f"postgresql+asyncpg://{UrlMaker.pg_url(pg_user, pg_password, pg_host, pg_port, pg_db)}"


NotFoundException = HTTPException(404, "NotFound")
