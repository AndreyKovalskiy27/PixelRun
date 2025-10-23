"""Triangle enemy"""


import pygame
from utils import Object


class TriangleEnemy(Object):
    """Triangle enemy"""
    def __init__(self, position, width=100, height=80, color=(255, 0, 0)):
        super().__init__(position)

        # Создаем поверхность для треугольника
        self._surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self._surface = self._surface.convert_alpha()

        points = [
            (width // 2, 0),
            (0, height),
            (width, height)
        ]
        pygame.draw.polygon(self._surface, color, points)
