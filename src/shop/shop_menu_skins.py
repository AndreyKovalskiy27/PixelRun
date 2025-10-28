import pygame
import settings
from ui.button import Button
from ui.text import Text
from utils.message import Message
from utils.sound import SoundEffects


class Notifier:
    def __init__(self):
        self.not_enought_coins_message = Message("You don't have enought coins, loser", (255, 0, 0))
        self.skin_bought = Message("Skin succefly bought!", (0, 255, 0))
        self.skin_equiped = Message("Skin succefly equiped!", (0, 255, 0))
        self.skin_is_equiped = Message("Skin is already equiped", (255, 0, 0))

        self.messages_list = {
            "not_enought_coins": self.not_enought_coins_message,
            "skin_bought": self.skin_bought,
            "skin_equiped": self.skin_equiped,
            "skin_is_already_equiped": self.skin_is_equiped
        }

    def show(self, id):
        for msg_id, msg in self.messages_list.items():
            if id == msg_id:
                msg.show()

            else:
                msg.hide()

    def draw(self, screen):
        self.not_enought_coins_message.draw(screen)
        self.skin_bought.draw(screen)
        self.skin_equiped.draw(screen)
        self.skin_is_equiped.draw(screen)


class ShopMenuSkins:
    def __init__(self, shop_util):
        self.shop_util = shop_util
        self.title = Text((0, 0),  "PIXEL SKINS", 100, True)
        self.button_buy = Button((0, 550), "Buy ({price} coins)", button_size=(300, 75), center_x=True)
        self.button_left = Button((410, 0), "<", button_size=(100, 100), size=100, center_y=True)
        self.button_right = Button((1290, 0), ">", button_size=(100, 100), size=100, center_y=True)
        self.button_back = Button((10, 10), "<", button_size=(50, 50))
        self.current_skin = 0
        self.notifier = Notifier()

        self.skins = []
        for skin in self.shop_util.skin_base.values():
            self.skins.append(skin)

    def draw(self, screen, event):
        self.title.draw(screen)
        self.notifier.draw(screen)
        self.button_left.draw(screen)
        self.button_right.draw(screen)
        self.button_back.draw(screen)

        try:
            skin_obj = self.skins[self.current_skin]

            if not skin_obj.is_bought:
                self.button_buy.set_text(f"Buy ({skin_obj.price} coins)")

            else:
                if skin_obj.is_equiped:
                    self.button_buy.set_text("Equipped")

                else:
                    self.button_buy.set_text("Equip")

            skin_image = pygame.image.load(skin_obj.sprites[0])
            skin_image = pygame.transform.scale(skin_image, (200, 200))
            skin_image_x = settings.WINDOW_SIZE[0] / 2 - skin_image.get_width() / 2
            skin_image_y = settings.WINDOW_SIZE[1] / 2 - skin_image.get_height() / 2
            screen.blit(skin_image, (skin_image_x, skin_image_y))
            self.button_buy.draw(screen)

            text1 = Text((0, skin_image_y - 50), skin_obj.title, 30, True)
            text2 = Text((0, skin_image_y + 200), skin_obj.description, 30, True)
        
            text1.draw(screen)
            text2.draw(screen)

        except IndexError:
            self.current_skin = 0

        if self.button_right.is_clicked(event):
            if self.current_skin < len(self.skins) - 1:
                self.current_skin += 1

        elif self.button_left.is_clicked(event):
            if self.current_skin > 0:
                self.current_skin -= 1

        elif self.button_buy.is_clicked(event, False):
            if not skin_obj.is_bought:
                try:
                    self.shop_util.buy_skin(skin_obj.id)
                    self.notifier.show("skin_bought")
                    SoundEffects.buy()

                except:
                    self.notifier.show("not_enought_coins")
                    SoundEffects.error()
    
            else:
                if not skin_obj.is_equiped:
                    self.shop_util.equip_skin(skin_obj.id)
                    self.notifier.show("skin_equiped")
                    SoundEffects.buy()
    
                else:
                    self.notifier.show("skin_is_already_equiped")
                    SoundEffects.error()

        elif self.button_back.is_clicked(event):
            return True
