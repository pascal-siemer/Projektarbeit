from Definitions.Connection import Connection
from Definitions.Message import Message
from Interfaces.IMessageHandler import IMessageHandler


class MessageRouter:

    def __init__(self):
        self.__handler = dict()

    def add(self, identifier: str, handler: IMessageHandler) -> None:
        self.__handler[identifier] = handler

    async def route(self, connection: Connection, message: Message) -> None:
        endpoint = self.__handler[message.handler]
        return await endpoint.handle_message(connection, message)

