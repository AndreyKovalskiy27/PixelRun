"""Game settings"""


import os
from utils.user_settings import UserSettings


users_settings = UserSettings()


class GameParams:
    PLAYER_SPEED = users_settings.difficulty_params["player_speed"]
    BACKGROUND_SPEED =  users_settings.difficulty_params["background_speed"]
    BULLET_DELAY =  users_settings.difficulty_params["bullet_delay"]
    BULLET_SIZE = users_settings.difficulty_params["bullet_size"]
    BULLET_SPEED =  users_settings.difficulty_params["bullet_speed"]
    SNIPER_ENEMY_MOVING_SPEED =  users_settings.difficulty_params["sniper_enemy_moving_speed"]
    TRIANGLE_ENEMY_SIZE =  users_settings.difficulty_params["triangle_enemy_size"]


# General
WINDOW_SIZE = (1800, 800)
BACKGROUND_COLOR = (50, 50, 50)

MENU_MUSIC_PATH = os.path.join("assets", "sounds", "Menu.mp3")
GAME_MUSIC_PATH = os.path.join("assets", "sounds", "Game.mp3")
SHOP_MUSIC_PATH  = os.path.join("assets", "sounds", "Shop.mp3")

SHIELD_IMAGE_PATH = os.path.join("assets", "images", "shield.png")
COPYRIGHT_IMAGE_PATH = os.path.join("assets", "images", "copyright.png")
SETTINGS_IMAGE_PATH = os.path.join("assets", "images", "settings.png")

MUSIC_VOLUME = users_settings.music_volume
SOUND_EFFECTS_VOLUME = users_settings.sound_effects_volume

BASE_FPS = 60 # 0 for the max FPS
SLOW_DOWN_FPS = 30
ICON_IMAGE_PATH = os.path.join("assets", "images", "icon.jpg")
FONT_PATH = os.path.join("assets", "fonts", "GameFont.ttf")
GROUND_LIMIT = WINDOW_SIZE[1]
TEXT_COLOR = (255, 255, 255)
LEVELS_ON_THE_SCREEN = 3
SHIELD_LASTS_FOR = 10000
MESSAGE_LASTS_FOR = 3000

SHOP_PATH = os.path.expanduser("~/.pixelshop.json")

# Sound effects
BUTTON_SOUND_EFFECT_PATH = os.path.join("assets", "sounds", "effects", "button.mp3")
BUY_SOUND_EFFECT_PATH = os.path.join("assets", "sounds", "effects", "buy_sound.mp3")
COIN_SOUND_EFFECT_PATH = os.path.join("assets", "sounds", "effects", "coin.mp3")
JUMP_SOUND_EFFECT_PATH = os.path.join("assets", "sounds", "effects", "jump.mp3")
DEATH_SOUND_EFFECT_PATH = os.path.join("assets", "sounds", "effects", "rip.mp3")
ERROR_SOUND_EFFECT_PATH = os.path.join("assets", "sounds", "effects", "error.mp3")

# Buttons
BUTTON_COLOR = (30, 30, 30)
BUTTON_SIZE = (500, 150)
BUTTON_CURSOR_COLOR = (70, 70, 70)


# PLayer
PLAYER_SIZE = (80, 100)
PLAYER_BASE_POSITION = (0, 560)

# Player physics
PLAYER_GRAVITY = 1
PLAYER_JUMP_STRENGHT = 30

# Player animation
PLAYER_ANIMATION_DELAY = 100
PLAYER_START_ANIMATION_SPRITE = 0
PLAYER_STANDING_SPIRTE_PATH = os.path.join("assets", "images", "player", "player_standing.PNG")
PLAYER_RUNNING_SPRITE_PATH = os.path.join("assets", "images", "player", "player_running.PNG")
PLAYER_RUNNING2_SPTIRE_PATH = os.path.join("assets", "images", "player", "player_running2.PNG")

ANGRY_MUNCI_STANDING_SPRITE_PATH = os.path.join("assets", "images", "angry_munci", "angry_munci_standing.PNG")
ANGRY_MUNCI_RUNNING_SPRITE_PATH = os.path.join("assets", "images", "angry_munci", "angry_munci_running.PNG")
ANGRY_MUNCI_RUNNING2_SPRITE_PATH = os.path.join("assets", "images", "angry_munci", "angry_munci_running2.PNG")
ANGRY_MUNCI_RUNNING3_SPRITE_PATH = os.path.join("assets", "images", "angry_munci", "angry_munci_running3.PNG")

CAT_JARD_STANDING_SPRITE_PATH = os.path.join("assets", "images", "cat_jard", "cat_jard_standing.PNG")
CAT_JARD_RUNNING_SPRITE_PATH = os.path.join("assets", "images", "cat_jard", "cat_jard_running.PNG")
CAT_JARD_RUNNING2_SPRITE_PATH = os.path.join("assets", "images", "cat_jard", "cat_jard_running2.PNG")
CAT_JARD_RUNNING3_SPRITE_PATH = os.path.join("assets", "images", "cat_jard", "cat_jard_running3.PNG")
CAT_JARD_RUNNING4_SPRITE_PATH = os.path.join("assets", "images", "cat_jard", "cat_jard_running4.PNG")
CAT_JARD_RUNNING5_SPRITE_PATH = os.path.join("assets", "images", "cat_jard", "cat_jard_running5.PNG")

# Enemies
TRIANGLE_ENEMY_COLOR = (255, 0, 255)
SNIPER_ENEMY_COLOR = (150, 0, 0)

# Bullets
SNIPER_ENEMY_SIZE = (200, 50)
BULLET_COLOR = (150, 0, 0)

PLATFORM_SIZE = (200, 50)
PLATFORM_COLOR = (0, 255, 155)
