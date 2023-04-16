from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IEndpoint import IEndpoint
from Definitions.Question import Question
from Tools.JsonConverter import JsonConverter
from Websocket.MessageSender import MessageSender


class QuestionHandler(IEndpoint):
    identifier: str = "Question"

    def __init__(self, game: Game, sender: MessageSender):
        self.game = game
        self.sender = sender

    async def handle_message(self, message: Message) -> None:
        question = self.__get_question()
        json_of_question = JsonConverter.deserialize(question)
        answer = Message(message.message_type, message.websocket, json_of_question)
        await self.sender.send(answer)

    def __get_question(self) -> Question:
        questions = self.game.questions
        index = self.game.question_index
        return questions[index]
