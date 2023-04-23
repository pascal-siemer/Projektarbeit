import asyncio

from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IMessageHandler import IMessageHandler
from Messaging.MessageSender import MessageSender


class RoundHandler(IMessageHandler):

    def __init__(self, game: Game, sender: MessageSender):
        self.__game = game
        self.__sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:
        await self.__sender.send_to_all(self.__game.connections, message)

    async def handle_message_old(self, connection: Connection, message: Message) -> None:
        while True:
            await asyncio.sleep(30)
            answer = Message("Round_Start", "{}")
            await self.__sender.send_to_all(self.__game.connections, answer)
            await asyncio.sleep(10)
            answer = Message("Round_End", "{}")
            await self.__sender.send_to_all(self.__game.connections, answer)
