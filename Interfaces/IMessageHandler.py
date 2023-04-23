from abc import ABC, abstractmethod
from typing import Any

from Definitions.Connection import Connection
from Definitions.Message import Message


class IMessageHandler(ABC):

    @abstractmethod
    async def handle_message(self, connection: Connection, message: Message) -> None:
        pass
