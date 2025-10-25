"""Base class for all buttons in the game"""


import pygame
import settings


class Button:
    """Button"""
    def __init__(self, position, text):
        self.x, self.y = position
        self.surface = pygame.Surface(settings.BUTTON_SIZE)
        self.surface.fill(settings.BUTTON_COLOR)
        self.button_rect = pygame.Rect(self.x, self.y, self.surface.get_width(), self.surface.get_height())

        font = pygame.font.Font(settings.FONT_PATH, 30)
        self.text = font.render(text, True, settings.TEXT_COLOR)

        self.text_rect = self.text.get_rect(center=(self.x + self.surface.get_width() / 2,
                                                    self.y + self.surface.get_height() / 2))

    def draw(self, screen):
        """Draw button on the screen"""
        screen.blit(self.surface, (self.x, self.y))
        screen.blit(self.text, self.text_rect)

    def update(self):
        """Update button"""
        mouse_pos = pygame.mouse.get_pos()
       

        if self.button_rect.collidepoint(mouse_pos):
            self.surface.fill(settings.BUTTON_CURSOR_COLOR)

        else:
            self.surface.fill(settings.BUTTON_COLOR)


    def is_clicked(self):
        """Returns True if button is being clicked by mouse"""
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.button_rect.collidepoint(mouse_pos):
                    print("Кнопка нажата!")
                    return True
