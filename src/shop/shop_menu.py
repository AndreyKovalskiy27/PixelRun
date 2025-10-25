"""Shop's main menu"""


from ui import Button, Text


class ShopMenu:
    """Shop's menu"""
    def __init__(self):
        self.title = Text((0, 0),  "PIXEL SHOP", 100, True)
        self.button_items = Button((10, 0), "ITEMS", (800, 600), 100, False, True)
        self.button_skins = Button((990, 0), "SKINS", (800, 600), 100, False, True)
        self.button_back = Button((10, 10), "<", (50, 50))

    def draw(self, screen):
        """Draw shop menu"""
        self.title.draw(screen)
        self.button_items.draw(screen)
        self.button_items.update()

        self.button_skins.draw(screen)
        self.button_skins.update()

        self.button_back.draw(screen)
        self.button_back.update()
