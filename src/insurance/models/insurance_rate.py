from datetime import datetime
from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from common.model.abstractmodel import AbstractModel


class InsuranceRate(AbstractModel):
    __tablename__ = "insurance_rate"
    __table_args__ = {
        "schema": "insurance",
        "extend_existing": True,
    }

    cargo_type: Mapped[str] = mapped_column(String, nullable=False)
    rate: Mapped[float] = mapped_column(Float, nullable=False)
    transportation_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
