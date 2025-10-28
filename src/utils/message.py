from ui.text import Text
from .timer import Timer
import settings


class Message:
    def __init__(self, text, color, time=settings.MESSAGE_LASTS_FOR):
        self.text = Text((0, 750), text, 30, True, False, color)
        self.time = time
        self.timer = Timer(self.time)
        self.timer.start()
        self.is_active = False

    def show(self):
        self.is_active = True
        self.timer.reset()
        self.timer.start()

    def hide(self):
        self.is_active = False

    def draw(self, screen):
        if self.is_active:
            if not self.timer.update():
                self.text.draw(screen)

            else:
                self.is_active = False
                self.hide()
