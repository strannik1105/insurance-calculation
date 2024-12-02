from fastapi_events.handlers.local import local_handler

from common.events.schemas import UserActionSchema
from common.events.types import EventType


@local_handler.register(event_name=EventType.USER_ACTION)
def handle_user_action(event: UserActionSchema):
    pass
