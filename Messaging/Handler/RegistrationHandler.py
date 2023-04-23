from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Definitions.Player import Player
from Interfaces.IMessageHandler import IMessageHandler
from Messaging.MessageSender import MessageSender
from Tools.JsonConverter import JsonConverter


class RegistrationHandler(IMessageHandler):

    def __init__(self, game: Game, sender: MessageSender):
        self.__game = game
        self.__sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:

        if connection is None:
            return

        if connection.player is not None:
            return

        for established_connection in self.__game.connections:    #if player already has a connection
            if established_connection.websocket == connection.websocket:
                return

        player = self.__get_player(message.value)
        if player is None:
            player = Player(message.value, 0)
            self.__game.players.append(player)

        connection.player = player
        self.__game.connections.append(connection)
        json_of_player = JsonConverter.deserialize(self.__game.players)
        answer = Message(message.handler, json_of_player)
        await self.__sender.send_to_all(self.__game.connections, answer)

    def __get_player(self, name: str) -> Player | None:
        for player in self.__game.players:
            if(name == player.name):
                return player
        return None



