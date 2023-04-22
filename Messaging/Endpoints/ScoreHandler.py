from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IEndpoint import IEndpoint
from Messaging.MessageSender import MessageSender
from Tools.JsonConverter import JsonConverter


class ScoreHandler(IEndpoint):

    def __init__(self, game: Game, sender: MessageSender):
        self.game = game
        self.sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:
        json_of_players = JsonConverter.deserialize(self.game.players)
        answer = Message(message.handler, json_of_players)
        await self.sender.send_to_all(self.game.connections, answer)
