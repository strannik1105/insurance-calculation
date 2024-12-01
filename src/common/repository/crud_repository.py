from typing import Generic, Type, TypeVar, Any
from sqlalchemy import select, update
from uuid import UUID

from common.dao import PostgresSession
from common.model import AbstractModel

T = TypeVar("T", bound=AbstractModel)


class CrudRepository(Generic[T]):
    def __init__(self, session: PostgresSession, model: Type[T]) -> None:
        self._session = session
        self._model = model

    async def get_all(self, limit: int = 100, offset: int = 0) -> list[T]:
        objs = await self._session.get_async().execute(
            select(self._model).limit(limit).offset(offset)
        )
        return list(objs.scalars().all())

    async def get(self, sid: UUID) -> T | None:
        obj = await self._session.get_async().execute(
            select(self._model).where(self._model.sid == sid)
        )
        return obj.scalar_one_or_none()

    async def create(self, obj: dict[str, Any], with_commit: bool = True) -> T | None:
        model_obj = self._model(**dict(obj))
        self._session.get_async().add(model_obj)
        await self._commit_or_flush(model_obj, with_commit)
        return model_obj

    async def update(
        self,
        obj: T,
        changes: dict[str, Any],
        sid: UUID,
        with_commit: bool = True,
    ):
        await self._session.get_async().execute(
            update(self._model).where(self._model.sid == sid).values(changes)
        )
        await self._commit_or_flush(obj, with_commit)
        return obj

    async def delete(self, obj, with_commit: bool = True):
        await self._session.get_async().delete(obj)

    async def _commit_or_flush(self, obj: T, with_commit: bool):
        if with_commit:
            await self._session.get_async().commit()
        else:
            await self._session.get_async().flush()

        await self._session.get_async().refresh(obj)
