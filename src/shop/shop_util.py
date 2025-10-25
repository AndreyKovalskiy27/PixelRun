"""Class to work with shop file and controls user's skins, items, coins"""


import json
import settings


class ShopUtil:
    """Shop util"""
    def __init__(self):
        self.shop_path = settings.SHOP_PATH
        self.shop_data = self.load_shop()
        self.shield_price = 5

    def load_shop(self):
        """Load shop"""
        try:
            with open(self.shop_path, "r") as file:
                self.shop_data = json.load(file)
                return self.shop_data

        except Exception as exception:
            return {"coins": 0, "shield": 0}

    def save(self):
        """Save shop"""
        with open(self.shop_path, "w+") as file:
            json.dump(self.shop_data, file, indent=4)

    def add_coins(self, amount=1):
        """Add coins to player"""
        self.shop_data["coins"] += amount
        self.save()

    def delete_coins(self, amount=5):
        """Remove coins from the player"""
        self.shop_data["coins"] -= amount
        self.save()

    def add_shield(self, amount=1):
        """Add shield to player"""
        self.shop_data["shield"] += amount
        self.save()

    def delete_shields(self, amount=1):
        """Remove shields from the player"""
        self.shop_data["shield"] -= amount
        self.save()
