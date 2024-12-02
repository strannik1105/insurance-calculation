from datetime import date
from typing import Optional
from uuid import UUID

from fastapi import Query
from pydantic import Field

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


class InsuranceRateFilterSchema(AbstractSchema):
    cargo_type: Optional[str] = Field(Query(None))
    transportation_date_gt: Optional[date] = Field(Query(None))
    transportation_date_lt: Optional[date] = Field(Query(None))


class InsuranceRateImportSchema(AbstractSchema):
    cargo_type: Optional[str]
    rate: Optional[float]


class ImportRatesSchema(AbstractSchema):
    rates: dict[date, InsuranceRateImportSchema]
