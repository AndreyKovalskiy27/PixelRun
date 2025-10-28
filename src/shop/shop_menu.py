"""Shop's main menu"""


from ui.button import Button
from ui.text import Text
from .shop_menu_items import ShopMenuItems
from .shop_menu_skins import ShopMenuSkins


class ShopMenu:
    """Shop's menu"""
    def __init__(self, shop_util):
        # Objects on the screen (text, buttons)
        self.title = Text((0, 0),  "PIXEL SHOP", 100, True)
        self.button_items = Button((10, 0), content="ITEMS", button_size=(800, 600), size=100, center_x=False, center_y=True)
        self.button_skins = Button((990, 0), "SKINS", 100, (800, 600), False, True)
        self.button_back = Button((10, 10), "<", button_size=(50, 50))
        self.shop_util = shop_util

        # Other
        self.menu_type = "mainmenu"
        self.items_menu = ShopMenuItems(self.shop_util)
        self.skins_menu = ShopMenuSkins(self.shop_util)

    def draw(self, screen, pygame_event):
        """Draw shop menu"""
        if self.menu_type == "mainmenu":
            self.title.draw(screen)
            self.button_items.draw(screen)
            self.button_skins.draw(screen)
            self.button_back.draw(screen)

            if self.button_items.is_clicked(pygame_event):
                self.menu_type = "items"

            elif self.button_skins.is_clicked(pygame_event):

                self.menu_type = "skins"

            elif self.button_back.is_clicked(pygame_event):
                return True

        elif self.menu_type == "items":
            res = self.items_menu.draw(screen, pygame_event)
            if res:
                self.menu_type = "mainmenu"

        elif self.menu_type == "skins":
            res = self.skins_menu.draw(screen, pygame_event)
            if res:
                self.menu_type = "mainmenu"

        coins_conuter = Text((1400, 25), f"Coins: {self.shop_util.coins}", 30, color=(255, 255, 0))
        coins_conuter.draw(screen)
