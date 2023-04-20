import asyncio

from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IEndpoint import IEndpoint
from Messaging.MessageSender import MessageSender
from Tools.JsonConverter import JsonConverter


class RoundHandler(IEndpoint):

    def __init__(self, game: Game, sender: MessageSender):
        self.game = game
        self.sender = sender

    #set game.round_started
    async def handle_message(self, connection: Connection, message: str) -> None:
        while True:
            await asyncio.sleep(10)

            answer = Message("Round_Start", "{}")
            await self.sender.send_to_all(self.game.connections, answer)
            await asyncio.sleep(10)
            answer = Message("Round_End", "{}")
            await self.sender.send_to_all(self.game.connections, answer)

    #while game.round_status: send round stuff
    #async def send
