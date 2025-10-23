"""Tab menu"""


import pygame
import settings


def draw_tab_menu(screen, fps):
    """Draw tab menu on the screen"""
    font = pygame.font.Font(settings.FONT_PATH, 30)
    text = f"""
TAB MENU
I really wanted to make a tab menu but
for some reason it makes game lag alot so there's nothing here(
FPS is {fps}
"""

    y = 0
    for line in text.split("\n"):
        render = font.render(line, True, settings.TEXT_COLOR)
        screen.blit(render, (10, y))
        y += 30
