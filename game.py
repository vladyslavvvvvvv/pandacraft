from direct.showbase.ShowBase import ShowBase
import builtins
from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = Mapmanager()
        self.land.loadLand("land.txt")
        builtins.base.camLens.setFov(90)


game = Game()
game.run()