"""Games main menu"""


from ui import Button, Text


class MainMenu:
    """Games main menu"""
    def __init__(self):
        """Create all menu objects"""
        self.text1 = Text((550, 0), "PIXEL RUN", 100, True)
        self.press_enter_button = Button((650, 196), "Press enter to play")
        self.button_shop = Button((650, 400), "SHOP")


    def draw_main_menu(self, screen):
        """Draw main menu"""
        self.text1.draw(screen)
        self.press_enter_button.draw(screen)
        self.press_enter_button.update()

        self.button_shop.draw(screen)
        self.button_shop.update()
