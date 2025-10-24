"""Base class for all the objects in the game (Player, enemies)"""


import pygame
import settings


class Object:
    """Base Object"""
    def __init__(self, position):
        self.x, self.y = position
        self.surface = pygame.Surface((50, 50))
        self.surface.fill((255, 0, 0))

    def draw(self, screen):
        """Draw object on the screen"""
        screen.blit(
            self.surface,
            (self.x, self.y)
        )

    def move_with_background(self, check_borders = False):
        """Move the object with the background"""
        self.move_left(settings.BACKGROUND_SPEED, check_borders)

    def move_right(self, speed, check_borders = False):
        """Move object to the right"""
        if check_borders:
            if self.x + self.surface.get_width() < settings.WINDOW_SIZE[0]:
                self.x += speed

        else:
            self.x += speed

    def move_left(self, speed, check_borders=False):
        """Move object to the left"""
        if check_borders:
            if self.x > 0:
                self.x -= speed
        else:
            self.x -= speed

    def move_up(self, speed, check_borders=False):
        """Move object up"""
        if check_borders:
            if self.y > 0:
                self.y -= speed
        else:
            self.y -= speed

    def move_down(self, speed, check_borders=False):
        """Move object down"""
        if check_borders:
            if self.y < settings.GROUND_LIMIT:
                self.y += speed

        else:
            self.y += speed

    def check_collision(self, surface):
        """Check objects collision with another object"""
        rect_self = self.surface.get_rect(topleft=(self.x, self.y))
        rect_other = surface.surface.get_rect(topleft=(surface.x, surface.y))

        # Проверяем пересечение
        return rect_self.colliderect(rect_other)
