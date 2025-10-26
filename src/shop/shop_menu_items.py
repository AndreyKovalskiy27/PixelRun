"""Menu where you can buy items! :)"""


import pygame
import settings
from ui import Button, Text


class ShopMenuItems:
    """Items menu"""
    def __init__(self, shop_util):
        self.title = Text((0, 0), "PIXEL ITEMS", 100, True)
        self.button_back = Button((10, 10), "<", (50, 50))
        self.button_left = Button((410, 0), "<", (100, 100), 100, center_y=True)
        self.button_right = Button((1290, 0), ">", (100, 100), 100, center_y=True)
        self.button_buy = Button((0, 550), "Buy (5 coins)", size=(300, 75), center_x=True)

        # Shield image
        self.shield_image = pygame.image.load(settings.SHIELD_IMAGE_PATH)
        self.shield_image = pygame.transform.scale(self.shield_image, (350, 200))
        self.shield_image_x = settings.WINDOW_SIZE[0] / 2 - self.shield_image.get_width() / 2
        self.shield_image_y = settings.WINDOW_SIZE[1] / 2 - self.shield_image.get_height() / 2

        self.text1 = Text((0, self.shield_image_y - 50), "Shield", 30, True)
        self.text2 = Text((0, self.shield_image_y + 200), "Makes you invinsible for 10 seconds", 30, True)
        self.user_message = Text((0, 200), "", 30, True)
        self.shop_util = shop_util

    def draw(self, screen, pygame_event):
        """Draw items menu"""
        screen.blit(
            self.shield_image,
            (self.shield_image_x, self.shield_image_y)
        )

        self.title.draw(screen)
        self.button_back.draw(screen)
        self.button_back.update()

        self.button_left.draw(screen)
        self.button_left.update()

        self.button_right.draw(screen)
        self.button_right.update()

        self.button_buy.draw(screen)
        self.button_buy.update()

        self.text1.draw(screen)
        self.text2.draw(screen)
        self.user_message.draw(screen)

        current_amount = Text((0, self.shield_image_y + 350), f"Current amount: {self.shop_util.shields}", 30, True)
        current_amount.draw(screen)

        if self.button_back.is_clicked(pygame_event):
            return True

        elif self.button_buy.is_clicked(pygame_event):
            try:
                self.shop_util.buy_shields(1)
                self.user_message.color = (0, 255, 0)
                self.user_message.change_text("You succefly bought shield!")
    

            except:
                self.user_message.color = (255, 0, 0)
                self.user_message.change_text("You don't have enought coins to buy shield!")
    