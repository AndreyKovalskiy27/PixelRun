import pygame


class Timer:
    def __init__(self, time):
        self.time = time
        self.start_tick = 0
        self.is_active = False
        self.is_paused = False
        self.pause_start = 0
        self.total_paused = 0

    def start(self):
        self.start_tick = pygame.time.get_ticks()
        self.is_paused = False
        self.is_active = True
        self.total_paused = 0

    def update(self):
        if not self.is_active or self.is_paused:
            return False
        curr_tick = pygame.time.get_ticks()
        elapsed = curr_tick - self.start_tick - self.total_paused
        if elapsed >= self.time:
            self.is_active = False
            return True
        return False

    def pause(self):
        if self.is_active and not self.is_paused:
            self.is_paused = True
            self.pause_start = pygame.time.get_ticks()

    def resume(self):
        if self.is_paused:
            pause_end = pygame.time.get_ticks()
            self.total_paused += pause_end - self.pause_start
            self.is_paused = False
