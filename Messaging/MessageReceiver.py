from Definitions.Connection import Connection
from Messaging.Endpoints.EndpointRouter import EndpointRouter
from Tools.JsonConverter import JsonConverter


class MessageReceiver:

    def __init__(self, router: EndpointRouter):
        self.router = router

    async def receive(self, websocket) -> None:
        async for message_string in websocket:
            print(f"{message_string}")
            message = JsonConverter.serialize(message_string)
            connection = Connection(websocket, None)
            await self.router.handle_message(connection, message)
