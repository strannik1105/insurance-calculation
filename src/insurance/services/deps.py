from typing import Annotated

from fastapi import Depends

from insurance.services import InsuranceRateService


InsuranceRateServiceDep = Annotated[InsuranceRateService, Depends(InsuranceRateService)]
