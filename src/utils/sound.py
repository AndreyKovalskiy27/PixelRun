import pygame
import settings


class SoundTracks:
    _instance = None

    def __init__(self):
        if SoundTracks._instance is not None:
            return
        self.current_music = None
        SoundTracks._instance = self

    @classmethod
    def _get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    @classmethod
    def play_music(cls, path, volume=settings.MUSIC_VOLUME):
        inst = cls._get_instance()
        if inst.current_music == path:
            return
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        inst.current_music = path

    @classmethod
    def main_menu(cls):
        cls.play_music(settings.MENU_MUSIC_PATH)

    @classmethod
    def shop(cls):
        cls.play_music(settings.SHOP_MUSIC_PATH)

    @classmethod
    def game(cls):
        cls.play_music(settings.GAME_MUSIC_PATH)


class SoundEffects:
    @classmethod
    def button(cls):
        sound = pygame.mixer.Sound(settings.BUTTON_SOUND_EFFECT_PATH)
        sound.play()

    @classmethod
    def jump(cls):
        sound = pygame.mixer.Sound(settings.JUMP_SOUND_EFFECT_PATH)
        sound.play()

    @classmethod
    def buy(cls):
        sound = pygame.mixer.Sound(settings.BUY_SOUND_EFFECT_PATH)
        sound.play()

    @classmethod
    def coin(cls):
        sound = pygame.mixer.Sound(settings.COIN_SOUND_EFFECT_PATH)
        sound.play()
