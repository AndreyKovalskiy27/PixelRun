from .copyright import CopyrightWindow
from .settings_window import SettingsWindow
from .music_window import MusicWindow
from .how_to_play import HowToPlayWindow


class WindowsManager:
    def __init__(self):
        self.copyright = CopyrightWindow()
        self.settings = SettingsWindow()
        self.how_to_play = HowToPlayWindow()
        self.music_window = MusicWindow()

    def is_a_window_active(self):
        if self.copyright.is_on:
            return True

        if self.how_to_play.is_on:
            return True

        if self.settings.is_on:
            return True

        if self.music_window.is_on:
            return True

        return False

    def show_or_hide_copyright(self):
        self.copyright.is_on = False if self.copyright.is_on else True
        if self.copyright.is_on:
            self.settings.is_on = False
            self.how_to_play.is_on = False
            self.music_window.is_on = False

    def show_or_hide_settings(self):
        self.settings.is_on = False if self.settings.is_on else True
        if self.settings.is_on:
            self.copyright.is_on = False
            self.how_to_play.is_on = False
            self.music_window.is_on = False

    def show_or_hide_how_to_play(self):
        self.how_to_play.is_on = False if self.how_to_play.is_on else True
        if self.how_to_play.is_on:
            self.settings.is_on = False
            self.copyright.is_on = False
            self.music_window.is_on = False

    def show_or_hide_music(self):
        self.music_window.is_on = False if self.music_window.is_on else True
        if self.music_window.is_on:
            self.settings.is_on = False
            self.copyright.is_on = False
            self.how_to_play.is_on = False

    def draw(self, screen, event):
        self.copyright.draw(screen)
        self.settings.draw(screen, event)
        self.how_to_play.draw(screen)
        self.music_window.draw(screen, event)
