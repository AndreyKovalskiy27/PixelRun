import pygame
import settings
from utils.sound import SoundEffects


class Button:
    def __init__(self, position, content,
                 size=30,
                 button_size=settings.BUTTON_SIZE,
                 center_x=False,
                 center_y=False):
        self.size = 30
        self.position = position
        self.center_x = center_x
        self.center_y = center_y
        self.button_size = button_size

        if isinstance(content, str):
            font = pygame.font.Font(settings.FONT_PATH, size)
            self.content = font.render(content, True, settings.TEXT_COLOR)
        elif isinstance(content, pygame.Surface):
            self.content = pygame.transform.smoothscale(content, size) if isinstance(size, tuple) else content

        self.x, self.y = position

        self.surface = pygame.Surface(button_size)
        self.surface.fill(settings.BUTTON_COLOR)

        if center_x:
            self.x = settings.WINDOW_SIZE[0] / 2 - self.surface.get_width() / 2

        if center_y:
            self.y = settings.WINDOW_SIZE[1] / 2 - self.surface.get_height() / 2

        self.button_rect = pygame.Rect(self.x, self.y,
                                       self.surface.get_width(),
                                       self.surface.get_height())

        self.content_rect = self.content.get_rect(center=(
            self.x + self.surface.get_width() / 2,
            self.y + self.surface.get_height() / 2
        ))

    def set_text(self, content):
        font = pygame.font.Font(settings.FONT_PATH, self.size)
        self.content = font.render(content, True, settings.TEXT_COLOR)
        self.x, self.y = self.position
        if self.center_x:
            self.x = settings.WINDOW_SIZE[0] / 2 - self.button_size[0] / 2
        if self.center_y:
            self.y = settings.WINDOW_SIZE[1] / 2 - self.button_size[1] / 2
        self.content_rect = self.content.get_rect(center=(self.x + self.button_size[0]/2, self.y + self.button_size[1]/2))

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        screen.blit(self.content, self.content_rect)
        self.update()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            self.surface.fill(settings.BUTTON_CURSOR_COLOR)
        else:
            self.surface.fill(settings.BUTTON_COLOR)

    def is_clicked(self, event, play_sound = True):
        mouse_pos = pygame.mouse.get_pos()
        for e in event:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.button_rect.collidepoint(mouse_pos):
                    if play_sound:
                        SoundEffects.button()

                    return True
