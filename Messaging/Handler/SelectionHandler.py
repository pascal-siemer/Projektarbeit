from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Definitions.Player import Player
from Interfaces.IMessageHandler import IMessageHandler


class SelectionHandler(IMessageHandler):

    """
    Nimmt die vom Spieler ausgewählte Antwort (via Index) an
    und erhöht den Score des passenden players um 1, wenn die Antwort richtig ist.
    """

    def __init__(self, game: Game):
        self.__game = game

    async def handle_message(self, connection: Connection, message: Message) -> None:
        current_question = self.__game.questions[self.__game.question_index]
        if message.value != current_question.indexCorrect:
            return
        player = self.get_player_of_connection(connection)
        if player is None:
            return
        player.score += 1

    def get_player_of_connection(self, connection: Connection) -> Player | None:
        for established_connection in self.__game.connections:
            if connection.websocket == established_connection.websocket:
                return established_connection.player
        return None
