"""Base class for all the objects in the game (Player, enemy, background)"""


import pygame
import settings


class Object:
    """Base Object"""
    def __init__(self, position):
        self._x, self._y = position
        self.__surface = pygame.Surface((50, 50))
        self.__surface.fill((255, 0, 0))

    def draw(self, screen):
        """Draw object on the screen"""
        screen.blit(
            self.__surface,
            (self._x, self._y)
        )

    def move(self):
        """Move the object with the background"""
        self._x -= settings.BACKGROUND_SPEED

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

    @property
    def surface(self):
        return self.__surface

    def check_collision(self, surface):
        """Check objects collision with another object"""
        rect_self = self.surface.get_rect(topleft=(self.x, self.y))
        rect_other = surface.surface.get_rect(topleft=(surface.x, surface.y))

        # Проверяем пересечение
        return rect_self.colliderect(rect_other)
