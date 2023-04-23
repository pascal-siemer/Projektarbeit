from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IMessageHandler import IMessageHandler
from Messaging.MessageSender import MessageSender
from Tools.JsonConverter import JsonConverter


class QuestionHandler(IMessageHandler):

    def __init__(self, game: Game, sender: MessageSender):
        self.__game = game
        self.__sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:
        index = self.__game.question_index
        if index < 0:
            return
        question = self.__game.questions[self.__game.question_index]
        json_of_question = JsonConverter.deserialize(question)
        answer = Message(message.handler, json_of_question)
        await self.__sender.send(connection, answer)


