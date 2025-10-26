import pygame
from .object import Object


class Coin(Object):
    def __init__(self, position):
        super().__init__(position)
        self.surface = pygame.Surface((25, 25))
        self.surface.fill((255, 255, 0))
        self.was_collected = False

    def draw(self, screen):
        if not self.was_collected:
            screen.blit(self.surface, (self.x, self.y))

    def check_collision(self, surface):
        if not self.was_collected:
            return super().check_collision(surface)

        else:
            return False
