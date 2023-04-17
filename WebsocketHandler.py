import asyncio
import websockets

from Definitions.Connection import Connection
from Definitions.Message import Message
from Messaging.Endpoints.EndpointRouter import EndpointRouter
from Tools.JsonConverter import JsonConverter


class WebsocketHandler:

    def __init__(self, router: EndpointRouter):
        self.router = router
        self.clients = set()

    async def listen(self, address: str, port: int) -> None:
        while True:
            async with websockets.serve(self.__handle_socket, address, port):
                await asyncio.Future()  # run forever

    # umbenennen in get?, clients.add auslagern in register_client()
    async def __handle_socket(self, websocket) -> None:
        self.clients.add(websocket)
        async for message_string in websocket:
            message = JsonConverter.serialize(message_string)
            print(f"{message}")
            await self.router.handle_message(message)


    async def send(self, connection: Connection, message: Message):
        json_of_message = JsonConverter.deserialize(message)
        connection.websocket.send(json_of_message)

    async def send_to_all(self, connections: list[Connection], message: Message):

        tasks = list()
        for connection in connections:
            task = asyncio.create_task(self.send(connection, message))
            tasks.append(task)

        if len(tasks) < 1:
            return

        await asyncio.wait(task)


    # umbenennen in send?
    async def __send_response(self, response: object) -> None:
        response = JsonConverter.deserialize(response)
        tasks = list()
        for client in self.clients:
            task = asyncio.create_task(client.send(response))
            tasks.append(task)
        await asyncio.wait(tasks)
