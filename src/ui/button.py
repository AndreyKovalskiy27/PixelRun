import pygame
import settings


class Button:
    def __init__(self, position, content,
                 size=30,
                 button_size=settings.BUTTON_SIZE,
                 center_x=False,
                 center_y=False):

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

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        screen.blit(self.content, self.content_rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            self.surface.fill(settings.BUTTON_CURSOR_COLOR)
        else:
            self.surface.fill(settings.BUTTON_COLOR)

    def is_clicked(self, event):
        mouse_pos = pygame.mouse.get_pos()
        for e in event:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.button_rect.collidepoint(mouse_pos):
                    return True
