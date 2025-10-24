"""Platform for the player"""

import pygame
import settings
from .object import Object


class Platform(Object):
    """Platform player can stand on"""
    def __init__(self, position):
        super().__init__(position)

        # Create the platform surface
        self.surface = pygame.Surface((200, 50))
        self.surface.fill(settings.PLATFORM_COLOR)

    def stop_player(self, player):
        """Prevents the player from moving through the platform"""
        if self.check_collision(player):
            if player.x + player.surface.get_width() <= self.x:
                player.x = self.x

            if self.x + self.surface.get_width() <= player.x:
                player.x = self.x + self.surface.get_width()

            if player.y + player.surface.get_height() - player.velocity_y <= self.y:
                player.y = self.y - player.surface.get_height()
                player.on_ground = True
                player.velocity_y = 0

            elif self.y + self.surface.get_height() >= player.y:
                player.y = self.y + self.surface.get_height()
                player.velocity_y = 0
