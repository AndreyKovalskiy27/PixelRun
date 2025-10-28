"""Main games class"""


import settings
import pygame
from shop.shop_menu import ShopMenu
from .main_menu import MainMenu
from utils.sound import SoundTracks
from shop.shop_util import ShopUtil
from .game import Game


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
                            self.game_menu.shield.timer.pause()

                            if self.game_type == "game":
                                self.game_menu.shield.timer.resume()

            if self.game_type == "game":
                SoundTracks.game()
                if self.game_menu.draw(self.screen, event):
                    self.game_type = "mainmenu"

            elif self.game_type == "shop":
                SoundTracks.shop()
                res = self.shop_menu.draw(self.screen, event)
                if res == True:
                    self.game_type = "mainmenu"

            elif self.game_type == "mainmenu":
                SoundTracks.main_menu()
                res = self.main_menu.draw_main_menu(self.screen, event)
                if res:
                    self.game_type = res
