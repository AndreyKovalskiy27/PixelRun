"""Main games class"""


import settings
import pygame
from shop import ShopMenu
from .main_menu import MainMenu
from ui import Button
from shop import ShopUtil
from objects import Player
from objects.shield import Shield
from utils import LevelsManager
from utils import Message


class Game:
    """Main game"""
    def __init__(self):
        """Start game"""
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode(settings.WINDOW_SIZE)
        self.shop_util = ShopUtil()
        pygame.display.set_caption("Pixel run")

        icon = pygame.image.load(settings.ICON_IMAGE_PATH)
        pygame.display.set_icon(icon)  # For some reason icon doesn't work on Windows

        self.current_music = None

    def create_game_objects(self):
        """Create game objects"""
        # Game objects
        self.player_object = Player()
        self.shield = Shield(self.player_object)
        self.levels_manager = LevelsManager()

        # Others
        self.game_type = "mainmenu"

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
        self.create_game_objects()
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu()
        self.shop_menu = ShopMenu(self.shop_util)
        self.back_btn = Button((10, 10), "< (Press Enter)", (350, 50))
        self.restart_btn = Button((400, 10), "Restart (Press R)", (350, 50))
        self.use_shield_btn = Button((800, 10), "Use shield (Press E)", (400, 50))
        self.no_shields_message = Message("You don't have shields", (255, 0, 0))
        self.shield_is_active_message = Message("Shield is already active", (255, 0, 0))
        self.shield_used_message = Message("Shield was succefly used!", (0, 255, 0))

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
                                self.shield.timer.resume()

                    # Restart
                    elif _.key == pygame.K_r:
                        if self.game_type == "game":
                            self.create_game_objects()
                            self.game_type = "game"

                    elif _.key == pygame.K_e:
                        if self.game_type == "game":
                            if self.shop_util.shields >= 1:
                                if not self.shield.is_active:
                                    self.shield.use()
                                    self.shield_is_active_message.hide()
                                    self.no_shields_message.hide()
                                    self.shield_used_message.show()

                                else:
                                    self.no_shields_message.hide()
                                    self.shield_used_message.hide()
                                    self.shield_is_active_message.show()
                            else:
                                self.shield_used_message.hide()
                                self.shield_is_active_message.hide()
                                self.no_shields_message.show()

            if self.game_type == "game":
                self.play_music(settings.GAME_MUSIC_PATH)

                # Moving objects
                self.player_object.keyboard_handler()
                self.player_object.apply_gravity()
                self.player_object.move_with_background()

                res = self.levels_manager.update(self.player_object)
                if res and not self.shield.is_active:
                    self.create_game_objects()
                    self.game_type = "game"

                self.shield.draw(self.screen)

                # Drawing game objects
                self.player_object.draw(self.screen)
                self.levels_manager.draw(self.screen)
                self.back_btn.draw(self.screen)
                self.back_btn.update()
                self.restart_btn.draw(self.screen)
                self.restart_btn.update()
                self.use_shield_btn.draw(self.screen)
                self.use_shield_btn.update()
                self.no_shields_message.draw(self.screen)
                self.shield_is_active_message.draw(self.screen)
                self.shield_used_message.draw(self.screen)

                if self.back_btn.is_clicked(event):
                    self.shield.timer.pause()
                    self.game_type = "mainmenu"

                elif self.restart_btn.is_clicked(event):
                    self.create_game_objects()
                    self.game_type = "game"

                elif self.use_shield_btn.is_clicked(event):
                    if self.shop_util.shields >= 1:
                        if not self.shield.is_active:
                            self.shield.use()
                            self.shield_is_active_message.hide()
                            self.no_shields_message.hide()
                            self.shield_used_message.show()

                        else:
                            self.no_shields_message.hide()
                            self.shield_used_message.hide()
                            self.shield_is_active_message.show()
                    else:
                        self.shield_used_message.hide()
                        self.shield_is_active_message.show()
                        self.no_shields_message.show()

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
                    self.shield.timer.resume()

                elif self.main_menu.button_shop.is_clicked(event):
                    self.game_type = "shop"
