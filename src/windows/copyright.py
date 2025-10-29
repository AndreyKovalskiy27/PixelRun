from ui.text import Text
from .window import BaseWindow


class CopyrightWindow(BaseWindow):
    def __init__(self):
        super().__init__()

        self.text1 = Text((550, 0), "PIXEL COPYRIGHT", 100, True)
        self.text2 = Text((0, 300), "Shop/main menu theme: 1nicopatty", 30, True)
        self.text3 = Text((0, 350), "Default game theme: LSPlash", 30, True)
        self.text4 = Text((0, 400), "Source code/programer: angrymuncifan2888", 30, True)
        self.text5 = Text((0, 450), "Thanks to Python and PyGame developers!", 30, True)

    def draw(self, screen):
        super().draw(screen)
        if self.is_on:
            self.text1.draw(screen)
            self.text2.draw(screen)
            self.text3.draw(screen)
            self.text4.draw(screen)
            self.text5.draw(screen)
