from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.dao.session import PostgresSession


PgSession = Annotated[AsyncSession, Depends(PostgresSession.get_instance().get_async)]
