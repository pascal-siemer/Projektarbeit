import json


class JsonConverter:

    @staticmethod
    def deserialize(deserializable: object) -> str:
        return json.dumps(deserializable, default=lambda obj: obj.__dict__)
    
    @staticmethod
    def serialize(message: str, websocket) -> Message:
        #message umbauen, neues Tool erstellen, welches die Teile aus Message seperiert.
