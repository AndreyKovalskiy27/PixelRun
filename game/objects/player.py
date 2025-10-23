"""Player"""


import pygame
import settings
from .object import Object
from utils import PlayerAnimation


class Player(Object):
    """
    Player class to draw player and
    move player with keyboard.
    """
    def __init__(self):
        super().__init__(settings.PLAYER_BASE_POSITION)
        # Physics for jumping
        self.__gravity = settings.PLAYER_GRAVITY # Gravity strength
        self.__jump_strength = settings.PLAYER_JUMP_STRENGHT # Initial jump velocity
        self.__velocity_y = 0     # Vertical speed
        self.__on_ground = True   # Is the player on the ground?

        # Player animation
        self.__animation = PlayerAnimation()

    def move_with_background(self):
        """Move player with the background"""
        super().move_left(settings.BACKGROUND_SPEED, True)

    def draw(self, screen):
        """Draw the player"""
        screen.blit(
            self.__animation.current_sprite,
            (self._x, self._y)
        )

    @property
    def gravity(self):
        return self.__gravity

    @property
    def jump_strenght(self):
        return self.__jump_strength

    @property
    def on_ground(self):
        return self.__on_ground

    @property
    def velocity_y(self):
        return self.__velocity_y

    @property
    def surface(self):
        return self.__animation.current_sprite

    def keyboard_handler(self):
        """Handle keyboard input for player movement"""
        pressed_keys = pygame.key.get_pressed()
        moving = False

        # Move left
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if self._x > 0:
                self.move_left(settings.PLAYER_SPEED, True)
                self.__animation.change_direction("left")
                moving = True

        # Move right
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
                self.move_right(settings.PLAYER_SPEED, True)
                self.__animation.change_direction("right")
                moving = True

        # Jump
        if (pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_SPACE]) and self.__on_ground:
            self.__velocity_y = -self.__jump_strength  # Go up
            self.__on_ground = False

        # Standing if not moving
        if not moving:
            self.__animation.change_direction("standing")

        self._surface = self.__animation.current_sprite

    def apply_gravity(self):
        """Apply gravity to the player"""
        self.__velocity_y += self.__gravity
        self._y += self.__velocity_y

        # Limit Y position (ground level from settings)
        ground_level = settings.GROUND_LIMIT

        # Prevent player from falling below the base level
        if self._y >= ground_level:
            self._y = ground_level
            self.__velocity_y = 0
            self.__on_ground = True
