from uuid import UUID


from fastapi import Depends
from fastapi_events.dispatcher import dispatch

from common.router.router import BaseRouter, HttpMethod
from common.schema import Msg
from common.events import ActionType, EventType, EntityType, UserActionSchema
from insurance.schemas.insurance_rate import (
    InsuranceRateSchema,
    InsuranceRateCreateSchema,
    InsuranceRateFilterSchema,
    InsuranceRateUpdateSchema,
    ImportRatesSchema,
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
        self.router.add_api_route(
            "/import", self.import_insurances, methods=[HttpMethod.POST]
        )

    async def get_insurances(
        self,
        service: deps.InsuranceRateServiceDep,
        filters: InsuranceRateFilterSchema = Depends(),
        limit: int = 50,
        offset=0,
    ) -> list[InsuranceRateSchema]:
        # dispatch(
        #     event_name=EventType.USER_ACTION,
        #     payload=UserActionSchema(
        #         action=ActionType.GET, entity=EntityType.INSURANCE_RATE
        #     ),
        # )
        return await service.get_all(filters, limit, offset)

    async def get_insurance(
        self, service: deps.InsuranceRateServiceDep, sid: UUID
    ) -> InsuranceRateSchema:
        dispatch(
            event_name=EventType.USER_ACTION,
            payload=UserActionSchema(
                action=ActionType.GET, entity=EntityType.INSURANCE_RATE
            ),
        )
        return await service.get_one(sid)

    async def update_insurance(
        self,
        service: deps.InsuranceRateServiceDep,
        sid: UUID,
        changes: InsuranceRateUpdateSchema,
    ) -> InsuranceRateSchema:
        dispatch(
            event_name=EventType.USER_ACTION,
            payload=UserActionSchema(
                action=ActionType.UPDATE, entity=EntityType.INSURANCE_RATE
            ),
        )
        return await service.update(sid, changes)

    async def create_insurance(
        self, service: deps.InsuranceRateServiceDep, rate: InsuranceRateCreateSchema
    ) -> InsuranceRateSchema:
        dispatch(
            event_name=EventType.USER_ACTION,
            payload=UserActionSchema(
                action=ActionType.CREATE, entity=EntityType.INSURANCE_RATE
            ),
        )
        return await service.create(rate)

    async def remove_insurance(
        self, service: deps.InsuranceRateServiceDep, sid: UUID
    ) -> Msg:
        dispatch(
            event_name=EventType.USER_ACTION,
            payload=UserActionSchema(
                action=ActionType.DELETE, entity=EntityType.INSURANCE_RATE
            ),
        )
        await service.remove(sid)
        return Msg(msg="Ok")

    async def import_insurances(
        self, service: deps.InsuranceRateServiceDep, rates: ImportRatesSchema
    ) -> Msg:
        dispatch(
            event_name=EventType.USER_ACTION,
            payload=UserActionSchema(
                action=ActionType.CREATE, entity=EntityType.INSURANCE_RATE
            ),
        )
        await service.import_rates(rates)
        return Msg(msg="Ok")
