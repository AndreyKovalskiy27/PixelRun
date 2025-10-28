import pygame
import settings
from ui.text import Text


class CopyrightWindow:
    def __init__(self):
        self.copyright_box = pygame.Surface((800, 600))
        self.copyright_box.fill((25, 25, 25))
        self.copyright_box_x = settings.WINDOW_SIZE[0] / 2 - self.copyright_box.get_width() / 2
        self.copyright_box_y = settings.WINDOW_SIZE[1] / 2 - self.copyright_box.get_height() / 2

        self.text1 = Text((550, 0), "PIXEL COPYRIGHT", 100, True)
        self.text2 = Text((0, 300), "Shop/main menu theme: 1nicopatty", 30, True)
        self.text3 = Text((0, 350), "Default game theme: LSPlash", 30, True)
        self.text4 = Text((0, 400), "Source code/programer: angrymuncifan2888", 30, True)
        self.text5 = Text((0, 450), "Thanks to Python and PyGame developers!", 30, True)

        self.copyright_on = False

    def draw(self, screen):
        if self.copyright_on:
            screen.blit(self.copyright_box, (
                self.copyright_box_x,
                self.copyright_box_y
            ))

            self.text1.draw(screen)
            self.text2.draw(screen)
            self.text3.draw(screen)
            self.text4.draw(screen)
            self.text5.draw(screen)
