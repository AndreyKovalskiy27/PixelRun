"""Player"""


import pygame
import settings


class Player:
    """
    Player class to draw player and
    move player with keyboard
    """
    def __init__(self, start_coords = (0, 0)):
        self.x, self.y = start_coords
        self.speed = settings.PLAYER_SPEED
        self.surface = pygame.Surface((150, 150))
        self.surface.fill((255, 255, 255))

    def draw(self, screen):
        """Draw player"""
        screen.blit(
             self.surface,
             (self.x, self.y)
        )

    def keyboard_handler(self):
        """Changes player's position by using keyboard"""
        pressed_keys = pygame.key.get_pressed()

        # Moving player to the left
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= settings.PLAYER_SPEED

        # Moving player to the right
        elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if self.x + self.surface.get_width() < settings.WINDOW_SIZE[0]:
                self.x += settings.PLAYER_SPEED
        
        # jump
        elif pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_SPACE]:
                ... # Jumping is a hard algorithm i'll realize later
