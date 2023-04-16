from Endpoints.EndpointRouter import EndpointRouter
from Tools.MessageProcessor import MessageProcessor


class MessageReceiver:

    # überlegen, was mit den clients passieren soll, vllt als Objekt?
    def __init__(self, router: EndpointRouter):
        self.router = router

    async def receive(self, websocket): #hier muss sich was ändern, muss leider pennen.
        async for message in websocket:
            message_object = MessageProcessor.create_message_object(message, websocket)
            await self.router.handle_message(message_object)
            # vllt auch direkt an einen EndpointRouter anschließen.
            # EndointRouter zu MessageRouter umbenennen?