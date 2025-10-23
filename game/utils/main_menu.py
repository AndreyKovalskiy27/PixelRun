"""Games main menu"""


import pygame
import settings


def draw_main_menu(screen):
    """Draw main menu"""
    font = pygame.font.Font(settings.MAIN_MENU_FONT_PATH, 100)
    text1 = font.render("PIXEL RUN", True, (255, 255, 255))
    x = settings.WINDOW_SIZE[0] / 2 - text1.get_width() / 2
    screen.blit(text1, (x, 0))

    font = pygame.font.Font(settings.MAIN_MENU_FONT_PATH, 50)
    text2 = font.render("Press Enter to play", True, (255, 255, 255))
    x = settings.WINDOW_SIZE[0] / 2 - text2.get_width() / 2
    screen.blit(text2, (x, 500))

    text3 = font.render("Press R to restart the game", True, (255, 255, 255))
    x = settings.WINDOW_SIZE[0] / 2 - text3.get_width() / 2
    screen.blit(text3, (x, 600))