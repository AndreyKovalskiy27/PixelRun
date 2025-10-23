import pygame
import settings
import player_animation


class Player:
    """
    Player class to draw player and
    move player with keyboard.
    """
    def __init__(self, start_coords=(0, 0)):
        self.x, self.y = start_coords
        self.speed = settings.PLAYER_SPEED

        # Physics for jumping
        self.gravity = 1        # Gravity strength
        self.jump_strength = 15 # Initial jump velocity
        self.velocity_y = 0     # Vertical speed
        self.on_ground = True   # Is the player on the ground?

        # Player surface (temporary placeholder)
        self.surface = pygame.Surface((50, 50))
        self.surface.fill((0, 0, 0))

    def draw(self, screen):
        """Draw the player"""
        screen.blit(
            self.surface,
            (self.x, self.y)
        )

    def keyboard_handler(self):
        """Handle keyboard input for player movement"""
        pressed_keys = pygame.key.get_pressed()

        # Move left
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= self.speed
                # self.animation.change_direction("left")

        # Move right
        elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if self.x + self.surface.get_width() < settings.WINDOW_SIZE[0]:
                self.x += self.speed
                # self.animation.change_direction("right")

        # Jump
        if (pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_SPACE]) and self.on_ground:
            self.velocity_y = -self.jump_strength  # Go up
            self.on_ground = False

    def apply_gravity(self):
        """Apply gravity to the player"""
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # Limit Y position (ground level from settings)
        ground_level = settings.PLAYER_BASE_Y_POSITION

        # Prevent player from falling below the base level
        if self.y >= ground_level:
            self.y = ground_level
            self.velocity_y = 0
            self.on_ground = True
