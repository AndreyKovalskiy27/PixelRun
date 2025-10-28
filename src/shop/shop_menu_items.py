"""Menu where you can buy items! :)"""


import pygame
import settings
from ui.button import Button
from ui.text import Text
from utils.message import Message
from utils.sound import SoundEffects


class ShopMenuItems:
    """Items menu"""
    def __init__(self, shop_util):
        self.title = Text((0, 0), "PIXEL ITEMS", 100, True)
        self.button_back = Button((10, 10), "<", button_size=(50, 50))
        self.button_left = Button((410, 0), "<", button_size=(100, 100), size=100, center_y=True)
        self.button_right = Button((1290, 0), ">", button_size=(100, 100), size=100, center_y=True)
        self.button_buy = Button((0, 550), "Buy (20 coins)", button_size=(300, 75), center_x=True)

        # Shield image
        self.shield_image = pygame.image.load(settings.SHIELD_IMAGE_PATH)
        self.shield_image = pygame.transform.scale(self.shield_image, (350, 200))
        self.shield_image_x = settings.WINDOW_SIZE[0] / 2 - self.shield_image.get_width() / 2
        self.shield_image_y = settings.WINDOW_SIZE[1] / 2 - self.shield_image.get_height() / 2

        self.text1 = Text((0, self.shield_image_y - 50), "Shield", 30, True)
        self.text2 = Text((0, self.shield_image_y + 200), "Makes you invinsible for 10 seconds", 30, True)
        self.bought_shield_message = Message("You succefly bought a shield! :)", (0, 255, 0))
        self.fail_message = Message("You don't have money to buy 1 shield... Go away!!!", (255, 0, 0))
        self.shop_util = shop_util

    def draw(self, screen, pygame_event):
        """Draw items menu"""
        screen.blit(
            self.shield_image,
            (self.shield_image_x, self.shield_image_y)
        )

        self.title.draw(screen)
        self.button_back.draw(screen)
        self.button_left.draw(screen)
        self.button_right.draw(screen)
        self.button_buy.draw(screen)

        self.text1.draw(screen)
        self.text2.draw(screen)
        self.bought_shield_message.draw(screen)
        self.fail_message.draw(screen)

        current_amount = Text((0, self.shield_image_y + 350), f"Current amount: {self.shop_util.shields}", 30, True)
        current_amount.draw(screen)

        if self.button_back.is_clicked(pygame_event):
            return True

        elif self.button_buy.is_clicked(pygame_event, False):
            try:
                self.shop_util.buy_shields()
                self.fail_message.hide()
                self.bought_shield_message.show()
                SoundEffects.buy()

            except:
                self.bought_shield_message.hide()
                self.fail_message.show()
                SoundEffects.error()
