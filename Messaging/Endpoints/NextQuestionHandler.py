from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IEndpoint import IEndpoint
from Definitions.Question import Question
from Messaging.MessageSender import MessageSender
from Tools.JsonConverter import JsonConverter


class NextQuestionHandler(IEndpoint):

    def __init__(self, game: Game, sender: MessageSender):
        self.game = game
        self.sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:
        self.__increase_index()
        question = self.game.questions[self.game.question_index]
        json_of_question = JsonConverter.deserialize(question)
        answer = Message(message.handler, json_of_question)
        await self.sender.send_to_all(self.game.connections, answer)

    def __increase_index(self) -> None:
        index = self.game.question_index
        number_of_questions = len(self.game.questions)
        index = min(index + 1, number_of_questions - 1)
        self.game.question_index = index
