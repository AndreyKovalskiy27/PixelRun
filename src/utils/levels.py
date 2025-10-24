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

            else:
                if obj.check_collision(player):
                    was_killed = True

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
