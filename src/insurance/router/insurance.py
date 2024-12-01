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
            "/create", self.create_insurances, methods=[HttpMethod.POST]
        )

    async def create_insurances(
        self, service: deps.InsuranceRateServiceDep, rate: InsuranceRateCreateSchema
    ) -> InsuranceRateSchema:
        return await service.create_insurance(rate)
