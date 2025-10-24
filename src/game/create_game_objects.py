"""Func to create game objects"""


from objects import Player
from utils import Level_2


def create_game_objects(self):
    """Create game objects"""
    # Game objects
    self.player_object = Player()
    self.level = Level_2()

    # Others
    self.game_type = "mainmenu"
