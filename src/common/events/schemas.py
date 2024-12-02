from pydantic import BaseModel
from fastapi_events.registry.payload_schema import registry

from common.events.types import EventType


@registry.register(event_name=EventType.USER_ACTION)
class UserActionSchema(BaseModel):
    name: str
    action: str
