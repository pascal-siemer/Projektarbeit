from Definitions.Connection import Connection
from Definitions.Message import Message
from Interfaces.IEndpoint import IEndpoint


class EndpointRouter(IEndpoint):

    identifier_left = "<<"
    identifier_right = ">>"

    def __init__(self):
        self.endpoints = dict()

    def add(self, identifier: str, endpoint: IEndpoint) -> None:
        self.endpoints[identifier] = endpoint

    async def handle_message(self, connection: Connection, message: Message) -> None:
        endpoint = self.endpoints[message.handler]
        return await endpoint.handle_message(connection, message)

