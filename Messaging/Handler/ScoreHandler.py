from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IMessageHandler import IMessageHandler
from Messaging.MessageSender import MessageSender
from Tools.JsonConverter import JsonConverter


class ScoreHandler(IMessageHandler):

    """
    gibt die Player-Liste aus self.game an alle Websockets aus.
    """

    def __init__(self, game: Game, sender: MessageSender):
        self.__game = game
        self.__sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:
        json_of_players = JsonConverter.deserialize(self.__game.players)
        answer = Message(message.handler, json_of_players)
        await self.__sender.send_to_all(self.__game.connections, answer)
