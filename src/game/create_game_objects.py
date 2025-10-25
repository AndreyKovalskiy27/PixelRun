"""Func to create game objects"""


from objects import Player
from utils import LevelsManager


def create_game_objects(self):
    """Create game objects"""
    # Game objects
    self.player_object = Player()
    self.levels_manager = LevelsManager()

    # Others
    self.game_type = "mainmenu"
