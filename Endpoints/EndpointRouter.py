from Interfaces.IEndpoint import IEndpoint


class EndpointRouter(IEndpoint):

    def __init__(self):
        self.endpoints = dict()

    def add(self, identifier: str, endpoint: IEndpoint) -> None:
        self.endpoints[identifier] = endpoint

    async def handle_request(self, message: str) -> object:
        identifier: str = self.__get_endpoint_identifier(message)
        endpoint: IEndpoint = self.__get_endpoint(identifier)
        message_object = MessageProcessor.create_message_object(message)
        return await endpoint.handle_request(message_object)

# private methods

    def __get_endpoint(self, identifier: str) -> IEndpoint:
        if identifier is None:
            raise Exception("endpoint identifier is None!")
        return self.endpoints[identifier]

    def __get_endpoint_identifier(self, message: str) -> str | None:
        start_index = message.find(self.identifier_left) + len(self.identifier_left)
        end_index = message.rfind(self.identifier_right)
        if start_index == -1 or end_index == 1:
            return None
        return message[start_index:end_index]

    def __get_message(self, message: str):
        identifier = f"{self.identifier_left}" \
                     f"{self.__get_endpoint_identifier(message)}" \
                     f"{self.identifier_right}"
        return message.replace(identifier, "")
