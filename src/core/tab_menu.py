import settings
from ui.text import Text


class TabMenu:
    def __init__(self):
        self.is_on = False
        self.text = Text((10, 75), "", 30)

    def draw(self, screen):
        if self.is_on:
            self.text.draw(screen)

    def update_text(self, fps, difficulty, song):
        text = f"""PixelRun {settings.VERSION} BETA by angrymuncifan2888
FPS: {fps}
Current difficulty: {difficulty}
Current song: {song}"""
        self.text.change_text(text)
