class MessageReceiver:

    # überlegen, was mit den clients passieren soll, vllt als Objekt?
    def __init__(self, router: EndpointRouter):
        self.router = router

    async def receive(self, message: str):
        print(f"{message}")
        self.router.handle_request(message)