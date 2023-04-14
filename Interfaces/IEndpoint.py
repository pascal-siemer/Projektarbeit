from abc import ABC, abstractmethod


class IEndpoint(ABC):

    @abstractmethod
    async def handle_request(self, message: Message) -> object:
        pass
