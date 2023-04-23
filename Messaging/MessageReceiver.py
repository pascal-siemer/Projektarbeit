from Definitions.Connection import Connection
from Messaging.MessageRouter import MessageRouter
from Tools.JsonConverter import JsonConverter


class MessageReceiver:

    def __init__(self, router: MessageRouter):
        self.__router = router

    async def receive(self, websocket) -> None:
        async for message_string in websocket:
            print(f"{message_string}")
            message = JsonConverter.serialize(message_string)
            connection = Connection(websocket, None)
            await self.__router.route(connection, message)
