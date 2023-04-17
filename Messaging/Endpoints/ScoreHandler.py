from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Score import Score
from Interfaces.IEndpoint import IEndpoint


class ScoreHandler(IEndpoint):

    def __init__(self, game: Game):
        self.game = game

    async def handle_message(self, connection: Connection, message: str) -> object | None:
        for score in self.scores:
            if score.player_name == message:
                return [score]
        return self.scores


