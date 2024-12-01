from common.router.router import BaseRouter, HttpMethod
from insurance.schemas.insurance_rate import InsuranceRateCreateSchema


class InsuranceRouter(BaseRouter):
    def __init__(self):
        super().__init__("insurance_rate")

    def register_handlers(self) -> None:
        self.router.add_api_route(
            "/create", self.create_insurances, methods=[HttpMethod.POST]
        )

    def create_insurances(self, rate: InsuranceRateCreateSchema) -> None:
        return None
