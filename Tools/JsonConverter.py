import json
from types import SimpleNamespace
from typing import Any


class JsonConverter:

    @staticmethod
    def deserialize(deserializable: object) -> str:
        return json.dumps(deserializable, default=lambda obj: obj.__dict__)

    @staticmethod
    def serialize(value: str):
        return json.loads(value, object_hook=lambda parameters: SimpleNamespace(**parameters))
