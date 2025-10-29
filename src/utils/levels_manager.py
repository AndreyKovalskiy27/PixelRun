"""Levels manager"""


import random
import settings
from utils import levels
from utils.sound import SoundEffects


class LevelsManager:
    """Manages the sequence of levels"""
    def __init__(self, shop_util):
        self.available_levels = [levels.Level_1,
                                 levels.Level_2,
                                 levels.Level_3,
                                 levels.Level_4,
                                 levels.Level_5,
                                 levels.Level_6,
                                 levels.Level_7,
                                 levels.Level_8,
                                 levels.Level_9,
                                 levels.Level_10]  # List of all available levels
        self.active_levels = []  # Levels currently on the screen
        self.preload_count = settings.LEVELS_ON_THE_SCREEN  # Number of levels to keep ahead

        # Load multiple levels at the start
        for i in range(self.preload_count):
            self.add_random_level(start=(i==0))

        self.shop_util = shop_util

    def add_random_level(self, start=False):
        """Add a random level to the end of active levels"""
        level_class = random.choice(self.available_levels)
        new_level = level_class()

        if start:
            self.active_levels.append(new_level)
        else:
            # Shift new level objects so it appears after the last level
            last_level_end_x = max(obj.x for obj in self.active_levels[-1].objects)
            for obj in new_level.objects:
                obj.x += last_level_end_x + 200  # Add a small gap
            self.active_levels.append(new_level)

    def draw(self, screen):
        """Draw all active levels"""
        for level in self.active_levels:
            level.draw(screen)

    def update(self, player):
        """Update all active levels"""
        was_killed = False
        for level in self.active_levels:
            res = level.update(player)

            if res == "coin":
                self.shop_util.add_coins(settings.GameParams.COINS_INCREASE)
                SoundEffects.coin()

            elif res == "killed":
                return True

        # Check if we need to add a new level ahead
        while len(self.active_levels) < self.preload_count or \
              max(obj.x for obj in self.active_levels[-1].objects) < 1600:
            self.add_random_level()

        # Remove old levels that have fully moved off screen
        self.active_levels = [
            level for level in self.active_levels
            if max(obj.x for obj in level.objects) > 0
        ]

        return was_killed
