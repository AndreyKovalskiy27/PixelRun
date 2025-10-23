"""Player"""


import pygame
import settings
from utils import PlayerAnimation 


class Player:
    """
    Player class to draw player and
    move player with keyboard.
    """
    def __init__(self):
        self.__x, self.__y = settings.PLAYER_BASE_POSITION
        self.__speed = settings.PLAYER_SPEED

        # Physics for jumping
        self.__gravity = settings.PLAYER_GRAVITY # Gravity strength
        self.__jump_strength = settings.PLAYER_JUMP_STRENGHT # Initial jump velocity
        self.__velocity_y = 0     # Vertical speed
        self.__on_ground = True   # Is the player on the ground?

        # Player animation
        self.__animation = PlayerAnimation()

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def draw(self, screen):
        """Draw the player"""
        self.apply_gravity()

        screen.blit(
            self.__animation.current_sprite,
            (self.__x, self.__y)
        )

    def keyboard_handler(self):
        """Handle keyboard input for player movement"""
        pressed_keys = pygame.key.get_pressed()
        moving = False

        # Move left
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if self.__x > 0:
                self.__x -= self.__speed
                self.__animation.change_direction("left")
                moving = True

        # Move right
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if self.__x + self.__animation.current_sprite.get_width() < settings.WINDOW_SIZE[0]:
                self.__x += self.__speed
                self.__animation.change_direction("right")
                moving = True

        # Jump
        if (pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_SPACE]) and self.__on_ground:
            self.__velocity_y = -self.__jump_strength  # Go up
            self.__on_ground = False

        # Standing if not moving
        if not moving:
            self.__animation.change_direction("standing")

    def apply_gravity(self):
        """Apply gravity to the player"""
        self.__velocity_y += self.__gravity
        self.__y += self.__velocity_y

        # Limit Y position (ground level from settings)
        ground_level = settings.PLAYER_GROUND_LIMIT

        # Prevent player from falling below the base level
        if self.__y >= ground_level:
            self.__y = ground_level
            self.__velocity_y = 0
            self.__on_ground = True
