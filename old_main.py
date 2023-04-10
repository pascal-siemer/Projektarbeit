import asyncio
from websockets import serve
from Definitions.Question import Question

address = "localhost"
port = 8123
question = Question("was?", ["ja", "nein", "vielleicht", "Toast"], 3)

async def handleSocket(websocket):
    while True:
        await websocket.recv()
        response = question.toJSON()
        await websocket.send(response)

async def main():
    while True:
        async with serve(handleSocket, "localhost", 8123):
            await asyncio.Future()  # run forever

asyncio.run(main())