"""Game settings"""


import os


# General
WINDOW_SIZE = (1800, 800)
BACKGROUND_COLOR = (50, 50, 50)
BACKGROUND_MUSIC_PATH = os.path.join("assets", "sounds", "BackgroundMusic.mp3")
MUSIC_VOLUME = 0.5
SHOP_MUSIC_PATH  = os.path.join("assets", "sounds", "Shop.mp3")
BASE_FPS = 60 # 0 for the max FPS
SLOW_DOWN_FPS = 30
ICON_IMAGE_PATH = "assets/images/icon.jpg"
FONT_PATH = "assets/fonts/GameFont.ttf"
GROUND_LIMIT = WINDOW_SIZE[1]
TEXT_COLOR = (255, 255, 255)
LEVELS_ON_THE_SCREEN = 3
SHOP_PATH = os.path.expanduser("~/.pixelshop.json")

# Buttons
BUTTON_COLOR = (30, 30, 30)
BUTTON_SIZE = (500, 150)
BUTTON_CURSOR_COLOR = (70, 70, 70)

# Background
BACKGROUND_SPEED = 3

# PLayer
PLAYER_SIZE = (63, 70)
PLAYER_SPEED = 10
PLAYER_BASE_POSITION = (0, 560)

# Player physics
PLAYER_GRAVITY = 1
PLAYER_JUMP_STRENGHT = 30

# Player animation
PLAYER_ANIMATION_DELAY = 150
PLAYER_START_ANIMATION_SPRITE = 0
PLAYER_STANDING_SPIRTE_PATH = "assets/images/player/player_standing.PNG"
PLAYER_RUNNING_SPRITE_PATH = "assets/images/player/player_running.PNG"
PLAYER_RUNNING2_SPTIRE_PATH = "assets/images/player/player_running2.PNG"

# Enemies
TRIANGLE_ENEMY_SIZE = (100, 80)
TRIANGLE_ENEMY_COLOR = (255, 0, 255)
SNIPER_ENEMY_COLOR = (150, 0, 0)
SNIPER_ENEMY_SIZE = (200, 50)
SNIPER_ENEMY_MOVING_SPEED = 10

# Bullets
BULLET_SIZE = (50, 10)
BULLET_COLOR = (150, 0, 0)
BULLET_SPEED = 10
BULLET_DELAY = 1000

PLATFORM_SIZE = (200, 50)
PLATFORM_COLOR = (0, 255, 155)
