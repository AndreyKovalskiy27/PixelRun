import pickle
import os


SETTINGS_PATH = os.path.expanduser("~/.pixelsettings.json")


class UserSettings:
    def __init__(self):
        self.settings = self.load()

    def load(self):
        try:
            with open(SETTINGS_PATH, "rb") as file:
                data = pickle.load(file)
                return data

        except:
            base_settings =  self.settings = {
                "music_volume": 0.5,
                "sound_effects_volume": 1.0,
            }
            return base_settings

    def save(self):
        with open(SETTINGS_PATH, "wb") as file:
            pickle.dump(self.settings, file)

    def set_music_volume(self, volume):
        self.settings["music_volume"] = volume
        self.save()

    def set_sound_effects_volume(self, volume):
        self.settings["sound_effects_volume"] = volume
        self.save()

    @property
    def music_volume(self):
        return self.settings["music_volume"]

    @property
    def sound_effects_volume(self):
        return self.settings["sound_effects_volume"]
