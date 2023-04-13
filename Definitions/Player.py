class Player:

    def __init__(self, name: str, websocket):
        self.name = name
        self.score = 0
        self.websocket = websocket


"""
from dataclasses import dataclass
@dataclass
class Player:
    name: str
    score: int
    socket: Websocket
"""