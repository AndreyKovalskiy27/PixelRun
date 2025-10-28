"""Games main menu"""


from ui.button import Button
from ui.text import Text
from windows.copyright import CopyrightWindow
from windows.settings_window import SettingsWindow
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

        self.copyright = CopyrightWindow()
        self.settings = SettingsWindow()

    def draw_main_menu(self, screen, pygame_event):
        """Draw main menu"""
        self.button_copyright.draw(screen)
        self.button_settings.draw(screen)

        self.copyright.draw(screen)
        self.settings.draw(screen, pygame_event)

        if not self.copyright.copyright_on and not self.settings.settings_on:
            self.text2.draw(screen)
            self.press_enter_button.draw(screen)

            self.button_shop.draw(screen)

            if self.press_enter_button.is_clicked(pygame_event):
                return "game"

            elif self.button_shop.is_clicked(pygame_event):
                return "shop"

        if self.button_copyright.is_clicked(pygame_event):
            self.copyright.copyright_on = True if not self.copyright.copyright_on else False

            if self.copyright.copyright_on:
                self.settings.settings_on = False


        elif self.button_settings.is_clicked(pygame_event):
            self.settings.settings_on = True if not self.settings.settings_on else False

            if self.settings.settings_on:
                self.copyright.copyright_on = False
