from Definitions.Connection import Connection
from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IEndpoint import IEndpoint
from Messaging.MessageSender import MessageSender
from Tools.JsonConverter import JsonConverter


class QuestionHandler(IEndpoint):

    def __init__(self, game: Game, sender: MessageSender):
        self.game = game
        self.sender = sender

    async def handle_message(self, connection: Connection, message: Message) -> None:
        index = self.game.question_index
        if index < 0:
            return
        question = self.game.questions[self.game.question_index]
        json_of_question = JsonConverter.deserialize(question)
        answer = Message(message.handler, json_of_question)
        await self.sender.send(connection, answer)


