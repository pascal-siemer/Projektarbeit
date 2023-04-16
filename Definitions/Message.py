from dataclasses import dataclass
from typing import Any


@dataclass
class Message:
    message_type: str
    websocket: Any
    value: str
