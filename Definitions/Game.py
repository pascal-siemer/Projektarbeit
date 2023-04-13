from dataclasses import dataclass

from Definitions.Player import Player
from Definitions.Question import Question
from Definitions.Score import Score


#add round_started: bool

@dataclass
class Game:
    questions: list[Question]
    question_index: int
    players: list[Player]

    def __init__(self):
        self.questions = []
        self.question_index = 0
        self.players = []
