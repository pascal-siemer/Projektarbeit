import asyncio

import websockets

from Messaging.MessageReceiver import MessageReceiver


class WebsocketListener:

    def __init__(self, receiver: MessageReceiver):
        self.__receiver = receiver

    async def listen(self, address: str, port: int) -> None:
        while True:
            async with websockets.serve(self.__receiver.receive, address, port):
                await asyncio.Future()  # run forever
