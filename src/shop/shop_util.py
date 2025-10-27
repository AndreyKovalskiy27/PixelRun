import pickle
import settings
import os
from dataclasses import dataclass


@dataclass
class Skin:
    title: str
    price: int
    description: str
    sprites: list
    id: str
    is_bought: bool = False
    is_equiped: bool = False


class ShopUtil:
    def __init__(self):
        self.shop_path = settings.SHOP_PATH
        self.shop_data = self.load_shop_util()
        self.shield_price = 20

        self.skin_base = {
            "player": Skin(
                "Player", 0, "First and default skin!",
                [settings.PLAYER_STANDING_SPIRTE_PATH,
                 settings.PLAYER_RUNNING_SPRITE_PATH,
                 settings.PLAYER_RUNNING2_SPTIRE_PATH], "player"
            ),
            "angry_munci": Skin(
                "Angry Munci", 50, "ANGRY MUNCI ON TOP!!!",
                [settings.ANGRY_MUNCI_STANDING_SPRITE_PATH,
                 settings.ANGRY_MUNCI_STANDING_SPRITE_PATH,
                 settings.ANGRY_MUNCI_STANDING_SPRITE_PATH], "angry_munci"
            )
        }

        self.skins = self.skin_base.copy()
        self._sync_skins_with_data()

    def _sync_skins_with_data(self):
        for skin_id in self.shop_data["owned_skins"]:
            if skin_id in self.skins:
                self.skins[skin_id].is_bought = True
        equipped = self.shop_data.get("equipped_skin", "player")
        if equipped in self.skins:
            self.skins[equipped].is_equiped = True

    def load_shop_util(self):
        try:
            with open(self.shop_path, "rb") as file:
                return pickle.load(file)
        except Exception:
            return {"coins": 0, "shield": 0, "owned_skins": ["player"], "equipped_skin": "player"}

    def save(self):
        with open(self.shop_path, "wb") as file:
            pickle.dump(self.shop_data, file)

    def add_coins(self, amount=1):
        self.shop_data["coins"] += amount
        self.save()

    def delete_coins(self, amount=20):
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

    def buy_skin(self, skin_id: str):
        if skin_id not in self.skins:
            raise Exception("Skin not found")

        skin = self.skins[skin_id]
        if skin.is_bought:
            raise Exception("Skin already owned")

        if self.shop_data["coins"] < skin.price:
            raise Exception("Not enough coins")

        self.delete_coins(skin.price)
        skin.is_bought = True
        self.shop_data["owned_skins"].append(skin_id)
        self.save()

    def equip_skin(self, skin_id: str):
        if skin_id not in self.skins:
            raise Exception("Skin not found")

        skin = self.skins[skin_id]
        if not skin.is_bought:
            raise Exception("Skin not owned")

        for s in self.skins.values():
            s.is_equiped = False

        skin.is_equiped = True
        self.shop_data["equipped_skin"] = skin_id
        self.save()

    def current_skin(self) -> Skin:
        equipped_id = self.shop_data.get("equipped_skin", "player")
        return self.skins.get(equipped_id, self.skins["player"])

    @property
    def shields(self):
        return self.shop_data["shield"]

    @property
    def coins(self):
        return self.shop_data["coins"]
