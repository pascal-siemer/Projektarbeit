import asyncio

from Definitions.Game import Game
from Definitions.Request import Request
from Interfaces.IEndpoint import IEndpoint
from WebsocketHandler import WebsocketHandler


class RoundHandler(IEndpoint):

    round_timer_in_seconds = 120
    after_round_timer_in_seconds = 30

    def __init__(self, game: Game, websocket: WebsocketHandler):
        self.game = game
        self.websocket = websocket

    async def handle_request(self, message: str) -> object:
        pass

    async def loop(self):
        while True:
            await asyncio.sleep(self.round_timer_in_seconds)
            await self.websocket.send("<<Round>>round_over")
            await asyncio.sleep(self.after_round_timer_in_seconds)
            await self.websocket.send("<<Round>>round_start")
