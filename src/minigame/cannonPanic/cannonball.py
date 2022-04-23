import pygame
import math
import sys # for flushing stdout for dev statements, remove later
import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
import src.minigame.physicsTest.ball as ball
from src.minigame.physicsTest.ball import Ball
from src.minigame.timer.timer import timer as timer

defMaxPow = 80
class CannonBall(Ball):
    def __init__(self, sprite, scale, x, y, lifetime, timerEnabled, name="undefinedC-Ball", mass=10, maxpower= ball.defMaxPow):
        Ball.__init__(self, sprite, scale, x, y, name="undefinedBall", mass=10,
                           maxpower=defMaxPow)
        self.lifetime = lifetime
        self.durTimer = timer(3, 60)
        self.alive = True
        self.timerEnabled = timerEnabled

    def timeUntilDeletion(self):
        self.durTimer.decrement()
        if(self.timerEnabled and self.durTimer.isFinished()):
            self.alive = False
    def launch(self, resetAngle = False, resetPower = False):
        Ball.launch(self, resetAngle, resetPower)