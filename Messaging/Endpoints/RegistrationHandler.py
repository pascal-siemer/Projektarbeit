from typing import Any
from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Definitions.Player import Player
from Interfaces.IEndpoint import IEndpoint
from Messaging.MessageSender import MessageSender
from Tools.JsonConverter import JsonConverter


class RegistrationHandler(IEndpoint):

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
        for established_connection in self.game.connections:
            if(established_connection.websocket == connection.websocket):
                return


        #execution

        player = self.get_player(message.value)
        if player is None:
            player = Player(message.value, 0)
            self.game.players.append(player)

        connection.player = player
        self.game.connections.append(connection)
        json_of_player = JsonConverter.deserialize(self.game.players)
        answer = Message(message.handler, json_of_player)
        await self.sender.send_to_all(self.game.connections, answer)

    def get_player(self, name: str) -> Player | None:
        for player in self.game.players:
            if(name == player.name):
                return player
        return None



