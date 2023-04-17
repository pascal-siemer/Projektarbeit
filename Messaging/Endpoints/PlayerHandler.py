from typing import Any
from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Definitions.Player import Player
from Interfaces.IEndpoint import IEndpoint
from Messaging.MessageSender import MessageSender


class PlayerHandler(IEndpoint):

    def __init__(self, game: Game, sender: MessageSender):
        self.game = game
        self.sender = sender
        pass

    async def handle_message(self, connection: Connection, message: Message) -> None:

        if connection is None:
            return

        if connection.player is not None:
            return

        player = Player(message.value, 0)
        connection.player = player
        self.game.connections.append(connection)

        await self.sender.send_to_all(game.connections, player)





