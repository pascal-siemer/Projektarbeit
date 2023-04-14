class RegistrationHandler:
    
    def __init__(self, game: Game)
        self.game = game
        
    def handle_registration(self, message: str):
        __add_new_player(message)
        
    def __add_new_player(message: str)
        players = self.game.players
        for player in players:
            if player.name == message:
                return
        #hier fehlt der entsprechende Socket
        
