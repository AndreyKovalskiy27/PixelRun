"""Games main menu"""


from ui.button import Button
from ui.text import Text
import settings
import pygame


class CopyrightWindow:
    def __init__(self):
        self.copyright_box = pygame.Surface((800, 600))
        self.copyright_box.fill((25, 25, 25))
        self.copyright_box_x = settings.WINDOW_SIZE[0] / 2 - self.copyright_box.get_width() / 2
        self.copyright_box_y = settings.WINDOW_SIZE[1] / 2 - self.copyright_box.get_height() / 2

        self.text1 = Text((550, 0), "PIXEL COPYRIGHT", 100, True)
        self.text2 = Text((0, 300), "Shop/main menu theme: 1nicopatty", 30, True)
        self.text3 = Text((0, 350), "Default game theme: LSPlash", 30, True)
        self.text4 = Text((0, 400), "Source code/programer: angrymuncifan2888", 30, True)
        self.text5 = Text((0, 450), "Thanks to Python and PyGame developers!", 30, True)

        self.copyright_on = False

    def draw(self, screen):
        if self.copyright_on:
            screen.blit(self.copyright_box, (
                self.copyright_box_x,
                self.copyright_box_y
            ))

            self.text1.draw(screen)
            self.text2.draw(screen)
            self.text3.draw(screen)
            self.text4.draw(screen)
            self.text5.draw(screen)

class SettingsWindow:
    def __init__(self):
        self.text1 = Text((550, 0), "PIXEL SETTINGS", 100, True)

        self.settings_box = pygame.Surface((800, 600))
        self.settings_box.fill((25, 25, 25))
        self.settings_box_x = settings.WINDOW_SIZE[0] / 2 - self.settings_box.get_width() / 2
        self.settings_box_y = settings.WINDOW_SIZE[1] / 2 - self.settings_box.get_height() / 2
        self.settings_on = False

        self.text2 = Text((0, 100), "Music volume", 60, True)
        self.button_plus_music = Button((600, 150), "-", 30, (50, 50))

    def draw(self, screen):
        if self.settings_on:
            screen.blit(self.settings_box, (
                self.settings_box_x,
                self.settings_box_y
            ))

            self.text1.draw(screen)
            self.text2.draw(screen)
            self.button_plus_music.draw(screen)


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
        self.settings.draw(screen)

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
