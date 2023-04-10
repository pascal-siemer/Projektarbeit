from Definitions.Game import Game
from Interfaces.IEndpoint import IEndpoint
from Definitions.Question import Question
from SQL.QustionMapper import QuestionMapper


class QuestionHandler(IEndpoint):

    def __init__(self, game: Game):
        self.index = 0
        self.questions = game.questions

    async def handle_request(self, message: str) -> Question:
        question = await self.__get_question()
        self.__increase_index()
        return question

    async def __get_question(self) -> Question:
        return self.questions[self.index]

    def __increase_index(self) -> None:
        self.index = min(self.index + 1, len(self.questions) - 1)