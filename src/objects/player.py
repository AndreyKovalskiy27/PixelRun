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
        self.gravity = settings.PLAYER_GRAVITY # Gravity strength
        self.jump_strength = settings.PLAYER_JUMP_STRENGHT # Initial jump velocity
        self.velocity_y = 0     # Vertical speed
        self.on_ground = True   # Is the player on the ground?

        # Allowed moving directions
        self.can_move_left = True
        self.can_move_right = True
        self.can_move_down = True
        self.can_move_up = True

        # Player animation
        self.animation = PlayerAnimation()

    def move_with_background(self):
        """Move player with the background"""
        super().move_left(settings.BACKGROUND_SPEED, True)

    def draw(self, screen):
        """Draw the player"""
        screen.blit(
            self.animation.current_sprite,
            (self.x, self.y)
        )

    def keyboard_handler(self):
        """Handle keyboard input for player movement"""
        pressed_keys = pygame.key.get_pressed()
        moving = False

        # Move left
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if self.can_move_left:
                if self.x > 0:
                    self.move_left(settings.PLAYER_SPEED, True)
                    self.animation.change_direction("left")
                    moving = True

        # Move right
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if self.can_move_right:
                self.move_right(settings.PLAYER_SPEED, True)
                self.animation.change_direction("right")
                moving = True

        # Jump
        if (pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_SPACE]) and self.on_ground:
            if self.can_move_up:
                self.velocity_y = -self.jump_strength  # Go up
                self.on_ground = False

        # Standing if not moving
        if not moving:
            self.animation.change_direction("standing")

        self.surface = self.animation.current_sprite

    def apply_gravity(self):
        """Apply gravity to the player"""
        if self.can_move_down:
            self.velocity_y += self.gravity
            self.y += self.velocity_y

        # Limit Y position (ground level from settings)
        ground_level = settings.GROUND_LIMIT - self.surface.get_height()

        # Prevent player from falling below the base level
        if self.y >= ground_level:
            self.y = ground_level
            self.velocity_y = 0
            self.on_ground = True
