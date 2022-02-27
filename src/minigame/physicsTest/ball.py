import pygame
import math
import sys # for flushing stdout for dev statements, remove later
import src.engine.physics.physics as physics
from src.engine.physics.physics import Object
from src.engine.physics.physics import DynamicObject


class Ball(DynamicObject):
    def __init__(self, sprite, scale, x, y, name="undefinedBall"):
        DynamicObject.__init__(self, sprite, scale, x, y, name)
        self.power = 0
        self.angle = 0

    def update(self):
        self.takeInputs(pygame.key.get_pressed())
        DynamicObject.update(self)

    def takeInputs(self, key):
        if key[pygame.K_u]:
            self.angle += .01
            self.angle = self.angle%6.28
            print("\rangle = " + str(self.angle) + " = " + str(self.angle*180/math.pi), end = "")
            sys.stdout.flush()
        if key[pygame.K_j]:
            self.angle += .5
            self.angle = self.angle%6.28 # angle < 2pi
            print("\rangle = " + str(self.angle) + " = " + str(self.angle*180/math.pi), end = "")
            sys.stdout.flush()
        if key[pygame.K_i]:
            self.power += .2
            if self.power > 40:
                self.power = 40
            print("\rpower = " + str(self.power), end = "")
            sys.stdout.flush()

        if key[pygame.K_k]:
            self.power -= .2
            if self.power < 0:
                self.power = 0
            print("\rpower = " + str(self.power), end = "")
            sys.stdout.flush()

        if key[pygame.K_o]:
            self.launch()

    def launch(self):
        if(self.power == 0):
            return
        print("\r\rlaunched!            \n")
        print("power = " + str(self.power))
        print("angle = " + str(self.angle) + " = " + str(self.angle * 180 / math.pi))
        print("powX = " + str(self.power*math.cos(self.angle)))
        print("powY = " + str(self.power*math.sin(self.angle)))
        print("")


        self.momX += self.power*math.cos(self.angle)
        self.momY -= self.power*math.sin(self.angle)
        self.power = 0
        self.angle = 0
