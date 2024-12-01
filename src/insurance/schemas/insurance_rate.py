from datetime import date
from typing import Optional
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


class InsuranceRateUpdateSchema(AbstractSchema):
    cargo_type: Optional[str]
    rate: Optional[float]
    transportation_date: Optional[date]


class InsuranceRateImportSchema(AbstractSchema):
    cargo_type: Optional[str]
    rate: Optional[float]


class ImportRatesSchema(AbstractSchema):
    rates: dict[date, InsuranceRateImportSchema]
