import pickle
import os


SETTINGS_PATH = os.path.expanduser("~/.pixelsettings.json")
DIFFICULTIES = {
    "child": {
        "background_speed": 2,
        "triangle_enemy_size": (50, 80),
        "bullet_speed": 5,
        "bullet_delay": 5000,
        "sniper_enemy_moving_speed": 5,
        "bullet_size": (10, 10),
        "player_speed": 10,
        "name": "Child"
    },
    "normal": {
        "background_speed": 3,
        "triangle_enemy_size": (60, 90),
        "bullet_speed": 10,
        "bullet_delay": 2000,
        "sniper_enemy_moving_speed": 7,
        "bullet_size": (12, 12),
        "player_speed": 11,
        "name": "Normal"
    },
    "hard": {
        "background_speed": 5,
        "triangle_enemy_size": (70, 100),
        "bullet_speed": 15,
        "bullet_delay": 750,
        "sniper_enemy_moving_speed": 10,
        "bullet_size": (25, 25),
        "player_speed": 13,
        "name": "Hard"
    },
    "extreme": {
        "background_speed": 6,
        "triangle_enemy_size": (200, 180),
        "bullet_speed": 20,
        "bullet_delay": 500,
        "sniper_enemy_moving_speed": 15,
        "bullet_size": (50, 50),
        "player_speed": 17,
        "name": "EXTREME"
    }
}


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
                "difficulty": DIFFICULTIES["normal"]["name"]
            }
            return base_settings

    def set_difficulty_to_settings(self):
        from settings import GameParams
        GameParams.BACKGROUND_SPEED =  self.difficulty_params["background_speed"]
        GameParams.BULLET_DELAY =  self.difficulty_params["bullet_delay"]
        GameParams.BULLET_SIZE = self.difficulty_params["bullet_size"]
        GameParams.BULLET_SPEED =  self.difficulty_params["bullet_speed"]
        GameParams.SNIPER_ENEMY_MOVING_SPEED =  self.difficulty_params["sniper_enemy_moving_speed"]
        GameParams.TRIANGLE_ENEMY_SIZE =  self.difficulty_params["triangle_enemy_size"]


    def set_difficulty(self, difficulty):
        self.settings["difficulty"] = DIFFICULTIES[difficulty]["name"]
        self.save()
        self.set_difficulty_to_settings()

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

    @property
    def difficulty(self):
        return self.settings["difficulty"]

    @property
    def difficulty_params(self):
        return DIFFICULTIES[self.difficulty.lower()]
