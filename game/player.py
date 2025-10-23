"""Player"""


import pygame
import settings
import player_animation


class Player:
    """
    Player class to draw player and
    move player with keyboard
    """
    def __init__(self, start_coords = (0, 0)):
        self.x, self.y = start_coords
        self.speed = settings.PLAYER_SPEED
        self.animation = player_animation.PlayerAnimation()

    def draw(self, screen):
        """Draw player"""

        screen.blit(
             self.animation.current_sprite,
             (self.x, self.y)
        )


    def keyboard_handler(self):
        """Changes player's position by using keyboard"""
        pressed_keys = pygame.key.get_pressed()  # Getting pressed keys

        # If player is moving to the left
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= settings.PLAYER_SPEED
                self.animation.change_direction("left")

        # If player is moving to the right
        elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if self.x + self.animation.current_sprite.get_width() < settings.WINDOW_SIZE[0]:
                self.x += settings.PLAYER_SPEED
                self.animation.change_direction("right")
        
        # jump
        elif pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_SPACE]:
                ... # Jumping is a hard algorithm i'll realize later

        # If player is not moving (standing)
        else:
            self.animation.change_direction("standing")
