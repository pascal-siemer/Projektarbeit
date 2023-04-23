from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IMessageHandler import IMessageHandler
from Messaging.MessageSender import MessageSender
from Tools.JsonConverter import JsonConverter


class NextQuestionHandler(IMessageHandler):

    def __init__(self, game: Game, sender: MessageSender):
        self.__game = game
        self.__sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:
        self.__increase_index()
        question = self.__game.questions[self.__game.question_index]
        json_of_question = JsonConverter.deserialize(question)
        answer = Message(message.handler, json_of_question)
        await self.__sender.send_to_all(self.__game.connections, answer)

    def __increase_index(self) -> None:
        index = self.__game.question_index
        number_of_questions = len(self.__game.questions)
        index = min(index + 1, number_of_questions - 1)
        self.__game.question_index = index
