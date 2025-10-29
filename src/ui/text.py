"""Base class for all text in the game"""

import settings
import pygame


class Text:
    """Text"""
    def __init__(self, position, text, size,
                 center_x=False, center_y=False,
                 color=settings.TEXT_COLOR):
        self.text = text
        self.size = size
        self.color = color
        self.center_x = center_x
        self.center_y = center_y

        self.font = pygame.font.Font(settings.FONT_PATH, size)

        self.is_multiple_lined = "\n" in text
        self.x, self.y = position

        if not self.is_multiple_lined:
            self.text_surface = self.font.render(text, True, self.color)
        else:

            lines = self.text.split("\n")
            widths = [self.font.size(line)[0] for line in lines]
            max_width = max(widths)
            total_height = len(lines) * (self.size + 5)

            self.text_surface = pygame.Surface((max_width, total_height), pygame.SRCALPHA)

        center_coords = self.get_center_coords()
        if self.center_x:
            self.x = center_coords[0]
        if self.center_y:
            self.y = center_coords[1]

    def get_center_coords(self):
        x = settings.WINDOW_SIZE[0] / 2 - self.text_surface.get_width() / 2
        y = settings.WINDOW_SIZE[1] / 2 - self.text_surface.get_height() / 2
        return x, y

    def draw(self, screen):
        """Draw text on the screen"""
        if self.is_multiple_lined:
            y = self.y
            for line in self.text.split("\n"):
                screen.blit(self.font.render(line, True, self.color), (self.x, y))
                y += self.size + 5
        else:
            screen.blit(self.text_surface, (self.x, self.y))

    def change_text(self, new):
        self.text = new
        self.is_multiple_lined = "\n" in new

        if not self.is_multiple_lined:
            self.text_surface = self.font.render(new, True, self.color)
        else:
            lines = self.text.split("\n")
            widths = [self.font.size(line)[0] for line in lines]
            max_width = max(widths)
            total_height = len(lines) * (self.size + 5)
            self.text_surface = pygame.Surface((max_width, total_height), pygame.SRCALPHA)

        center_coords = self.get_center_coords()
        if self.center_x:
            self.x = center_coords[0]
        if self.center_y:
            self.y = center_coords[1]
