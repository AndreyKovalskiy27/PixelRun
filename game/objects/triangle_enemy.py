"""Triangle enemy"""


import pygame
import settings
from .object import Object


class TriangleEnemy(Object):
    """Triangle enemy"""
    def __init__(self, position):
        super().__init__(position)

        width, height = settings.TRIANGLE_ENEMY_SIZE
        color = settings.TRIANGLE_ENEMY_COLOR

        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._surface = self._surface.convert_alpha()

        points = [
            (width // 2, 0),
            (0, height),
            (width, height)
        ]
        pygame.draw.polygon(self._surface, color, points)
