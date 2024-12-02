from typing import Annotated
from fastapi import Depends

from common.kafka.client import KafkaClient


KafkaClientDep = Annotated[KafkaClient, Depends(KafkaClient)]
