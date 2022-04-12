import src.minigame.physicsTest.ball as ball
import pygame
import math
import sys
import src.engine.physics.physics as physics
from src.minigame.timer.timer import timer as timer

scaleFancy = 0.05
defMaxPow = 80
_maxHealth = 5
class playerController(ball.Ball):
    def __init__(self, sprite, scale, x, y,  up, down, left, right, launch, primedBall, lifetime, timerEnabled, name="undefinedBall", mass = 10, maxpower = defMaxPow):
        ball.Ball.__init__(self, sprite, scale, x, y, name="undefinedBall", mass=10, maxpower=defMaxPow)
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.launchKey = launch
        self.isLaunched = False
        self.health = _maxHealth
        self.alive = True
        self.lifetime = lifetime
        self.durTimer = timer(3, 60)
        self.timerEnabled = timerEnabled

    def takeInputs(self, objects):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.momY -= 3
            if key[pygame.K_LSHIFT]:
                self.momY -= 3
        if key[pygame.K_DOWN]:
            self.momY += 3
            if key[pygame.K_LSHIFT]:
                self.momY += 7
        if key[pygame.K_LEFT]:
            self.momX -= 2
            if key[pygame.K_LSHIFT]:
                self.momX -= 4
        if key[pygame.K_RIGHT]:
            self.momX += 2
            if key[pygame.K_LSHIFT]:
                self.momX += 4

    def loseHealth(self):
        if(self.health>0):
            self.health -= 1

    def gainHealth(self):
        if(self.health<_maxHealth):
            self.gainHealth += 1

    def isDead(self):
        return(self.health<=0)

    def timeUntilDeletion(self):
        self.durTimer.decrement()
        if(self.timerEnabled and self.durTimer.isFinished()):

            self.alive = False