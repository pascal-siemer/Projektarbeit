from dataclasses import dataclass
from Definitions.Question import Question
from Definitions.Score import Score


@dataclass
class Game:
    questions: list[Question]
    question_index: int
    scores: list[Score]

    def __init__(self):
        self.questions = []
        self.question_index = -1
        self.scores = []