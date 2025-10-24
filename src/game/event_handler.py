"""Event handler"""


import pygame
from .create_game_objects import create_game_objects


def event_handler(self):
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Keys
        if event.type == pygame.KEYDOWN:
            # Changing game modes
            if event.key == pygame.K_RETURN:
                self.game_type = "game" if self.game_type == "mainmenu" else "mainmenu"

            # Restart
            elif event.key == pygame.K_r:
                if self.game_type == "game":
                    create_game_objects(self)
                    self.game_type = "game"

                else:
                    pass
