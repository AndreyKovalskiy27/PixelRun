"""Player animation"""


import pygame
import settings
from .timer import Timer
from shop import ShopUtil


class PlayerAnimation:
    """Class for animating player"""
    def __init__(self):
        # For animations
        self.__moving_status = "standing"
        self.__moving_direction = "right"
        self.__current_running_sprite = settings.PLAYER_START_ANIMATION_SPRITE

        # For animation delay
        self.timer = Timer(settings.PLAYER_ANIMATION_DELAY)
        self.timer.start()

        self.load_sprites()

    def load_sprites(self):
        # Loading sprites
        shop_util = ShopUtil()
        skin = shop_util.current_skin()
        player_size = settings.PLAYER_SIZE
        self.__standing_sprite = pygame.transform.scale(
                                pygame.image.load(skin.sprites[0]), player_size)
        self.__running_sprites = [pygame.transform.scale(pygame.image.load(skin.sprites[1]), player_size),
                                pygame.transform.scale(pygame.image.load(skin.sprites[2]), player_size)
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
        if self.timer.update():
            self.__current_running_sprite = 0 if self.__current_running_sprite else 1
            self.timer.start()

        # If player is moving left
        if self.__moving_status == "running" and self.__moving_direction == "left":
            surface = pygame.transform.flip(self.__running_sprites[self.__current_running_sprite], True, False)

        # If player is moving right
        elif self.__moving_status == "running" and self.__moving_direction == "right":
            surface = self.__running_sprites[self.__current_running_sprite]

        return surface
