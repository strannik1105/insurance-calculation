from typing import TypedDict


class ActionMessage(TypedDict):
    action: str
    entity: str
