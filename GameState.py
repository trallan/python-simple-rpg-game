class GameState:
    def __init__(self, new_player: object):
        self.player = new_player
        self.enemy = None
        self.zone = "town"
        self.mode = "exploration"