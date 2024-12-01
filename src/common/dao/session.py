from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from common.config.config import PostgresConfig
from utils.utils import Singleton, UrlMaker


class PostgresSession(Singleton):
    def __init__(self):
        config = PostgresConfig.get_instance()
        self._async_session = async_sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=create_async_engine(
                echo=True,
                url=UrlMaker.async_pg_url(
                    config.POSTGRES_USER,
                    config.POSTGRES_PASSWORD,
                    config.POSTGRES_HOST,
                    config.POSTGRES_PORT,
                    config.POSTGRES_DB,
                ),
            ),
        )()

    def get_async(self) -> AsyncSession:
        return self._async_session
