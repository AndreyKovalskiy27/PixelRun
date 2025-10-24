"""Sniper enemy"""


import pygame
import settings
from .object import Object


class SniperEnemy(Object):
    """Sniper enemy who shoots at the player"""
    def __init__(self, position):
        super().__init__(position)

        self.surface = pygame.Surface(settings.SNIPER_ENEMY_SIZE)
        self.surface.fill(settings.SNIPER_ENEMY_COLOR)

        self.moving_direction = "up"

        # Bullets
        self.last_update = 0
        self.bullet_delay = settings.BULLET_DELAY
        self.bullets = []

    def draw(self, screen):
        """Draw sniper enemy and bullets"""
        super().draw(screen)

        for bullet in self.bullets:
            bullet.draw(screen)

    def check_collision(self, surface):
        """Check snipers and bullets collision with other objects"""
        was_bulet_collision = False

        for bullet in self.bullets:
            if bullet.check_collision(surface):
                was_bulet_collision = True
                return True

        if not was_bulet_collision:
            return super().check_collision(surface)

    def shot(self):
        """Shot a bullet"""
        current_tick = pygame.time.get_ticks()
        if current_tick - self.last_update > self.bullet_delay:
            bullet = Object((self.x, self.y))
            bullet.surface = pygame.surface.Surface(settings.BULLET_SIZE)
            bullet.surface.fill(settings.BULLET_COLOR)
            self.bullets.append(bullet)
            self.last_update = current_tick

    @property
    def bullets_amount(self):
        return len(self.bullets)

    def update(self):
        """Update sniper enemy"""
        # Updating bullets
        for bullet in self.bullets:
            bullet.move_left(settings.BULLET_SPEED)
            if bullet.x + bullet.surface.get_width() < 0:
                self.bullets.remove(bullet)

        # Moving sniper enemy
        if self.moving_direction == "up":
            if self._y > 0:
                self.move_up(settings.SNIPER_ENEMY_MOVING_SPEED, True)
            else:
                self.moving_direction = "down"

        elif self.moving_direction == "down":
            if self._y < settings.GROUND_LIMIT:
                self.move_down(settings.SNIPER_ENEMY_MOVING_SPEED, True)
            else:
                self.moving_direction = "up"
