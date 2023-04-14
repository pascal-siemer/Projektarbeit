class RegistrationHandler:
    
    def __init__(self, game: Game):
        self.game = game
        
    def handle_registration(self, message: Message) -> None:
        __add_new_player(message)
        
    def __add_new_player(message: Message) -> None:
        players = self.game.players
        for player in players:
            if player.name == message:
                return
        new_player = Player(message.value, message.websocket)
        game.players.add(new_player)
