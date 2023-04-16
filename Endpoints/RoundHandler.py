import asyncio

from Definitions.Game import Game
from Definitions.Request import Request
from Interfaces.IEndpoint import IEndpoint
from WebsocketHandler import WebsocketHandler


class RoundHandler(IEndpoint):

    identifier: str = "Round"
    round_timer_in_seconds: int = 120
    after_round_timer_in_seconds: int = 30

    def __init__(self, game: Game):
        self.game = game

    async def handle_request(self, message: str) -> object:
        pass

    #Funktionalität vllt in Game-Object implementieren?? game.loop() oder game.start oder sowas halt.
    async def loop(self):
        while True:
            await asyncio.sleep(self.round_timer_in_seconds)
            await self.websocket.send("<<Round>>round_over")
            await asyncio.sleep(self.after_round_timer_in_seconds)
            await self.websocket.send("<<Round>>round_start")
