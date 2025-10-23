"""Game"""


import pygame
import settings
from utils import draw_main_menu
from objects import Player
from utils import Background
from objects import SniperEnemy


def init():
    """Start game"""
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

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
    sniper_enemy = SniperEnemy((1500, settings.PLAYER_BASE_POSITION[1]))

    # Others
    game_type = "mainmenu"
    return player_object, background_object, sniper_enemy, game_type

def mainloop(screen):
    """Main loop of the game"""
    player_object, background_object, sniper_enemy, game_type = create_game_objects()
    tab_menu_on = False
    fps = settings.BASE_FPS
    clock = pygame.time.Clock()

    # Music
    pygame.mixer.music.load(settings.BACKGROUND_MUSIC_PATH)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(settings.BACKGROUND_MUSIC_VOLUME)

    while True:
        clock.tick(fps)
        pygame.display.update()
        screen.fill(settings.BACKGROUND_COLOR)

        if game_type == "game":
            # Moving objects
            player_object.keyboard_handler()
            background_object.move()
            player_object.move_with_background()
            sniper_enemy.move_with_background()
            player_object.apply_gravity()

            sniper_enemy.shot()
            sniper_enemy.update()

            # Drawing game objects
            background_object.draw(screen)
            player_object.draw(screen)
            sniper_enemy.draw(screen)

            # Cheching enemy's collision with the player
            if sniper_enemy.check_collision(player_object):
                player_object, background_object, sniper_enemy, game_type = create_game_objects()

        else:
            draw_main_menu(screen)

        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                # Changing game modes
                if event.key == pygame.K_RETURN:
                    game_type = "game" if game_type == "mainmenu" else "mainmenu"

                # Restart
                elif event.key == pygame.K_r:
                    if game_type == "game":
                        player_object, background_object, sniper_enemy, game_type = create_game_objects()
                        game_type = "game"

                    else:
                        None

                # Slow down
                elif event.key == pygame.K_t:
                    fps = settings.SLOW_DOWN_FPS if fps == settings.BASE_FPS else settings.BASE_FPS
def main():
    """Main func. Starts the game"""
    screen = init()
    mainloop(screen)
