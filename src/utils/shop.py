"""Games shop"""


import pygame
import json
from .button import Button


class Shop:
    """Shop with items and skins"""
    def __init_(self):
        self.shop_type = "shopmenu"
        self.button_items = Button((0, 0), "ITEMS")

    def draw(self, screen):
        """Draw shop"""
        if self.shop_type == "shopmenu":
            self.button_items.draw(screen)
