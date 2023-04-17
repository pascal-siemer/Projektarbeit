from Definitions.Connection import Connection
from Definitions.Game import Game
from Interfaces.IEndpoint import IEndpoint


class RoundHandler(IEndpoint):

    def __init__(self, game: Game):
        self.game = game

    #set game.round_started
    async def handle_message(self, connection: Connection, message: str) -> None:
        return

    #while game.round_status: send round stuff
    #async def send
