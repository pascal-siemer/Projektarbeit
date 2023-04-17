from typing import Any

from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IEndpoint import IEndpoint
from Messaging.MessageSender import MessageSender


class HandshakeHandler(IEndpoint):

    def __init__(self, game: Game, sender: MessageSender):
        self.game = game
        self.sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:
        if connection is None:
            return
        if connection.player is not None:
            return
        connection.player = message.value

        await self.sender.send_to_all(game.connections)



