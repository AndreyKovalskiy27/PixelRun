import pygame
import settings
from ui.button import Button


class PauseWindow:
    def __init__(self):
        self.window_box = pygame.Surface((300, 300))
        self.window_box.fill((25, 25, 25))
        self.window_box_x = settings.WINDOW_SIZE[0] / 2 - self.window_box.get_width() / 2
        self.window_box_y = settings.WINDOW_SIZE[1] / 2 - self.window_box.get_height() / 2

        self.button_main_menu = Button((0, 275), "Main menu", button_size=(250, 100), center_x=True)
        self.button_continue = Button((0, 425), "Continue", button_size=(250, 100), center_x=True)
        self.is_on = False

    def draw(self, screen, event):
        if self.is_on:
            screen.blit(self.window_box, (self.window_box_x, self.window_box_y))
            self.button_main_menu.draw(screen)
            self.button_continue.draw(screen)

            if self.button_main_menu.is_clicked(event):
                return "mainmenu"

            elif self.button_continue.is_clicked(event):
                return "continue"
