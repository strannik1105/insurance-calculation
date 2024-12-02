from enum import Enum


class EventType(Enum):
    USER_ACTION = "user_action"


class ActionType(Enum):
    GET = "GET"
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class EntityType(Enum):
    INSURANCE_RATE = "InsuranceRate"
