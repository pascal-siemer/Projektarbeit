from Definitions.Game import Game
from Definitions.Message import Message
from Interfaces.IEndpoint import IEndpoint
from Definitions.Question import Question
from Websocket.MessageSender import MessageSender


class QuestionHandler(IEndpoint):

    identifier: str = "Question"
    
    def __init__(self, game: Game, sender: MessageSender):
        self.game = game
        self.sender = sender

    async def handle_message(self, message: Message) -> None:
        self.__increase_index()
        question = self.__get_question()
        await self.sender.send(question)

    def __get_question(self) -> Question:
        questions = self.game.questions
        index = self.game.question_index
        return questions[index]

    def __increase_index(self) -> None:
        index = self.game.question_index
        number_of_questions = len(self.game.questions)
        new_index = min(index + 1, number_of_questions - 1)
        self.game.question_index = new_index
