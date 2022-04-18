from src.engine.physics import physics as physics
from src.engine.physics.physics import DynamicObject


class Chest(physics.Object):
    def __init__(self, sprite, scale, x, y, name="undefinedBall", mass = 10):
        physics.Object.__init__(self, sprite, scale, x, y, name, mass)
        self.x = x
        self.y = y
