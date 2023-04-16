from Definitions.Message import Message
from Tools.JsonConverter import JsonConverter


class MessageProcessor:
    
    identifier_left = "<<"
    identifier_right = ">>"


    @staticmethod
    def create_message(message_type: str, websocket, value: object) -> Message:
        json = JsonConverter.deserialize(value)
        return Message(message_type, websocket, json)

    @staticmethod
    def create_message_object(message: str, websocket) -> Message:
        return Message(message_type=MessageProcessor.get_message_type(message),
                       websocket=websocket,
                       value=MessageProcessor.get_message_data(message))
    
    @staticmethod
    def get_message_type(message: str) -> str | None:
        start_index = message.find(MessageProcessor.identifier_left) + len(MessageProcessor.identifier_left)
        end_index = message.rfind(MessageProcessor.identifier_right)
        if start_index == -1 or end_index == 1:
            return None
        return message[start_index:end_index]

    @staticmethod
    def get_message_data(message: str):
        identifier = f"{MessageProcessor.identifier_left}" \
                     f"{MessageProcessor.get_message_type(message)}" \
                     f"{MessageProcessor.identifier_right}"
        return message.replace(identifier, "")
