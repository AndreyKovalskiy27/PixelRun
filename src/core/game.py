"""Main games class"""


import pygame
from ui.button import Button
from objects.player import Player
from objects.shield import Shield
from utils.levels_manager import LevelsManager
from utils.sound import SoundEffects, SoundTracks
from utils.notifier import BaseNotifier
from utils.message import Message
from windows.pause_window import PauseWindow


class GameNotifier(BaseNotifier):
    def __init__(self):
        self.no_shields_message = Message("You don't have shields", (255, 0, 0))
        self.shield_is_active_message = Message("Shield is already active", (255, 0, 0))
        self.shield_used_message = Message("Shield was succefly used!", (0, 255, 0))
        self.game_restarted_message = Message("Game succesfly restarted!", (0, 255, 0))

        self.messages_list = {
            "no_shields": self.no_shields_message,
            "shield_is_active": self.shield_is_active_message,
            "shield_used": self.shield_used_message,
            "game_restarted": self.game_restarted_message
        }


class Game:
    def __init__(self, shop_util):
        self.pause_btn = Button((10, 10), "Pause (Press Enter)", button_size=(350, 50))
        self.restart_btn = Button((400, 10), "Restart (Press R)", button_size=(350, 50))
        self.use_shield_btn = Button((800, 10), "Use shield (Press E)", button_size=(400, 50))

        self.notifier = GameNotifier()
        self.pause_window = PauseWindow()
        self.shop_util = shop_util

        self.is_paused = False

        self.create_game_objects()

    def create_game_objects(self):
        """Create game objects"""
        # Game objects
        self.player_object = Player()
        self.shield = Shield(self.player_object, self.shop_util)
        self.levels_manager = LevelsManager(self.shop_util)

    def keyboard_handler(self, pygame_event):
        for event in pygame_event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.create_game_objects()
                    self.notifier.show("game_restarted")

                elif event.key == pygame.K_e:
                    self.use_shield()

                elif event.key == pygame.K_RETURN:
                    return "pause"

    def use_shield(self):
        if not self.shield.is_active:
            if self.shop_util.shields >= 1:
                self.shield.use()
                self.notifier.show("shield_used")

            else:
                self.notifier.show("no_shields")
                SoundEffects.error()

        else:
            self.notifier.show("shield_is_active")
            SoundEffects.error()

    def pause(self):
        self.shield.timer.pause()
        self.player_object.animation.timer.pause()
        pygame.mixer.music.pause()
        self.is_paused = True
        self.pause_window.is_on = True

    def resume(self):
        self.shield.timer.resume()
        self.player_object.animation.timer.resume()

        # если сейчас в плеере уже игра (мы просто были на паузе) — unpause,
        # иначе — явно переключаемся на игровой трек
        if SoundTracks._get_instance().music_type == "game":
            pygame.mixer.music.unpause()
        else:
            SoundTracks.game()

        self.is_paused = False
        self.pause_window.is_on = False

    def draw(self, screen, event):
        if not self.pause_window.is_on:
            # Moving objects
            if self.player_object.keyboard_handler() == "jumped":
                SoundEffects.jump()

            self.player_object.apply_gravity()
            self.player_object.move_with_background()

            res = self.levels_manager.update(self.player_object)
            if res and not self.shield.is_active:
                self.create_game_objects()
                SoundEffects.death()

            if self.restart_btn.is_clicked(event):
                self.create_game_objects()
                self.notifier.show("game_restarted")

            elif self.use_shield_btn.is_clicked(event):
                self.use_shield()


        self.shield.draw(screen)

        # Drawing game objects
        self.player_object.draw(screen)
        self.levels_manager.draw(screen)
        self.pause_btn.draw(screen)
        self.restart_btn.draw(screen)
        self.use_shield_btn.draw(screen)
        self.notifier.draw(screen)

        res = self.pause_window.draw(screen, event)
        if res == "mainmenu":
            return True

        elif res == "continue":
            self.resume()

        if self.keyboard_handler(event) == "pause":
            self.pause_window.is_on = False if self.pause_window.is_on else True

            if self.pause_window.is_on:
                self.pause()

            else:
                self.resume()

        if self.pause_btn.is_clicked(event):
            self.pause_window.is_on = False if self.pause_window.is_on else True

            if self.pause_window.is_on:
                self.pause()

            else:
                self.resume()
