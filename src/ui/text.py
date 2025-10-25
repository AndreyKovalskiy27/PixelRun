"""Base class for all text in the game"""


import settings
import pygame


class Text:
    """Text"""
    def __init__(self, position, text, size,
                 center_x = False, center_y = False,
                 color=settings.TEXT_COLOR):
        self.text = text
        self.size = size
        self.color = color
        self.font = pygame.font.Font(settings.FONT_PATH, size)
        self.is_multiple_lined = True  # Does text have multiple lines
        if not "\n" in text:
            self.text_surface = self.font.render(text, True, self.color)
            self.is_multiple_lined = False

        self.x, self.y = position
        if center_x and not self.is_multiple_lined:
            self.x = settings.WINDOW_SIZE[0] / 2 - self.text_surface.get_width() / 2  # Placing text at the center by x

        if center_y and not self.is_multiple_lined:
            self.y = settings.WINDOW_SIZE[1] / 2 - self.text_surface.get_height() / 2  # Placing text at the center by y

    def draw(self, screen):
        """Draw text on the screen"""
        if self.is_multiple_lined:
            y = self.y
            for line in self.text.split("\n"):
                screen.blit(self.font.render(line, True, self.color), (self.x, y))
                y += self.size + 5

        else:
            screen.blit(self.text_surface, (self.x, self.y))
