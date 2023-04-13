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
            async with websockets.serve(self.__handle_message, address, port):
                await asyncio.Future()  # run forever

    # umbenennen in get?, clients.add auslagern in register_client()
    async def __handle_message(self, websocket) -> None:
        self.clients.add(websocket)
        async for message in websocket:
            print(f"{message}")
            answer = await self.router.handle_request(message)
            await self.__send(answer)
    
    # umbenennen in send?
    async def __send(self, response: object) -> None:
        response = JsonConverter.deserialize(response)
        tasks = list()
        for client in self.clients:
            task = asyncio.create_task(client.send(response))
            tasks.append(task)
        await asyncio.wait(tasks)

        
"""
class WebsocketListener:
    
    def __init__(self, receiver: MessageReceiver):
        self.receiver = receiver
    
    async def listen(self, address: str, port: int) -> None:
        while True:
            async with websockets.serve(, address, port):
                await asyncio.Future()

    async def handle_message(self, websocket):
        #clients.add(websocket)
        async for message in websocket:
            await self.receiver.receive()
            #vllt auch direkt an einen EndpointRouter anschließen.
            #EndointRouter zu MessageRouter umbenennen?
    
class MessageReceiver:
    
    # überlegen, was mit den clients passieren soll, vllt als Objekt?
    def __init__(self, router: EndpointRouter):
        self.router = router
        
    async def receive(self, message: str):
        print(f"{message}")
        self.router.handle_request(message):
            
class MessageSender:
    
    def __init__(self, clients: Clients):
        self.clients = clients
        
    async def send(self, message: str):
        json = JsonConverter.deserialize(message)
        tasks = list()
        for client in self.clients:
            task = asyncio.create_task(client.send(response))
            tasks.append(task)
        await asyncio.wait(tasks)
"""

