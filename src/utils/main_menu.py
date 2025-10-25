"""Games main menu"""


import pygame
import settings
from .button import Button


class MainMenu:
    """Games main menu"""
    def __init__(self):
        """Create all menu objects"""
        """Draw main menu"""
        font = pygame.font.Font(settings.FONT_PATH, 100)
        self.text1 = font.render("PIXEL RUN", True, settings.TEXT_COLOR)
        self.press_enter_button = Button((650, 196), "Press enter to play")
        self.button_shop = Button((650, 400), "SHOP")


    def draw_main_menu(self, screen):
        x = settings.WINDOW_SIZE[0] / 2 - self.text1.get_width() / 2
        screen.blit(self.text1, (x, 50))
        self.press_enter_button.draw(screen)
        self.press_enter_button.update()

        self.button_shop.draw(screen)
        self.button_shop.update()
