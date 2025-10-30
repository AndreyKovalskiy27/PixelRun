"""Games main menu"""


from ui.button import Button
from ui.text import Text
from windows.windows_manager import WindowsManager
import settings
import pygame


class MainMenu:
    """Games main menu"""
    def __init__(self):
        """Create all menu objects"""
        self.text2 = Text((550, 0), "PIXEL RUN", 100, True)
        self.button_play = Button((0, 120), "Play", 50, center_x=True)
        self.button_shop = Button((0, 300), "SHOP (NEW)", size=60, center_x=True)
        self.button_copyright = Button((10, 0), pygame.image.load(settings.COPYRIGHT_IMAGE_PATH),
                                       size=(150, 150), button_size=(200, 200), center_y=True)

        self.button_settings = Button((1580, 0), pygame.image.load(settings.SETTINGS_IMAGE_PATH),
                                       size=(150, 150), button_size=(200, 200), center_y=True)

        self.button_how_to_play = Button((1580, 580), "?", 100, (200, 200))
        self.button_music = Button((10, 590), pygame.image.load(settings.MUSIC_IMAGE_PATH),
                                   size=(150, 150), button_size=(200, 200))
        self.windows_manager = WindowsManager()

    def draw_main_menu(self, screen, pygame_event):
        """Draw main menu"""
        self.button_copyright.draw(screen)
        self.button_settings.draw(screen)
        self.button_how_to_play.draw(screen)
        self.button_music.draw(screen)

        self.windows_manager.draw(screen, pygame_event)

        if not self.windows_manager.is_a_window_active():
            self.text2.draw(screen)
            self.button_play.draw(screen)

            self.button_shop.draw(screen)

            if self.button_play.is_clicked(pygame_event):
                return "game"

            elif self.button_shop.is_clicked(pygame_event):
                return "shop"

        if self.button_copyright.is_clicked(pygame_event):
            self.windows_manager.show_or_hide_copyright()

        elif self.button_settings.is_clicked(pygame_event):
            self.windows_manager.show_or_hide_settings()

        elif self.button_how_to_play.is_clicked(pygame_event):
            self.windows_manager.show_or_hide_how_to_play()

        elif self.button_music.is_clicked(pygame_event):
            self.windows_manager.show_or_hide_music()
