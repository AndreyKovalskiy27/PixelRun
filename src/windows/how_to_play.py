from.window import BaseWindow
from ui.text import Text


class HowToPlayWindow(BaseWindow):
    def __init__(self):
        super().__init__()

        self.title = Text((550, 0), "PIXEL TUTORIAL", 100, True)
        self.text = """Main game:
Press A, W, D, Space and arrow keys to move
You'll need to avoid pink triangles.
Sniper enemy doesn't kill you but he shoots
bullet and they can kill you.
While running don't forget to collect yellow
coins to use them in the shop!

Shop:
In shop you can buy shield you can use in game.
Shield makes you invinsible for 10 seconds.
You can also buy cool skins for your character!

Settings:
You can change music's and sound effects
volume in settings.
You can chose game difficulties (Higher
difficulty = More coins)
Also you can set you own music for the game!
"""
        self.text_rendered = Text((540, 130), self.text, 25)
        self.text1 = Text((0, 100), "How to play", 30, True)

    def draw(self, screen):
        super().draw(screen)
        if self.is_on:
            self.title.draw(screen)
            self.text_rendered.draw(screen)
            self.text1.draw(screen)
