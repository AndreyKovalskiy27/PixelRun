"""Main games class"""


import pygame
from ui.button import Button
from objects.player import Player
from objects.shield import Shield
from utils.levels_manager import LevelsManager
from utils.message import Message
from utils.sound import SoundEffects


class GameNotifier:
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

    def draw(self, screen):
        for message in self.messages_list.values():
            message.draw(screen)

    def show(self, message_to_show):
        for message, message_object in self.messages_list.items():
            if message != message_to_show:
                message_object.hide()

            elif message == message_to_show:
                message_object.show()

class Game:
    def __init__(self, shop_util):
        self.back_btn = Button((10, 10), "< (Press Enter)", button_size=(350, 50))
        self.restart_btn = Button((400, 10), "Restart (Press R)", button_size=(350, 50))
        self.use_shield_btn = Button((800, 10), "Use shield (Press E)", button_size=(400, 50))

        self.notifier = GameNotifier()
        self.shop_util = shop_util

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

    def use_shield(self):
        if not self.shield.is_active:
            if self.shop_util.shields >= 1:
                self.shield.use()
                self.notifier.show("shield_used")

            else:
                self.notifier.show("no_shields")

        else:
            self.notifier.show("shield_is_active")

    def draw(self, screen, event):
        # Moving objects
        if self.player_object.keyboard_handler() == "jumped":
            SoundEffects.jump()

        self.player_object.apply_gravity()
        self.player_object.move_with_background()

        res = self.levels_manager.update(self.player_object)
        if res and not self.shield.is_active:
            self.create_game_objects()

        self.shield.draw(screen)

        # Drawing game objects
        self.player_object.draw(screen)
        self.levels_manager.draw(screen)
        self.back_btn.draw(screen)
        self.restart_btn.draw(screen)
        self.use_shield_btn.draw(screen)
        self.notifier.draw(screen)
        self.keyboard_handler(event)

        if self.back_btn.is_clicked(event):
            self.shield.timer.pause()
            return True

        elif self.restart_btn.is_clicked(event):
            self.create_game_objects()
            self.notifier.show("game_restarted")

        elif self.use_shield_btn.is_clicked(event):
            self.use_shield()
