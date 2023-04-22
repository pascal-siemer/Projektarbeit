from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Definitions.Player import Player
from Definitions.Score import Score
from Interfaces.IEndpoint import IEndpoint
from Messaging.MessageSender import MessageSender
from Tools.Debouncer import Debouncer
from Tools.JsonConverter import JsonConverter


class SelectionHandler(IEndpoint):

    def __init__(self, game: Game):
        self.game = game

    async def handle_message(self, connection: Connection, message: Message) -> None:
        current_question = self.game.questions[self.game.question_index]
        if message.value != current_question.indexCorrect:
            return
        player = self.get_player_of_connection(connection)
        if player is None:
            return
        player.score += 1

    def get_player_of_connection(self, connection: Connection) -> Player | None:
        for established_connection in self.game.connections:
            if connection.websocket == established_connection.websocket:
                return established_connection.player
        return None
