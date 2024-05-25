from direct.showbase.ShowBase import ShowBase
import builtins
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = Mapmanager()
        self.land.loadLand("land.txt")
        self.hero = Hero((5,0,3), (self.land))
        builtins.base.camLens.setFov(90)


game = Game()
game.run()