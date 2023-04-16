import asyncio
import websockets

from websocket import Websocket
from Definitions.Player import Player
from Endpoints.EndpointRouter import EndpointRouter
from Tools.JsonConverter import JsonConverter
from Websocket.MessageReceiver import MessageReceiver


class WebsocketListener:

    def __init__(self, receiver: MessageReceiver, game: Game):
        self.receiver = receiver
        self.game = game

    async def listen(self, address: str, port: int) -> None:
        while True:
            async with websockets.serve(self.receiver.receive, address, port):
                await asyncio.Future()

"""
    def add_player_if_new(self, name: str, websocket: Websocket):
        players = self.game.players
        for player in players:
            if player.websocket == websocket:
                return
        new_player = Player(name, websocket)
        self.game.players.add(new_player)
"""