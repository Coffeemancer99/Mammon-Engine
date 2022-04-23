import random
import src.minigame.fruitPanic.fruit as fruit
import src.engine.scenecreator.tile as tile
import src.minigame.fruitPanic.handController as player
import pygame
import time as time
import src.minigame.teamMasher.masher as masher

import src.minigame.physicsTest.ball as ball

class cannon():
    def __init__(self):
        self.loaded = None
        pass

    def addAmmo(self):
        pass

    def fireCannon(self):
        pass

class cannonLoader():
    def __init__(self):
        self.carryingBall = None
        pass
        pass

    def pickUpBall(self, cannonBall):
        pass

    def placeBall(self, cannon):
        pass

class cannonBall(ball.Ball):
    def __init__(self, sprite, scale, x, y, lifetime, timerEnabled, name="undefinedCanBall", mass = 10, maxpower = defMaxPow):
        ball.Ball.__init__(self, sprite, scale, x, y, name, mass, maxpower)
        self.lifetime = lifetime
        self.durTime = timer(3, 60)
        self.alive = True
        self.timerEnabled = timerEnabled

class Ball(DynamicObject):
    def __init__(self, sprite, scale, x, y, lifetime, timerEnabled, name="undefinedBall", mass = 10, maxpower = defMaxPow):
        DynamicObject.__init__(self, sprite, scale, x, y, name, mass)
        self.power = 0
        self.angle = 0
        self.maxpower = maxpower
        self.lifetime = lifetime
        self.durTimer = timer(3, 60)
        self.alive = True
        self.timerEnabled = timerEnabled

"""
import random
import src.minigame.fruitPanic.fruit as fruit
import src.engine.scenecreator.tile as tile
import src.minigame.fruitPanic.handController as player
import pygame
import time as time
import src.minigame.teamMasher.masher as masher
class cannon():
    def __init__(self):
        self.loaded = False
        pass

    def addAmmo(self):
        self.loaded = True
        pass

    def fireCannon(self):
        if self.loaded == True:
            self.loaded = False
            return True
        return False

class cannonLoader():
    def __init__(self):
        self.carryingBall = False
        pass

    def pickUpBall(self, cannonBall):
        self.carryingBall=True

    def placeBall(self, cannon):
        self.carryingBall=False

class cannonBall():
    def __init__(self, x, y):
        pass"""