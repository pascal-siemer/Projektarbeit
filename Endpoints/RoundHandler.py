from Definitions.Game import Game
from Interfaces.IEndpoint import IEndpoint


class RoundHandler(IEndpoint):

    def __init__(self, game: Game):
        self.game = game

    async def handle_request(self, message: str) -> object:
        pass
