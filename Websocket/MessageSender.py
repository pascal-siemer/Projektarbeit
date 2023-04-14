class MessageSender:

    def __init__(self, game: Game):
        self.clients = [player.websocket for player in game.players]

    async def send(self, message: str):
        json = JsonConverter.deserialize(message)
        tasks = list()
        for client in self.clients:
            task = asyncio.create_task(client.send(response))
            tasks.append(task)
        await asyncio.wait(tasks)
