"""Games main menu"""


from ui.button import Button
from ui.text import Text
from windows.copyright import CopyrightWindow
from windows.settings_window import SettingsWindow
from windows.how_to_play import HowToPlayWindow
import settings
import pygame


class MainMenu:
    """Games main menu"""
    def __init__(self):
        """Create all menu objects"""
        self.text2 = Text((550, 0), "PIXEL RUN", 100, True)
        self.press_enter_button = Button((0, 196), "Press enter to play", center_x=True)
        self.button_shop = Button((0, 400), "SHOP (NEW)", size=60, center_x=True)
        self.button_copyright = Button((10, 0), pygame.image.load(settings.COPYRIGHT_IMAGE_PATH),
                                       size=(150, 150), button_size=(200, 200), center_y=True)

        self.button_settings = Button((1580, 0), pygame.image.load(settings.SETTINGS_IMAGE_PATH),
                                       size=(150, 150), button_size=(200, 200), center_y=True)

        self.button_how_to_play = Button((1580, 580), "?", 100, (200, 200))
        self.copyright = CopyrightWindow()
        self.settings = SettingsWindow()
        self.how_to_play = HowToPlayWindow()

    def draw_main_menu(self, screen, pygame_event):
        """Draw main menu"""
        self.button_copyright.draw(screen)
        self.button_settings.draw(screen)
        self.button_how_to_play.draw(screen)

        self.copyright.draw(screen)
        self.settings.draw(screen, pygame_event)
        self.how_to_play.draw(screen)

        if not self.copyright.is_on and not self.settings.is_on and not self.how_to_play.is_on:
            self.text2.draw(screen)
            self.press_enter_button.draw(screen)

            self.button_shop.draw(screen)

            if self.press_enter_button.is_clicked(pygame_event):
                return "game"

            elif self.button_shop.is_clicked(pygame_event):
                return "shop"

        if self.button_copyright.is_clicked(pygame_event):
            self.copyright.is_on = True if not self.copyright.is_on else False

            if self.copyright.is_on:
                self.settings.is_on = False
                self.how_to_play.is_on = False

        elif self.button_settings.is_clicked(pygame_event):
            self.settings.is_on = True if not self.settings.is_on else False

            if self.settings.is_on:
                self.copyright.is_on = False
                self.how_to_play.is_on = False

        elif self.button_how_to_play.is_clicked(pygame_event):
            self.how_to_play.is_on = True if not self.how_to_play.is_on else False

            if self.how_to_play.is_on:
                self.copyright.is_on = False
                self.settings.is_on = False
