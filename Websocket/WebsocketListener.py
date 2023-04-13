import asyncio
import websockets

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
            async with websockets.serve(self.handle_message, address, port):
                await asyncio.Future()

    async def handle_message(self, websocket):
        self.add_player_if_new() #hier muss sich was ändern, muss leider pennen.
        async for message in websocket:
            await self.receiver.receive()
            # vllt auch direkt an einen EndpointRouter anschließen.
            # EndointRouter zu MessageRouter umbenennen?

    def add_player_if_new(self, name: str, websocket):
        players = self.game.players
        for player in players:
            if player.websocket == websocket:
                return
        new_player = Player(name, websocket)
        self.game.players.add(new_player)
