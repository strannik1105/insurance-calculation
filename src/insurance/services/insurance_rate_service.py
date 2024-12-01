from common.dao.deps import PgSession
from common.repository import CrudRepository
from insurance.models import InsuranceRate
from insurance.schemas import InsuranceRateCreateSchema
from insurance.schemas.insurance_rate import InsuranceRateSchema


class InsuranceRateService:
    def __init__(self, session: PgSession) -> None:
        self._repository = CrudRepository[InsuranceRate](session, InsuranceRate)

    async def get_all_insurances(
        self, limit: int, offset: int
    ) -> list[InsuranceRateSchema]:
        objs = await self._repository.get_all(limit, offset)
        return [InsuranceRateSchema.model_validate(obj) for obj in objs]

    async def create_insurance(
        self, rate: InsuranceRateCreateSchema
    ) -> InsuranceRateSchema:
        obj = await self._repository.create(rate.model_dump())
        return InsuranceRateSchema.model_validate(obj)
