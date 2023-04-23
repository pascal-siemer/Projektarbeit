from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IMessageHandler import IMessageHandler
from Messaging.MessageSender import MessageSender


class HandshakeHandler(IMessageHandler):

    def __init__(self, game: Game, sender: MessageSender):
        self.__game = game
        self.__sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:
        if connection is None:
            return
        if connection.player is not None:
            return
        connection.player = message.value

        await self.__sender.send_to_all(self.__game.connections)



