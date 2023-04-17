import json
from types import SimpleNamespace
from typing import TypeVar

from Definitions.Message import Message


class JsonConverter:

    @staticmethod
    def deserialize(deserializable: object) -> str:
        return json.dumps(deserializable, default=lambda obj: obj.__dict__)

    @staticmethod
    def serialize_to_dict(value: str):
        return json.loads(value)

    @staticmethod
    def serialize(value: str):
        return json.loads(value, object_hook=lambda parameters: SimpleNamespace(**parameters))
