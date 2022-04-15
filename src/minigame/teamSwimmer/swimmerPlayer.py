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
    def __init__(self, sprite, scale, x, y, objects, playerAControls, playerBControls, maxHeight, name="undefinedBall", mass = 10):
        DynamicObject.__init__(self, sprite, scale, x, y, objects, name, mass)
        #Player A controls the left/right movement
        #Player B controls the jump/float movement
        self.playerAControls = playerAControls
        self.playerBControls = playerBControls
        self.left = playerAControls["left"]
        self.right = playerAControls["right"]
        self.up = playerBControls["up"]
        self.timer = timer(0.5, framerate)
        self.paralyzed = False
        self.facingRight = True
        self.score = 0
        self.maxHeight = maxHeight
        self.paralyzedTimer = timer(1.5, framerate)

    def floatSub(self, buttons):
        noMatch = True
        #If the player is at the spawning zone or paralyzed, just make them fall
        if self.y<self.maxHeight or self.paralyzed:
            self.momY += 0.35
            return
        #Iterate through the list of buttons gained from the event handler
        for things in buttons:
            if self.up == things.key: #If the up button was pressed (Prevents just holding the button up)
                self.momY -= 7 #Make them float up
                noMatch = False #Prevent them from falling later
        if(noMatch): #If their up button was not pressed, then they should fall
            self.momY += 0.35

    def takeInputs(self, objects):
        if(self.paralyzedTimer.isFinished()):
            self.paralyzedTimer = timer(2, framerate)
            self.paralyzed=False
        elif self.paralyzed:
            self.paralyzedTimer.decrement()
        if(self.paralyzed):
            return
        key = pygame.key.get_pressed()
        if key[self.left]:
            self.momX -= 2
            if(self.facingRight):
                self.sprite = pygame.transform.flip(self.sprite, True, False)
                self.facingRight=False

        if key[self.right]:
            self.momX += 2
            if(not self.facingRight):
                self.sprite = pygame.transform.flip(self.sprite, True, False)
                self.facingRight=True

    def update(self, airRes=physics.airRes, minMom=physics.minMom, maxMom=None): # retrieves default values from physics module
        try: self.takeInputs(pygame.key.get_pressed())
        except: pass # pygame not initialized, so ignore takeInputs
        DynamicObject.update(self, airRes, minMom, maxMom)

    def changeScore(self, quantity):
        self.score += quantity
        if(self.score<0):
            self.score = 0



