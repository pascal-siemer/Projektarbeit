from dataclasses import dataclass
from typing import Any

from Tools.JsonConverter import JsonConverter


@dataclass
class Message:
    handler: str
    value: str

    def __init__(self, handler: str, value: str):
        self.handler = handler
        self.value = value