import src.minigame.physicsTest.ball as ball
import pygame
import math
import sys
import src.minigame.cannonPanic.cannonball as cannonball
from src.minigame.timer.timer import timer as timer

from src.engine.physics import spritegen
scaleFancy = 0.05
defMaxPow = 80
class CannonPlayer(ball.Ball):
    def __init__(self, sprite, scale, x, y,  up, down, left, right, launch, primedBall, lifetime, timerEnabled, name="undefinedBall", mass = 10, maxpower = defMaxPow):
        ball.Ball.__init__(self, sprite, scale, x, y, name="undefinedBall", mass = 10, maxpower = defMaxPow)
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.launchKey = launch
        self.isLaunched = False
        self.alive = True
        self.primedBall = primedBall
        self.ready = True
        self.lifetime = lifetime
        self.durTimer = timer(3, 60)
        self.timerEnabled = timerEnabled

    def generateBall(self):
        cocoSprite = spritegen.grab_sprite("data/assets/sprites/goodSprites/coconut.png", scaleFancy*self.scale)
        yPos = self.y
        xPos = self.x
        mathyPos=(self.sprite.get_width()/2) * math.sin(self.angle+0.785398)
        mathxPos=(self.sprite.get_height()/2) * math.cos(self.angle+0.785398)

        # yPos -= mathyPos
        # xPos += mathxPos
        xPos += cocoSprite.get_width()
        yPos -=  cocoSprite.get_height()



        # yPos+=self.y + self.sprite.get_height()+ cocoSprite.get_height()*4
        # xPos+=self.x + +self.sprite.get_width()+cocoSprite.get_width()*4
        print("\nCannon pos is %f %f \n" %(self.x, self.y))
        print("\nBall pos is %f %f\n" %(xPos, yPos))
        coco = cannonball.CannonBall(cocoSprite, 1, xPos, yPos, 3, True, name="coco", mass=4, maxpower=80)
        return coco

    def reloadCannonball(self, ball):
        self.primedBall = ball

    def takeInputs(self, key):
        if key[self.right]:
            self.angle += .01
            self.angle = self.angle % 6.28


            print("\rangle = " + str(self.angle) + " = " + str(self.angle * 180 / math.pi), end="")
            sys.stdout.flush()
        if key[self.left]:
            self.angle -= .01
            self.angle = self.angle % 6.28  # angle < 2pi

            print("\rangle = " + str(self.angle) + " = " + str(self.angle * 180 / math.pi), end="")
            sys.stdout.flush()
        if key[self.up]:
            self.power += .2
            self.power = min(self.power, self.maxpower)

            print("\rpower = " + str(self.power), end="")
            sys.stdout.flush()

        if key[self.down]:
            self.power -= .2
            if self.power < 0:
                self.power = 0

            print("\rpower = " + str(self.power), end="")
            sys.stdout.flush()

        if key[self.launchKey]:


            if ((not self.isLaunched)  and self.ready):
                self.reloadCannonball(self.generateBall())
                # self.isLaunched = True
                self.ready = False
                self.primedBall.power = self.power
                self.primedBall.angle = self.angle+0.985398
                self.primedBall.launch()

                #self.primedBall=None
               # self.launch()

    def timeUntilDeletion(self):
        self.durTimer.decrement()
        if (self.timerEnabled and self.durTimer.isFinished()):
            self.alive = False