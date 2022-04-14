import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
from src.engine.physics.spritegen import *
import src.engine.physics.terrain as terrain
import src.minigame.exampleGame.myObjects as myObjects
import pygame
import time

class swimmerPlayer(DynamicObject):
    def __init__(self, sprite, scale, x, y, objects, playerAControls, playerBControls, name="undefinedBall", mass = 10):
        DynamicObject.__init__(self, sprite, scale, x, y, objects, name, mass)
        #Player A controls the left/right movement
        #Player B controls the jump/float movement
        self.playerAControls = playerAControls
        self.playerBControls = playerBControls
