"""Player animation"""


import pygame
import settings


class PlayerAnimation:
    """Class for animating player"""
    def __init__(self):
        # For animations
        self.__moving_status = "standing"
        self.__moving_direction = "right"
        self.__current_running_sprite = settings.PLAYER_START_ANIMATION_SPRITE

        # For animation delay
        self.__last_update = 0
        self.__animation_delay = settings.PLAYER_ANIMATION_DELAY

        # Loading sprites
        player_size = settings.PLAYER_SIZE
        self.__standing_sprite = pygame.transform.scale(
                                pygame.image.load(settings.PLAYER_STANDING_SPIRTE_PATH), player_size)
        self.__running_sprites = [pygame.transform.scale(pygame.image.load(settings.PLAYER_RUNNING_SPRITE_PATH), player_size),
                                pygame.transform.scale(pygame.image.load(settings.PLAYER_RUNNING2_SPTIRE_PATH), player_size)
                                ]

    def change_direction(self, direction):
        """Change player's direction"""
        if direction != "standing":
            self.__moving_direction = direction
            self.__moving_status = "running"

        else:
            self.__moving_status = "standing"

    @property
    def current_sprite(self):
        """Get current player sprite"""
        # If player is standing
        if self.__moving_status == "standing":
            # If player is faced to the right
            if self.__moving_direction == "right":
                surface = self.__standing_sprite

            # If player is faced to the left
            else:
                surface = pygame.transform.flip(self.__standing_sprite, True, False)

        # Animation
        current_tick = pygame.time.get_ticks()
        if current_tick - self.__last_update > self.__animation_delay:
            self.__current_running_sprite = 0 if self.__current_running_sprite else 1
            self.__last_update = current_tick

        # If player is moving left
        if self.__moving_status == "running" and self.__moving_direction == "left":
            surface = pygame.transform.flip(self.__running_sprites[self.__current_running_sprite], True, False)

        # If player is moving right
        elif self.__moving_status == "running" and self.__moving_direction == "right":
            surface = self.__running_sprites[self.__current_running_sprite]

        return surface
