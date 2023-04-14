from Definitions.Game import Game
from Definitions.Score import Score
from Interfaces.IEndpoint import IEndpoint


class ScoreHandler(IEndpoint):

    identifier: str = "Score"
    
    def __init__(self, game: Game):
        self.scores = game.scores

    async def handle_request(self, message: str) -> object | None:
        for score in self.scores:
            if score.player_name == message:
                return [score]
        return self.scores


