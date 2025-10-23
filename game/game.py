"""Game"""


import pygame
import settings
from player import Player
from utils import Background


def init():
    """Start game"""
    pygame.init()

    screen = pygame.display.set_mode(settings.WINDOW_SIZE)
    pygame.display.set_caption("Pixel run")

    icon = pygame.image.load(settings.ICON_IMAGE_PATH)
    pygame.display.set_icon(icon)  # For some reason icon doesn't work on Windows

    return screen

def mainloop(screen):
    """Main loop of the game"""
    # Game objects
    player_object = Player()
    background_object = Background()

    clock = pygame.time.Clock()

    while True:
        clock.tick(settings.TICK_RATE)
        pygame.display.update()
        screen.fill((0, 0, 0))

        # Drawing game objects
        background_object.draw(screen)
        player_object.draw(screen)

        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        background_object.move()
        player_object.keyboard_handler()

def main():
    """Main func. Starts the game"""
    screen = init()
    mainloop(screen)
