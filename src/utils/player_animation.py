import pygame
import settings
from .timer import Timer
from shop.shop_util import ShopUtil


class PlayerAnimation:
    def __init__(self):
        self.__moving_status = "standing"
        self.__moving_direction = "right"
        self.__current_running_sprite = settings.PLAYER_START_ANIMATION_SPRITE

        self.timer = Timer(settings.PLAYER_ANIMATION_DELAY)
        self.timer.start()

        self.__last_skin_name = None
        self.__standing_sprite = None
        self.__running_sprites = []

        self.update_skin_if_needed()

    def update_skin_if_needed(self):
        shop_util = ShopUtil()
        skin = shop_util.current_skin()

        if skin.title != self.__last_skin_name:
            self.__last_skin_name = skin.title

            player_size = settings.PLAYER_SIZE

            self.__standing_sprite = pygame.image.load(skin.sprites[0]).convert_alpha()
            self.__standing_sprite = pygame.transform.scale(self.__standing_sprite, player_size)

            self.__running_sprites = []
            for sprite_path in skin.sprites[1:]:
                sprite = pygame.image.load(sprite_path).convert_alpha()
                sprite = pygame.transform.scale(sprite, player_size)
                self.__running_sprites.append(sprite)

    def change_direction(self, direction):
        if direction != "standing":
            self.__moving_direction = direction
            self.__moving_status = "running"
        else:
            self.__moving_status = "standing"

    @property
    def current_sprite(self):
        self.update_skin_if_needed()

        if self.__moving_status == "standing":
            if self.__moving_direction == "right":
                surface = self.__standing_sprite
            else:
                surface = pygame.transform.flip(self.__standing_sprite, True, False)
        else:
            if self.timer.update():
                self.__current_running_sprite = (self.__current_running_sprite + 1) % len(self.__running_sprites)
                self.timer.start()

            sprite = self.__running_sprites[self.__current_running_sprite]
            if self.__moving_direction == "right":
                surface = sprite
            else:
                surface = pygame.transform.flip(sprite, True, False)

        return surface
