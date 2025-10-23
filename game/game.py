"""Game"""


import pygame
import settings
import player


def init():
    """Start game"""
    pygame.init()

    screen = pygame.display.set_mode(settings.WINDOW_SIZE)
    pygame.display.set_caption("Pixel run")

    icon = pygame.image.load("assets/images/icon.jpg")
    pygame.display.set_icon(icon)  # For some reason icon doesn't work on Windows

    return screen

def mainloop(screen):
    """Main loop of the game"""
    player_object = player.Player((0, 600))
    running = True

    while running:
        pygame.display.update()
        screen.fill((0, 0, 0))
        player_object.draw(screen)

        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        player_object.keyboard_handler()

def main():
    """Main func. Starts the game"""
    screen = init()
    mainloop(screen)
