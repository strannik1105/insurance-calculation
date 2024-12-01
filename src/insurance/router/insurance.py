from common.router.router import BaseRouter, HttpMethod
from insurance.schemas.insurance_rate import (
    InsuranceRateCreateSchema,
    InsuranceRateSchema,
)
from insurance.services import deps


class InsuranceRouter(BaseRouter):
    def __init__(self):
        super().__init__("insurance_rate")

    def register_handlers(self) -> None:
        self.router.add_api_route(
            "/get_all", self.get_insurances, methods=[HttpMethod.GET]
        )
        self.router.add_api_route(
            "/create", self.create_insurance, methods=[HttpMethod.POST]
        )

    async def get_insurances(
        self, service: deps.InsuranceRateServiceDep, limit: int = 50, offset=0
    ):
        return await service.get_all_insurances(limit, offset)

    async def create_insurance(
        self, service: deps.InsuranceRateServiceDep, rate: InsuranceRateCreateSchema
    ) -> InsuranceRateSchema:
        return await service.create_insurance(rate)
