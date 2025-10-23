"""Games main menu"""


import pygame
import settings


def draw_main_menu(screen):
    """Draw main menu"""
    font = pygame.font.Font(settings.FONT_PATH, 100)
    text1 = font.render("PIXEL RUN", True, settings.TEXT_COLOR)
    x = settings.WINDOW_SIZE[0] / 2 - text1.get_width() / 2
    screen.blit(text1, (x, 0))

    font = pygame.font.Font(settings.FONT_PATH, 50)
    text2 = font.render("Press Enter to play", True, settings.TEXT_COLOR)
    x = settings.WINDOW_SIZE[0] / 2 - text2.get_width() / 2
    screen.blit(text2, (x, 300))

    text3 = font.render("Press R to restart the game", True, settings.TEXT_COLOR)
    x = settings.WINDOW_SIZE[0] / 2 - text3.get_width() / 2
    screen.blit(text3, (x, 400))

    text4 = font.render("Press T slow down the game", True, settings.TEXT_COLOR)
    x = settings.WINDOW_SIZE[0] / 2 - text4.get_width() / 2
    screen.blit(text4, (x, 500))

    text5 = font.render("Hi Shreshail :)", True, settings.TEXT_COLOR)
    x = settings.WINDOW_SIZE[0] / 2 - text5.get_width() / 2
    screen.blit(text5, (x, 600))