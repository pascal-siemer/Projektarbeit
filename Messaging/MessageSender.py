import asyncio

from Definitions.Connection import Connection
from Definitions.Message import Message
from Tools.JsonConverter import JsonConverter


class MessageSender:

    async def send(self, connection: Connection, message: Message):
        json_of_message = JsonConverter.deserialize(message)
        connection.websocket.send(json_of_message)

    async def send_to_all(self, connections: list[Connection], message: Message):
        tasks = list()
        for connection in connections:
            task = asyncio.create_task(self.send(connection, message))
            tasks.append(task)
        await asyncio.wait(tasks)
