import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
from src.engine.physics.spritegen import *
import src.engine.physics.terrain as terrain
import src.minigame.exampleGame.myObjects as myObjects
import pygame
import time
from src.minigame.timer.timer import timer as timer
framerate = 60

class seaItem(DynamicObject):
    def __init__(self, sprite, scale, x, y, objects, name="undefinedBall", mass = 10):
        DynamicObject.__init__(self, sprite, scale, x, y, objects, name, mass)
        self.isBad = False
        self.cost = 0

    def fall(self):
        self.momY += 0.35