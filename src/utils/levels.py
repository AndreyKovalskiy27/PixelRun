from objects.coin import Coin
from objects.platform import Platform
from objects.sniper_enemy import SniperEnemy
from objects.triangle_enemy import TriangleEnemy


class Level:
    """Base class for all levels"""
    def __init__(self):
        self.objects = []

    def draw(self, screen):
        for obj in self.objects:
            obj.draw(screen)

    def update(self, player):
        was_killed = False
        for obj in self.objects:
            obj.move_with_background()
            if isinstance(obj, Platform):
                obj.stop_player(player)
            elif isinstance(obj, Coin):
                if obj.check_collision(player):
                    obj.was_collected = True
                    return "coin"
            else:
                if obj.check_collision(player):
                    was_killed = "killed"
                if isinstance(obj, SniperEnemy):
                    obj.update()
        return was_killed


class Level_1(Level):
    def __init__(self):
        super().__init__()
        self.objects = [
            Platform((509, 523)),
            Platform((900, 315)),
            Platform((661, 50)),
            Platform((1227, 126)),
            Platform((1297, 558)),
            TriangleEnemy((1327, 448)),
            TriangleEnemy((786, 685)),
            TriangleEnemy((925, 685)),
            TriangleEnemy((1075, 685)),
            TriangleEnemy((1222, 685)),
            TriangleEnemy((1372, 685)),
            TriangleEnemy((1522, 685)),
        ]


class Level_2(Level):
    def __init__(self):
        super().__init__()
        self.objects = [
            Platform((174, 158)),
            TriangleEnemy((199, 50)),
            Platform((509, 523)),
            Platform((1122, 350)),
            TriangleEnemy((997, 687)),
            TriangleEnemy((1503, 687)),
            SniperEnemy((1600, 189))
        ]


class Level_3(Level):
    def __init__(self):
        super().__init__()
        self.objects = [
            Platform((200, 480)),
            Platform((600, 300)),
            TriangleEnemy((630, 200)),
            Platform((950, 520)),
            TriangleEnemy((975, 420)),
            Platform((1350, 250)),
            TriangleEnemy((1380, 140)),
            TriangleEnemy((1500, 687)),
            SniperEnemy((1650, 200))
        ]


class Level_4(Level):
    def __init__(self):
        super().__init__()
        self.objects = [
            Platform((150, 550)),
            TriangleEnemy((175, 450)),
            Platform((520, 380)),
            TriangleEnemy((540, 280)),
            Platform((900, 600)),
            Platform((1180, 310)),
            TriangleEnemy((1205, 210)),
            TriangleEnemy((1420, 687)),
            SniperEnemy((1620, 230))
        ]


class Level_5(Level):
    def __init__(self):
        super().__init__()
        self.objects = [
            Platform((180, 200)),
            TriangleEnemy((210, 100)),
            Platform((600, 500)),
            TriangleEnemy((620, 400)),
            Platform((980, 350)),
            Platform((1260, 580)),
            TriangleEnemy((1290, 480)),
            TriangleEnemy((1460, 687)),
            TriangleEnemy((1570, 687)),
            SniperEnemy((1680, 220))
        ]


class Level_6(Level):
    def __init__(self):
        super().__init__()
        self.objects = [
            Platform((150, 550)),
            TriangleEnemy((200, 500)),
            Platform((500, 380)),
            SniperEnemy((1200, 200)),
            Coin((170, 500)),
            Coin((520, 330))
        ]


class Level_7(Level):
    def __init__(self):
        super().__init__()
        self.objects = [
            Platform((100, 400)),
            TriangleEnemy((150, 350)),
            Platform((400, 500)),
            SniperEnemy((1000, 150)),
            Coin((120, 350)),
            Coin((420, 450))
        ]


class Level_8(Level):
    def __init__(self):
        super().__init__()
        self.objects = [
            Platform((200, 550)),
            TriangleEnemy((250, 500)),
            Platform((500, 400)),
            SniperEnemy((1200, 200)),
            Coin((220, 500)),
            Coin((520, 350))
        ]


class Level_9(Level):
    def __init__(self):
        super().__init__()
        self.objects = [
            Platform((150, 500)),
            TriangleEnemy((200, 450)),
            Platform((450, 350)),
            SniperEnemy((1100, 250)),
            Coin((170, 450)),
            Coin((470, 300))
        ]


class Level_10(Level):
    def __init__(self):
        super().__init__()
        self.objects = [
            Platform((100, 600)),
            TriangleEnemy((150, 550)),
            Platform((400, 400)),
            SniperEnemy((1000, 200)),
            Coin((120, 550)),
            Coin((420, 350))
        ]
