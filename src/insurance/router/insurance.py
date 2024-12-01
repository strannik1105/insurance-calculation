from uuid import UUID
from common.router.router import BaseRouter, HttpMethod
from common.schema import Msg
from insurance.schemas.insurance_rate import (
    InsuranceRateSchema,
    InsuranceRateCreateSchema,
    InsuranceRateUpdateSchema,
)
from insurance.services import deps


class InsuranceRouter(BaseRouter):
    def __init__(self):
        super().__init__("insurance_rate")

    def register_handlers(self) -> None:
        self.router.add_api_route(
            "/get_all", self.get_insurances, methods=[HttpMethod.GET]
        )
        self.router.add_api_route("/get", self.get_insurance, methods=[HttpMethod.GET])
        self.router.add_api_route(
            "/update", self.update_insurance, methods=[HttpMethod.PUT]
        )
        self.router.add_api_route(
            "/create", self.create_insurance, methods=[HttpMethod.POST]
        )
        self.router.add_api_route(
            "/delete", self.remove_insurance, methods=[HttpMethod.DELETE]
        )

    async def get_insurances(
        self, service: deps.InsuranceRateServiceDep, limit: int = 50, offset=0
    ) -> list[InsuranceRateSchema]:
        return await service.get_all(limit, offset)

    async def get_insurance(
        self, service: deps.InsuranceRateServiceDep, sid: UUID
    ) -> InsuranceRateSchema:
        return await service.get_one(sid)

    async def update_insurance(
        self,
        service: deps.InsuranceRateServiceDep,
        sid: UUID,
        changes: InsuranceRateUpdateSchema,
    ) -> InsuranceRateSchema:
        return await service.update(sid, changes)

    async def create_insurance(
        self, service: deps.InsuranceRateServiceDep, rate: InsuranceRateCreateSchema
    ) -> InsuranceRateSchema:
        return await service.create(rate)

    async def remove_insurance(
        self, service: deps.InsuranceRateServiceDep, sid: UUID
    ) -> Msg:
        await service.remove(sid)
        return Msg(msg="Ok")
