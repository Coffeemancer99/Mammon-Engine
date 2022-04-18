from src.engine.physics import physics as physics
from src.engine.physics.physics import DynamicObject


class patientPlayer(physics.Object):
    def __init__(self, sprite, scale, x, y, timerEnabled=False, name="undefinedBall", mass = 10):
        physics.Object.__init__(self, sprite, scale, x, y, name, mass)
        self.x = x
        self.y = y
        self.timerEnabled = timerEnabled
        self.alive = True

    def timeUntilDeletion(self):
        pass