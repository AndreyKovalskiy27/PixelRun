import pygame
from utils.sound import SoundTracks, SoundEffects
from ui.button import Button
from ui.text import Text
from utils.user_settings import UserSettings
from .window import BaseWindow


class SettingsWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.music = SoundTracks._get_instance()
        self.effects = SoundEffects._get_instance()
        self.user_settings = UserSettings()

        self.text1 = Text((550, 0), "PIXEL SETTINGS", 100, True)

        # Music
        self.text2 = Text((0, 100), "Music volume", 60, True)
        self.music_volume = Text((0, 185), str(self.music.volume), 50, True)
        self.button_minus_music = Button((650, 170), "-", 50, (75, 75))
        self.button_plus_music = Button((1075, 170), "+", 50, (75, 75))

        # Sound effects
        self.text3 = Text((0, 270), "Sound effects volume", 60, True)
        self.sound_effects_volume = Text((0, 355), str(self.effects.volume), 50, True)
        self.button_minus_sound_effects = Button((650, 340), "-", 50, (75, 75))
        self.button_plus_sound_effects = Button((1075, 340), "+", 50, (75, 75))

        # Difficulty
        self.difficulties_text = {
            "child": Text((0, 525), "Child", 50, True, color=(0, 255, 0)),
            "normal": Text((0, 525), "Normal", 50, True, color=(0, 255, 0)),
            "hard": Text((0, 525), "Hard", 50, True, color=(255, 255, 0)),
            "extreme": Text((0, 525), "EXTREME", 50, True, color=(255, 0, 0)),
        }
        self.difficulties = {
            0: "child",
            1: "normal",
            2: "hard",
            3: "extreme"
        }
        self.text4 = Text((0, 440), "Difficulty", 60, True)
        self.button_minus_difficulty = Button((650, 510), "-", 50, (75, 75))
        self.button_plus_difficulty = Button((1075, 510), "+", 50, (75, 75))
 
    def draw(self, screen, event):
        super().draw(screen)

        if self.is_on:
            self.text1.draw(screen)
            self.text2.draw(screen)
            self.music_volume.draw(screen)
            self.button_minus_music.draw(screen)
            self.button_plus_music.draw(screen)

            self.text3.draw(screen)
            self.sound_effects_volume.draw(screen)
            self.button_minus_sound_effects.draw(screen)
            self.button_plus_sound_effects.draw(screen)

            self.text4.draw(screen)
            self.button_minus_difficulty.draw(screen)
            self.button_plus_difficulty.draw(screen)

            self.difficulties_text[self.user_settings.difficulty.lower()].draw(screen)

            if self.button_minus_music.is_clicked(event):
                self.music.volume = max(0.0, round(self.music.volume - 0.1, 1))
                pygame.mixer.music.set_volume(self.music.volume)
                self.user_settings.set_music_volume(self.music.volume)
                self.music_volume.change_text(str(self.music.volume))

            elif self.button_plus_music.is_clicked(event):
                self.music.volume = min(1.0, round(self.music.volume + 0.1, 1))
                pygame.mixer.music.set_volume(self.music.volume)
                self.user_settings.set_music_volume(self.music.volume)
                self.music_volume.change_text(str(self.music.volume))

            elif self.button_minus_sound_effects.is_clicked(event):
                self.effects.volume = max(0.0, round(self.effects.volume - 0.1, 1))
                self.user_settings.set_sound_effects_volume(self.effects.volume)
                self.sound_effects_volume.change_text(str(self.effects.volume))

            elif self.button_plus_sound_effects.is_clicked(event):
                self.effects.volume = min(1.0, round(self.effects.volume + 0.1, 1))
                self.user_settings.set_sound_effects_volume(self.effects.volume)
                self.sound_effects_volume.change_text(str(self.effects.volume))

            elif self.button_minus_difficulty.is_clicked(event):
                current_index = list(self.difficulties.keys())[list(self.difficulties.values()).index(self.user_settings.difficulty.lower())]
                new_index = max(0, current_index - 1)
                new_difficulty = self.difficulties[new_index]
                self.user_settings.set_difficulty(new_difficulty)
                self.difficulties_text[new_difficulty].draw(screen)

            elif self.button_plus_difficulty.is_clicked(event):
                current_index = list(self.difficulties.keys())[list(self.difficulties.values()).index(self.user_settings.difficulty.lower())]
                new_index = min(len(self.difficulties) - 1, current_index + 1)
                new_difficulty = self.difficulties[new_index]
                self.user_settings.set_difficulty(new_difficulty)
                self.difficulties_text[new_difficulty].draw(screen)
