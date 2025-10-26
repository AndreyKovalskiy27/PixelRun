"""Func to create game objects"""


from objects import Player
from utils import LevelsManager
from utils import Shield


def create_game_objects(self):
    """Create game objects"""
    # Game objects
    self.player_object = Player()
    self.shield = Shield(self.player_object)
    self.levels_manager = LevelsManager()

    # Others
    self.game_type = "mainmenu"
