from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IEndpoint import IEndpoint
from Messaging.MessageSender import MessageSender
from Tools.JsonConverter import JsonConverter


class AnswerHandler(IEndpoint):

    def __init__(self, game: Game, sender: MessageSender):
        self.game = game
        self.sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:
        current_question = self.game.questions[self.game.question_index]
        is_answer_correct = message.value == current_question.indexCorrect
        json_of_is_answer_correct = JsonConverter.deserialize(is_answer_correct)
        answer = Message(message.handler, json_of_is_answer_correct)
        await self.sender.send(connection, answer)
