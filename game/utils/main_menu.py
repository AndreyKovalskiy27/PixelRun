"""Games main menu"""


import pygame
import settings


def draw_main_menu(screen):
    """Draw main menu"""
    text1_render = pygame.font.Font(settings.MAIN_MENU_FONT_PATH, 100)
    text1 = text1_render.render("PIXEL RUN", False, (255, 255, 255))
    x = settings.WINDOW_SIZE[0] / 2 - text1.get_width() / 2
    screen.blit(text1, (x, 0))

