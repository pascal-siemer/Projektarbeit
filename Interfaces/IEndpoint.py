from abc import ABC, abstractmethod

from Definitions.Message import Message


class IEndpoint(ABC):

    @abstractmethod
    async def handle_message(self, message: Message) -> None:
        pass
