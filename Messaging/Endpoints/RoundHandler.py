from Definitions.Connection import Connection
from Definitions.Game import Game
from Interfaces.IEndpoint import IEndpoint


class RoundHandler(IEndpoint):

    def __init__(self, game: Game, question_handler, question_next_handler):
        self.game = game
        self.question_handler
        self.question_next_handler

    #set game.round_started
    async def handle_message(self, connection: Connection, message: str) -> None:
        pass

    #while game.round_status: send round stuff
    #async def send
