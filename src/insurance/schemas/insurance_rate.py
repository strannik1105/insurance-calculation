from datetime import date
from uuid import UUID

from common.schema import AbstractSchema


class InsuranceRateBaseSchema(AbstractSchema):
    cargo_type: str
    rate: float
    transportation_date: date


class InsuranceRateSchema(InsuranceRateBaseSchema):
    sid: UUID


class InsuranceRateCreateSchema(InsuranceRateBaseSchema):
    pass
