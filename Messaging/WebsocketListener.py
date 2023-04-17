import asyncio
import websockets

from Definitions.Connection import Connection
from Definitions.Message import Message
from Messaging.Endpoints.EndpointRouter import EndpointRouter
from Messaging.MessageReceiver import MessageReceiver
from Tools.JsonConverter import JsonConverter


class WebsocketListener:

    def __init__(self, receiver: MessageReceiver):
        self.receiver = receiver

    async def listen(self, address: str, port: int) -> None:
        while True:
            async with websockets.serve(self.receiver.receive, address, port):
                await asyncio.Future()  # run forever
