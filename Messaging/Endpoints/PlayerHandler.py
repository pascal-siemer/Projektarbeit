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

        #guards

        #if no connection
        if connection is None:
            return

        #if connection already has a player
        if connection.player is not None:
            return

        #if player already has a connection
        for connection in self.game.connections:
            if connection.player is None:
                continue
            if connection.player.name == message.value:
                return

        #execution

        player = Player(message.value, 0)
        connection.player = player
        self.game.connections.append(connection)

        await self.sender.send_to_all(self.game.connections, player)





