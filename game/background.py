"""Game background"""


import pygame
import settings


class Background:
    """Class to work with background"""
    def __init__(self, start_x = 0):
        self.x = start_x
        self.surface = pygame.image.load(settings.BACKGROUND_IMAGE_PATH)
        self.surface = pygame.transform.scale(
            self.surface,
            settings.WINDOW_SIZE)  # Stretch the background to fill the entire screen

    def draw(self, screen):
        """Draw background on the screen"""
        screen.blit(
            self.surface,
            (self.x, 0)
        )

    def move(self):
        """Move background a bit"""
        self.x -= settings.BACKGROUND_SPEED
