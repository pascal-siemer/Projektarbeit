from dataclasses import dataclass


@dataclass
class Message:
    message_type: str
    socket
    value: str
