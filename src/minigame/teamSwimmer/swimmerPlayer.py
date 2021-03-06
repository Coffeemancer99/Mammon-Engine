import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
from src.engine.graphics.spritegen import *
import src.engine.physics.terrain as terrain
import src.minigame.exampleGame.myObjects as myObjects
import pygame
from src.minigame.timer.timer import timer as timer
framerate = 60
weightPunish = 0.075
class swimmerPlayer(DynamicObject):
    def __init__(self, sprite, scale, x, y, objects, playerAControls, playerBControls, maxHeight, timerEnabled=False, name="undefinedBall", mass = 10):
        DynamicObject.__init__(self, sprite, scale, x, y, objects, name, mass)
        #Player A controls the left/right movement
        #Player B controls the jump/float movement
        self.playerAControls = playerAControls
        self.playerBControls = playerBControls
        self.alive = True
        if(playerAControls != None and playerBControls != None):
            self.left = playerAControls["left"]
            self.right = playerAControls["right"]
            self.up = playerBControls["up"]
        self.timer = timer(0.5, framerate)
        self.paralyzed = False
        self.facingRight = True
        self.score = 0
        self.maxHeight = maxHeight
        self.paralyzedTimer = timer(1.5, framerate)
        self.consec = 0
        self.x = x
        self.y = y
        self.storedCoins = 0
        self.touchingCorner = False
        self.weight = 0
        self.textActive = False
        self.timerEnabled = timerEnabled


    def floatSub(self, buttons):
        noMatch = True
        #If the player is at the spawning zone or paralyzed, just make them fall
        if self.y<self.maxHeight or self.paralyzed:
            self.momY += 0.35 + (weightPunish*self.weight)
            return
        #Iterate through the list of buttons gained from the event handler
        for things in buttons:
            if self.up == things.key: #If the up button was pressed (Prevents just holding the button up)
                self.momY -= 7 + (weightPunish*self.weight)#Make them float up
                noMatch = False #Prevent them from falling later
        if(noMatch): #If their up button was not pressed, then they should fall
            self.momY += 0.35 + (weightPunish*self.weight)

    def takeInputs(self, objects):
        if(self.paralyzedTimer.isFinished()):
            self.paralyzedTimer = timer(1.5, framerate)
            self.paralyzed=False
        elif self.paralyzed:
            self.paralyzedTimer.decrement()
        if(self.paralyzed):
            return
        key = pygame.key.get_pressed()
        if key[self.left]:
            self.momX -= 2 + (weightPunish*self.weight)
            if(self.facingRight):
                self.sprite = pygame.transform.flip(self.sprite, True, False)
                self.facingRight=False

        if key[self.right]:
            self.momX += 2 - (weightPunish*self.weight)
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

    def depositCoins(self):
        self.storedCoins += self.score
        self.score=0

    def adjustWeight(self):
        if(self.score>9):
            self.weight=4
        elif(self.score>6):
            self.weight=3
        elif(self.score>3):
            self.weight=2
        elif(self.score>0):
            self.weight=1
        else:
            self.weight=0

    def timeUntilDeletion(self):
        pass



