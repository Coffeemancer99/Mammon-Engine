import pygame
import math
import sys # for flushing stdout for dev statements, remove later
import src.engine.physics.physics as physics
from src.engine.physics.physics import Object
from src.engine.physics.physics import DynamicObject
import src.minigame.physicsTest.ball as ball
from src.minigame.timer.timer import timer as timer

defMaxPow = 80
class CannonBall(ball.Ball):
    def __init__(self, sprite, scale, x, y, lifetime, timerEnabled, name="undefinedBall", mass=10, maxpower=defMaxPow):
        ball.Ball.__init__(self, sprite, scale, x, y, name="undefinedBall", mass=10,
                           maxpower=defMaxPow)
        self.lifetime = lifetime
        self.durTimer = timer(3, 60)
        self.alive = True
        self.timerEnabled = timerEnabled



    def launch(self):
        if(self.power == 0):
            return
        print("\r\rlaunched!            \n")
        print("power = " + str(self.power))
        print("angle = " + str(self.angle) + " = " + str(self.angle * 180 / math.pi))
        print("powX = " + str(self.power*math.cos(self.angle)))
        print("powY = " + str(self.power*math.sin(self.angle)))
        print("")


        self.momX += self.power*math.cos(self.angle)*2*self.scale
        self.momY -= self.power*math.sin(self.angle)*2*self.scale
        self.power = 30
        #self.angle = 0

    def timeUntilDeletion(self):
        self.durTimer.decrement()
        if(self.timerEnabled and self.durTimer.isFinished()):

            self.alive = False