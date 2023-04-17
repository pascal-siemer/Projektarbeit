from dataclasses import dataclass

from Definitions.Connection import Connection
from Definitions.Player import Player
from Definitions.Question import Question


#add round_started: bool

@dataclass
class Game:
    questions: list[Question]
    players: list[Player]
    connections: list[Connection]
    question_index: int

    def __init__(self):
        self.questions = []
        self.question_index = -1
        self.players = []
        self.connections = []
