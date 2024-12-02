from fastapi_events.handlers.local import local_handler

from common.events.schemas import UserActionSchema
from common.events.types import EventType
from common.kafka import ActionMessage, KafkaClient


# TODO: вынести в отдельный поток/BackgroundTask


@local_handler.register(event_name=EventType.USER_ACTION)
def handle_user_action(obj: tuple[EventType, UserActionSchema]):
    kafka = KafkaClient()
    event: UserActionSchema = obj[1]
    kafka.send_log(ActionMessage(**event.model_dump()))
