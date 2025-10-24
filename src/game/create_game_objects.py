"""Func to create game objects"""


from objects import Player
from objects import Platform


def create_game_objects(self):
    """Create game objects"""
    # Game objects
    self.player_object = Player()
    self.platform = Platform((1000, 500))

    # Others
    self.game_type = "mainmenu"
