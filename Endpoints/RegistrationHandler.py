from Definitions.Game import Game
from Definitions.Message import Message
from Definitions.Player import Player
from Interfaces.IEndpoint import IEndpoint
from Websocket.MessageSender import MessageSender


class RegistrationHandler(IEndpoint):
    
    identifier: str = "Registration"
    
    def __init__(self, game: Game, sender: MessageSender):
        self.game = game
        self.sender = sender
        
    def handle_message(self, message: Message) -> None:
        self.__add_new_player(message)
        answer = Message(message.message_type, message.websocket, "")
        
    def __add_new_player(self, message: Message) -> None:
        players = self.game.players
        for player in players:
            if player.name == message.value:
                return
        new_player = Player(message.value, message.websocket)
        self.game.players.append(new_player)
