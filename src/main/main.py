"""Main games class"""


import settings
import pygame
from shop import ShopMenu
from .main_menu import MainMenu
from ui import Button
from shop import ShopUtil
from .game import Game
from utils import Message


class Main:
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

        self.shop_util = ShopUtil()
        self.game_type = "mainmenu"
        self.current_music = None

    def play_music(self, path, volume=settings.MUSIC_VOLUME):
        """Play background music safely"""
        if self.current_music == path:
            return

        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        self.current_music = path

    def mainloop(self):
        """Main loop of the game"""
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu()
        self.shop_menu = ShopMenu(self.shop_util)
        self.game_menu = Game(self.shop_util)

        while True:
            self.clock.tick(settings.BASE_FPS)
            pygame.display.update()
            self.screen.fill(settings.BACKGROUND_COLOR)

            event = pygame.event.get()

            for _ in event:
                # Quit
                if _.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

                # Keys
                if _.type == pygame.KEYDOWN:
                    # Changing game modes
                    if _.key == pygame.K_RETURN:
                        if self.game_type != "shop":
                            self.game_type = "game" if self.game_type == "mainmenu" else "mainmenu"

                            if self.game_type == "game":
                                self.game_menu.shield.timer.resume()

            if self.game_type == "game":
                self.play_music(settings.GAME_MUSIC_PATH)

                if self.game_menu.draw(self.screen, event):
                    self.game_type = "mainmenu"

            elif self.game_type == "shop":
                self.play_music(settings.SHOP_MUSIC_PATH)
                res = self.shop_menu.draw(self.screen, event)
                if res:
                    self.game_type = "mainmenu"

            elif self.game_type == "mainmenu":
                # Music
                self.play_music(settings.MENU_MUSIC_PATH)
                self.main_menu.draw_main_menu(self.screen)
                if self.main_menu.press_enter_button.is_clicked(event):
                    self.game_type = "game"
                    self.game_menu.shield.timer.resume()

                elif self.main_menu.button_shop.is_clicked(event):
                    self.game_type = "shop"
