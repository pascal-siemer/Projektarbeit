import asyncio
import websockets
from Endpoints.EndpointRouter import EndpointRouter
from Tools.JsonConverter import JsonConverter


class WebsocketHandler:

    def __init__(self, router: EndpointRouter):
        self.router = router
        self.clients = set()

    async def listen(self, address: str, port: int) -> None:
        while True:
            async with websockets.serve(self.__handle_socket, address, port):
                await asyncio.Future()  # run forever

    async def __handle_socket(self, websocket) -> None:
        self.clients.add(websocket)
        async for request in websocket:
            print(f"{request}")
            response = await self.router.handle_request(request)
            await self.__send_response(response)

    async def __send_response(self, response: object) -> None:
        response = JsonConverter.deserialize(response)
        tasks = list()
        for client in self.clients:
            task = asyncio.create_task(client.send(response))
            tasks.append(task)
        await asyncio.wait(tasks)
