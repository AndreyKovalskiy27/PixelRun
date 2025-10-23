"""Player animation"""


import pygame
import settings


class PlayerAnimation:
    """Class for animating player"""
    def __init__(self):
        # For animations
        self.moving_status = "standing"
        self.moving_direction = "right"
        self.current_running_sprite = settings.PLAYER_START_ANIMATION_SPRITE

        # For animation delay
        self.last_update = 0
        self.animation_delay = settings.PLAYER_ANIMATION_DELAY

        # Loading sprites
        self.standing_sprite = pygame.image.load(settings.PLAYER_STANDING_SPIRTE_PATH)
        self.running_sprites = [pygame.image.load(settings.PLAYER_RUNNING_SPRITE_PATH),
                                pygame.image.load(settings.PLAYER_RUNNING2_SPTIRE_PATH)]

    def change_direction(self, direction):
        """Change player's direction"""
        if direction != "standing":
            self.moving_direction = direction
            self.moving_status = "running"

        else:
            self.moving_status = "standing"

    @property
    def current_sprite(self):
        """Get current player sprite"""
        # If player is standing
        if self.moving_status == "standing":
            # If player is faced to the right
            if self.moving_direction == "right":
                surface = self.standing_sprite

            # If player is faced to the left
            else:
                surface = pygame.transform.flip(self.standing_sprite, True, False)

        # Animation
        current_tick = pygame.time.get_ticks()
        if current_tick - self.last_update > self.animation_delay:
            self.current_running_sprite = 0 if self.current_running_sprite else 1
            self.last_update = current_tick

        # If player is moving left
        if self.moving_status == "running" and self.moving_direction == "left":
            surface = pygame.transform.flip(self.running_sprites[self.current_running_sprite], True, False)

        # If player is moving right
        elif self.moving_status == "running" and self.moving_direction == "right":
            surface = self.running_sprites[self.current_running_sprite]

        return surface
