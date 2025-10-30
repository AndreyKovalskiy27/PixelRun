"""Main games class"""


import sys
import settings
import pygame
from shop.shop_menu import ShopMenu
from .main_menu import MainMenu
from utils.sound import SoundTracks
from utils.storage.shop_util import ShopUtil
from .game import Game
from .tab_menu import TabMenu


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
        self.sound_tracks_instance = SoundTracks._get_instance()

    def mainloop(self):
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu()
        self.shop_menu = ShopMenu(self.shop_util)
        self.game_menu = Game(self.shop_util)
        self.tab_menu = TabMenu()

        while True:
            self.clock.tick(settings.BASE_FPS)
            pygame.display.update()
            self.screen.fill(settings.BACKGROUND_COLOR)

            self.tab_menu.update_text(self.clock.get_fps(),
                                      self.main_menu.windows_manager.settings.user_settings.difficulty,
                                      self.sound_tracks_instance.current_music)
            self.tab_menu.draw(self.screen)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        self.tab_menu.is_on = False if self.tab_menu.is_on else True

            if self.game_type != self.prev_game_type:
                if self.game_type == "game" and not self.game_menu.is_paused:
                    SoundTracks.game()
                elif self.game_type == "shop":
                    SoundTracks.shop()
                elif self.game_type == "mainmenu":
                    SoundTracks.main_menu()
                self.prev_game_type = self.game_type

            if self.game_type == "game":
                if pygame.mixer.music.get_busy() and self.game_menu.is_paused:
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
