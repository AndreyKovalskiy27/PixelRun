import pickle
import settings


class ShopUtil:
    def __init__(self):
        self.shop_path = settings.SHOP_PATH
        self.shop_data = self.load_shop_util()
        self.shield_price = 5

    def load_shop_util(self):
        try:
            with open(self.shop_path, "rb") as file:
                return pickle.load(file)
        except Exception:
            return {"coins": 0, "shield": 0}

    def save(self):
        with open(self.shop_path, "wb") as file:
            pickle.dump(self.shop_data, file)

    def add_coins(self, amount=1):
        self.shop_data["coins"] += amount
        self.save()

    def delete_coins(self, amount=5):
        self.shop_data["coins"] = max(0, self.shop_data["coins"] - amount)
        self.save()

    def buy_shields(self, amount=1):
        total_cost = amount * self.shield_price
        if self.shop_data["coins"] >= total_cost:
            self.shop_data["shield"] += amount
            self.delete_coins(total_cost)
            self.save()

        else:
            raise Exception("Not enough coins")

    def delete_shields(self, amount=1):
        self.shop_data["shield"] = max(0, self.shop_data["shield"] - amount)
        self.save()

    @property
    def shields(self):
        return self.shop_data["shield"]

    @property
    def coins(self):
        return self.shop_data["coins"]
