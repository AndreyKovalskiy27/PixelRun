"""Game levels"""


import objects


class Level:
    """Base class for all leves"""
    def __init__(self):
        self.objects = []

    def draw(self, screen):
        """Draw all level objects"""
        for obj in self.objects:
            obj.draw(screen)

    def update(self, player):
        """Update all level objects"""
        was_killed = False
        for obj in self.objects:
            obj.move_with_background()  # Moving level with the background
            if type(obj) == objects.Platform:
                obj.stop_player(player)

            elif type(obj) == objects.Coin:
                if obj.check_collision(player):
                    obj.was_collected = True
                    return "coin"

            else:
                if obj.check_collision(player):
                    was_killed = "killed"

                if type(obj) == objects.SniperEnemy:
                    obj.update()

        return was_killed

class Level_1(Level):
    """Level 1"""
    def __init__(self):
        super().__init__()

        self.objects = [objects.Platform((509, 523)),
                        objects.Platform((900, 315)),
                        objects.Platform((661, 50)),
                        objects.Platform((1227, 126)),
                        objects.Platform((1297, 558)),
                        objects.TriangleEnemy((1327, 448)),
                        objects.TriangleEnemy((786, 685)),
                        objects.TriangleEnemy((925, 685)),
                        objects.TriangleEnemy((1075, 685)),
                        objects.TriangleEnemy((1222, 685)),
                        objects.TriangleEnemy((1372, 685)),
                        objects.TriangleEnemy((1522, 685)),]
class Level_2(Level):
    """Level 2"""
    def __init__(self):
        super().__init__()

        self.objects = [objects.Platform((174, 158)),
                        objects.TriangleEnemy((199, 50)),
                        objects.Platform((509, 523)),
                        objects.Platform((1122, 350)),
                        objects.TriangleEnemy((997, 687)),
                        objects.TriangleEnemy((1503, 687)),
                        objects.SniperEnemy((1600, 189))]

class Level_3(Level):
    """Level 3"""
    def __init__(self):
        super().__init__()

        self.objects = [
            objects.Platform((200, 480)),
            objects.Platform((600, 300)),
            objects.TriangleEnemy((630, 200)),
            objects.Platform((950, 520)),
            objects.TriangleEnemy((975, 420)),
            objects.Platform((1350, 250)),
            objects.TriangleEnemy((1380, 140)),
            objects.TriangleEnemy((1500, 687)),
            objects.SniperEnemy((1650, 200))  # Sniper at the end
        ]


class Level_4(Level):
    """Level 4"""
    def __init__(self):
        super().__init__()

        self.objects = [
            objects.Platform((150, 550)),
            objects.TriangleEnemy((175, 450)),
            objects.Platform((520, 380)),
            objects.TriangleEnemy((540, 280)),
            objects.Platform((900, 600)),
            objects.Platform((1180, 310)),
            objects.TriangleEnemy((1205, 210)),
            objects.TriangleEnemy((1420, 687)),
            objects.SniperEnemy((1620, 230))  # Sniper at the end
        ]


class Level_5(Level):
    """Level 5"""
    def __init__(self):
        super().__init__()

        self.objects = [
            objects.Platform((180, 200)),
            objects.TriangleEnemy((210, 100)),
            objects.Platform((600, 500)),
            objects.TriangleEnemy((620, 400)),
            objects.Platform((980, 350)),
            objects.Platform((1260, 580)),
            objects.TriangleEnemy((1290, 480)),
            objects.TriangleEnemy((1460, 687)),
            objects.TriangleEnemy((1570, 687)),
            objects.SniperEnemy((1680, 220))  # Sniper at the end
        ]


class Level_6(Level):
    """Level 6"""
    def __init__(self):
        super().__init__()

        self.objects = [
            objects.Platform((150, 550)),
            objects.TriangleEnemy((200, 500)),
            objects.Platform((500, 380)),
            objects.SniperEnemy((1200, 200)),
            objects.Coin((170, 500)),
            objects.Coin((520, 330))
        ]


class Level_7(Level):
    """Level 7"""
    def __init__(self):
        super().__init__()

        self.objects = [
            objects.Platform((100, 400)),
            objects.TriangleEnemy((150, 350)),
            objects.Platform((400, 500)),
            objects.SniperEnemy((1000, 150)),
            objects.Coin((120, 350)),
            objects.Coin((420, 450))
        ]


class Level_8(Level):
    """Level 8"""
    def __init__(self):
        super().__init__()

        self.objects = [
            objects.Platform((200, 550)),
            objects.TriangleEnemy((250, 500)),
            objects.Platform((500, 400)),
            objects.SniperEnemy((1200, 200)),
            objects.Coin((220, 500)),
            objects.Coin((520, 350))
        ]


class Level_9(Level):
    """Level 9"""
    def __init__(self):
        super().__init__()

        self.objects = [
            objects.Platform((150, 500)),
            objects.TriangleEnemy((200, 450)),
            objects.Platform((450, 350)),
            objects.SniperEnemy((1100, 250)),
            objects.Coin((170, 450)),
            objects.Coin((470, 300))
        ]


class Level_10(Level):
    """Level 10"""
    def __init__(self):
        super().__init__()

        self.objects = [
            objects.Platform((100, 600)),
            objects.TriangleEnemy((150, 550)),
            objects.Platform((400, 400)),
            objects.SniperEnemy((1000, 200)),
            objects.Coin((120, 550)),
            objects.Coin((420, 350))
        ]
