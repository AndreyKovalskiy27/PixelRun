import pygame
import settings


class Shield:
    def __init__(self, player):
        self.is_active = False
        self.player = player
        self.last_tick = 0
        self.paused_time = 0
        self.pause_start = 0
        self.lasts_for = settings.SHIELD_LASTS_FOR
        self.size = 128
        self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, (0, 150, 255, 100), (self.size // 2, self.size // 2), self.size // 2)

    def draw(self, screen):
        if not self.is_active:
            return
        curr_tick = pygame.time.get_ticks() - self.paused_time
        if curr_tick - self.last_tick > self.lasts_for:
            self.stop()
            return
        x = self.player.x + 32 - self.size // 2
        y = self.player.y + 32 - self.size // 2
        screen.blit(self.surface, (x, y))

    def pause(self):
        if not self.is_active:
            return
        self.pause_start = pygame.time.get_ticks()

    def resume(self):
        if not self.is_active or self.pause_start == 0:
            return
        paused_duration = pygame.time.get_ticks() - self.pause_start
        self.paused_time += paused_duration
        self.pause_start = 0

    def use(self):
        if not self.is_active:
            self.is_active = True
            self.last_tick = pygame.time.get_ticks() - self.paused_time

    def stop(self):
        self.is_active = False
        self.last_tick = 0
        self.paused_time = 0
        self.pause_start = 0
