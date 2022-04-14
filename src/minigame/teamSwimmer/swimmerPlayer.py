import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
from src.engine.physics.spritegen import *
import src.engine.physics.terrain as terrain
import src.minigame.exampleGame.myObjects as myObjects
import pygame
import time
from src.minigame.timer.timer import timer as timer
framerate = 60
class swimmerPlayer(DynamicObject):
    def __init__(self, sprite, scale, x, y, objects, playerAControls, playerBControls, name="undefinedBall", mass = 10):
        DynamicObject.__init__(self, sprite, scale, x, y, objects, name, mass)
        #Player A controls the left/right movement
        #Player B controls the jump/float movement
        self.playerAControls = playerAControls
        self.playerBControls = playerBControls
        self.left = playerAControls["left"]
        self.right = playerAControls["right"]
        self.up = playerBControls["up"]
        self.timer = timer(0.5, framerate)

    def floatSub(self, buttons):
        noMatch = True
        for things in buttons:

            if self.up == things.key:
                print("in it")
                self.momY -= 7
                noMatch = False
        if(noMatch):
            self.momY += 0.35

    def takeInputs(self, objects):
        key = pygame.key.get_pressed()
        if key[self.left]:
            self.momX -= 2

        if key[self.right]:
            self.momX += 2

    def update(self, airRes=physics.airRes, minMom=physics.minMom, maxMom=None): # retrieves default values from physics module
        try: self.takeInputs(pygame.key.get_pressed())
        except: pass # pygame not initialized, so ignore takeInputs
        DynamicObject.update(self, airRes, minMom, maxMom)


