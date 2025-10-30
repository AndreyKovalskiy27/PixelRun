"""Main games class"""


import settings
import pygame
from shop.shop_menu import ShopMenu
from .main_menu import MainMenu
from utils.sound import SoundTracks
from utils.storage.shop_util import ShopUtil
from .game import Game


class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        pygame.display.set_caption("Pixel run")
        icon = pygame.image.load(settings.ICON_IMAGE_PATH)
        pygame.display.set_icon(icon)

        self.shop_util = ShopUtil()
        self.game_type = "mainmenu"
        self.prev_game_type = None

    def mainloop(self):
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu()
        self.shop_menu = ShopMenu(self.shop_util)
        self.game_menu = Game(self.shop_util)

        while True:
            self.clock.tick(settings.BASE_FPS)
            pygame.display.update()
            self.screen.fill(settings.BACKGROUND_COLOR)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.game_type != "shop":
                            self.game_type = "game" if self.game_type == "mainmenu" else "mainmenu"
                            self.game_menu.shield.timer.pause()
                            if self.game_type == "game":
                                self.game_menu.shield.timer.resume()

            if self.game_type != self.prev_game_type:
                if self.game_type == "game":
                    SoundTracks.game()
                elif self.game_type == "shop":
                    SoundTracks.shop()
                elif self.game_type == "mainmenu":
                    SoundTracks.main_menu()
                self.prev_game_type = self.game_type

            if self.game_type == "game":
                if not pygame.mixer.music.get_busy():
                    SoundTracks.game()

                if self.game_menu.draw(self.screen, events):
                    self.game_type = "mainmenu"

            elif self.game_type == "shop":
                SoundTracks.shop()
                res = self.shop_menu.draw(self.screen, events)
                if res:
                    self.game_type = "mainmenu"
            elif self.game_type == "mainmenu":
                SoundTracks.main_menu()
                res = self.main_menu.draw_main_menu(self.screen, events)
                if res:
                    self.game_type = res
