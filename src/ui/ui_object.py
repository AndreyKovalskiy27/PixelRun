import settings


class UiObject:
    def __init__(self, position, content, size, center_x=False, center_y=False):
        self.position = position
        self.size = size
        self.center_x = center_x
        self.center_y = center_y
        self.x, self.y = position

    def center_in_window(self, width, height):
        x = settings.WINDOW_SIZE[0] / 2 - width / 2 if self.center_x else self.x
        y = settings.WINDOW_SIZE[1] / 2 - height / 2 if self.center_y else self.y
        return x, y


    def draw(self, screen):
        raise NotImplementedError()