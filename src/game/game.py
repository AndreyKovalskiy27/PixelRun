"""Main games class"""


import settings
import pygame
from utils import MainMenu
from .create_game_objects import create_game_objects
from .event_handler import event_handler


class Game:
    """Main game"""
    def __init__(self):
        """Start game"""
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        pygame.display.set_caption("Pixel run")

        icon = pygame.image.load(settings.ICON_IMAGE_PATH)
        pygame.display.set_icon(icon)  # For some reason icon doesn't work on Windows

    def mainloop(self):
        """Main loop of the game"""
        create_game_objects(self)
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu()

        # Music
        pygame.mixer.music.load(settings.BACKGROUND_MUSIC_PATH)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(settings.BACKGROUND_MUSIC_VOLUME)

        while True:
            self.clock.tick(settings.BASE_FPS)
            pygame.display.update()
            self.screen.fill(settings.BACKGROUND_COLOR)

            if self.game_type == "game":
                # Moving objects
                self.player_object.keyboard_handler()
                self.player_object.apply_gravity()
                self.platform.move_with_background()

                # Drawing game objects
                self.player_object.draw(self.screen)
                self.platform.draw(self.screen)

                self.platform.stop_player(self.player_object)

            else:
                self.main_menu.draw_main_menu(self.screen)

            event_handler(self)