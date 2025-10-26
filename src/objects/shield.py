import pygame
import settings
from utils import Timer


class Shield:
    def __init__(self, player, shop_util):
        self.is_active = False
        self.player = player
        self.size = 128
        self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, (0, 150, 255, 100),
                           (self.size // 2, self.size // 2),
                           self.size // 2)
        self.timer = Timer(settings.SHIELD_LASTS_FOR)
        self.shop_util = shop_util

    def draw(self, screen):
        if self.is_active:
            expired = self.timer.update()
            if expired:
                self.is_active = False
                return
            x = self.player.x + 32 - self.size // 2
            y = self.player.y + 32 - self.size // 2
            screen.blit(self.surface, (x, y))

        else:
            self.timer.update()

    def use(self):
        if not self.is_active:
            self.is_active = True
            self.shop_util.delete_shields()
            self.timer.start()
