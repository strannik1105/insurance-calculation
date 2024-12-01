from uuid import UUID

from common.dao.deps import PgSession
from common.repository import CrudRepository
from insurance.models import InsuranceRate
from insurance.schemas.insurance_rate import (
    ImportRatesSchema,
    InsuranceRateSchema,
    InsuranceRateCreateSchema,
    InsuranceRateUpdateSchema,
)
from utils import NotFoundException


class InsuranceRateService:
    def __init__(self, session: PgSession) -> None:
        self._repository = CrudRepository[InsuranceRate](session, InsuranceRate)

    async def get_all(self, limit: int, offset: int) -> list[InsuranceRateSchema]:
        objs = await self._repository.get_all(limit, offset)
        return [InsuranceRateSchema.model_validate(obj) for obj in objs]

    async def get_one(self, sid: UUID) -> InsuranceRateSchema:
        obj = await self._repository.get(sid)
        if obj is None:
            raise NotFoundException
        return InsuranceRateSchema.model_validate(obj)

    async def update(
        self, sid: UUID, changes: InsuranceRateUpdateSchema
    ) -> InsuranceRateSchema:
        obj = await self._repository.get(sid)
        if obj is None:
            raise NotFoundException
        obj = await self._repository.update(obj, changes.model_dump())
        return InsuranceRateSchema.model_validate(obj)

    async def create(self, rate: InsuranceRateCreateSchema) -> InsuranceRateSchema:
        obj = await self._repository.create(rate.model_dump())
        return InsuranceRateSchema.model_validate(obj)

    async def remove(self, sid: UUID) -> None:
        obj = await self._repository.get(sid)
        if obj is None:
            raise NotFoundException
        await self._repository.delete(obj)

    async def import_rates(self, rates: ImportRatesSchema) -> None:
        await self._repository.create_many(
            [
                dict(transportation_date=date, **rates.rates[date].model_dump())
                for date in rates.rates
            ]
        )
