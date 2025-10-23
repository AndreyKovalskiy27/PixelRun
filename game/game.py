"""Game"""


import pygame
import settings
from main_menu import draw_main_menu
import enemys
from player import Player
from utils import Background


def init():
    """Start game"""
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode(settings.WINDOW_SIZE)
    pygame.display.set_caption("Pixel run")

    icon = pygame.image.load(settings.ICON_IMAGE_PATH)
    pygame.display.set_icon(icon)  # For some reason icon doesn't work on Windows

    return screen

def create_game_objects():
    """Create game objects"""
    # Game objects
    player_object = Player()
    background_object = Background()
    enemy = enemys.TriangleEnemy((1000, settings.PLAYER_BASE_POSITION[1]))

    # Others
    game_type = "mainmenu"
    return player_object, background_object, enemy, game_type

def mainloop(screen):
    """Main loop of the game"""
    player_object, background_object, enemy, game_type = create_game_objects()
    clock = pygame.time.Clock()

    # Music
    pygame.mixer.music.load(settings.BACKGROUND_MUSIC_PATH)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(settings.BACKGROUND_MUSIC_VOLUME)

    while True:
        clock.tick(settings.TICK_RATE)
        pygame.display.update()
        screen.fill(settings.BACKGROUND_COLOR)

        if game_type == "game":
            # Drawing game objects
            background_object.draw(screen)
            player_object.draw(screen)
            enemy.draw(screen)

            # Moving objects
            background_object.move()
            player_object.keyboard_handler()
            enemy.move()

            # Cheching enemy's collision with the player
            if player_object.check_collision(enemy):
                player_object, background_object, enemy, game_type = create_game_objects()

        else:
            draw_main_menu(screen)

        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_type = "game" if game_type == "mainmenu" else "mainmenu"

def main():
    """Main func. Starts the game"""
    screen = init()
    mainloop(screen)
