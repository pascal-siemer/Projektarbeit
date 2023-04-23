from dataclasses import dataclass


@dataclass
class Message:
    handler: str
    value: str

    def __init__(self, handler: str, value: str):
        self.handler = handler
        self.value = value
