import asyncio
from typing import Any

from Definitions.Game import Game
from Definitions.Message import Message
from Tools.JsonConverter import JsonConverter


class MessageSender:

    def __init__(self, game: Game):
        self.game = game
        self.clients = [player.websocket for player in game.players]

    async def send(self, message: Message):
        json_of_message = JsonConverter.deserialize(message)
        await message.websocket.send(json_of_message)

    async def send_to_everyone(self, message: Message, clients: list[Any]):
        json_of_message = JsonConverter.deserialize(message)
        for client in clients:
            task = asyncio.create_task(client.send(json))
            tasks.append(task)
        await asyncio.wait(tasks)
