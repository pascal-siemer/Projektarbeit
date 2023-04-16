from Definitions.Message import Message
from Interfaces.IEndpoint import IEndpoint


class EndpointRouter(IEndpoint):

    def __init__(self):
        self.endpoints = dict()

    def add(self, identifier: str, endpoint: IEndpoint) -> None:
        self.endpoints[identifier] = endpoint

    async def handle_message(self, message: Message) -> object:
        endpoint = self.endpoints[message.message_type]
        return await endpoint.handle_request(message)
