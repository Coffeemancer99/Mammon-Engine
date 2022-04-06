import random
import src.minigame.fruitPanic.fruit as fruit
import src.engine.scenecreator.tile as tile
import src.minigame.fruitPanic.handController as player
import pygame
import time as time
import src.minigame.teamMasher.masher as masher
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

class cannonBall():
    def __init__(self, x, y):
        pass
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