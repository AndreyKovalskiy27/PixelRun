import pygame
import settings


class SoundTracks:
    _instance = None

    def __init__(self):
        if SoundTracks._instance is not None:
            return
        self.current_music = None
        self.positions = {}
        self.volume = settings.MUSIC_VOLUME
        SoundTracks._instance = self

    @classmethod
    def _get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance


    @classmethod
    def play_music(cls, path):
        inst = cls._get_instance()
        volume = inst.volume
        if inst.current_music is not None:
            inst.positions[inst.current_music] = pygame.mixer.music.get_pos() / 1000

        start_pos = inst.positions.get(path, 0)

        if inst.current_music == path:
            return

        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1, start=start_pos)
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

    @classmethod
    def death(cls):
        sound = pygame.mixer.Sound(settings.DEATH_SOUND_EFFECT_PATH)
        sound.play()

    @classmethod
    def error(cls):
        sound = pygame.mixer.Sound(settings.ERROR_SOUND_EFFECT_PATH)
        sound.play()
