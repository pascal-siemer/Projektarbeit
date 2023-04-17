import json


class JsonConverter:

    @staticmethod
    def deserialize(deserializable: object) -> str:
        return json.dumps(deserializable, default=lambda obj: obj.__dict__)

    @staticmethod
    def serialize(value: str):
        return json.loads(value)
