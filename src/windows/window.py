import pygame
import settings


class BaseWindow:
    def __init__(self):
        self.window_box = pygame.Surface((800, 600))
        self.window_box.fill((25, 25, 25))
        self.window_box_x = settings.WINDOW_SIZE[0] / 2 - self.window_box.get_width() / 2
        self.window_box_y = settings.WINDOW_SIZE[1] / 2 - self.window_box.get_height() / 2
        self.is_on = False

    def draw(self, screen):
        if self.is_on:
            screen.blit(self.window_box, (self.window_box_x, self.window_box_y))
