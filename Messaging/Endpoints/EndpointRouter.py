from Interfaces.IEndpoint import IEndpoint


class EndpointRouter(IEndpoint):

    identifier_left = "<<"
    identifier_right = ">>"

    def __init__(self):
        self.endpoints = dict()

    def add(self, identifier: str, endpoint: IEndpoint) -> None:
        self.endpoints[identifier] = endpoint

    async def handle_request(self, request: str) -> object:
        identifier: str = self.__get_endpoint_identifier(request)
        endpoint: IEndpoint = self.__get_endpoint(identifier)
        message = self.__get_message(request)
        return await endpoint.handle_request(message)

# private methods

    def __get_endpoint(self, identifier: str) -> IEndpoint:
        if identifier is None:
            raise Exception("endpoint identifier is None!")
        return self.endpoints[identifier]

    def __get_endpoint_identifier(self, request: str) -> str | None:
        start_index = request.find(self.identifier_left) + len(self.identifier_left)
        end_index = request.rfind(self.identifier_right)
        if start_index == -1 or end_index == 1:
            return None
        return request[start_index:end_index]

    def __get_message(self, request: str):
        identifier = f"{self.identifier_left}" \
                     f"{self.__get_endpoint_identifier(request)}" \
                     f"{self.identifier_right}"
        return request.replace(identifier, "")
