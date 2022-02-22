import pygame
import math
import sys # for flushing stdout
class Ball():
    def __init__(self, x, y, scale, sprite, bId):
        self.ballID = bId
        self.scale = scale
        self.sprite = sprite
        self.sprite = pygame.transform.scale(self.sprite, ((self.sprite.get_width()) * scale/2, (self.sprite.get_height()) * scale/2))
        self.rectCol = self.sprite.get_rect()
        self.rectCol.x = x
        self.rectCol.y = y

        self.momX = 0
        self.momY = 0
        self.mass = 1

        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()\

        self.angle = 0
        self.power = 0

        self.dx = 0
        self.dy = 0

    def update(self):
        self.dX = 0
        self.dY = 0

        airRes = 0.9

        key = pygame.key.get_pressed()
        if key[pygame.K_u]:
            self.angle += .01
            self.angle = self.angle%6.28
            print("\rangle = " + str(self.angle), end = "")
            sys.stdout.flush()
        if key[pygame.K_j]:
            self.angle += 1
            self.angle = self.angle%6.28 # angle < 2pi
            print("\rangle = " + str(self.angle), end = "")
            sys.stdout.flush()
        if key[pygame.K_i]:
            self.power += .2
            if self.power > 10:
                self.power = 10
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

        self.momY = self.momY*airRes
        if abs(self.momY) < 0.05:
            self.momY = 0
        self.momX = self.momX*airRes
        if abs(self.momX) < 0.05:
            self.momX = 0

        self.dX = self.momX/self.mass
        self.dY = self.momY/self.mass



    def launch(self):
        if(self.power == 0):
            return
        print("\r\rlaunched!            \n")
        print("power = " + str(self.power))
        print("angle = " + str(self.angle))
        print("powX = " + str(self.power*math.cos(self.angle)))
        print("powY = " + str(self.power*math.sin(self.angle)))
        print("")


        self.momX -= self.power*math.cos(self.angle)
        self.momY -= self.power*math.sin(self.angle)
        self.power = 0
        self.angle = 0

#ONLY UPDATE RECTANGLE IN ONE PLACE!!! O_O SHARED MUTABLE STATE OH MY~
    def updateRect(self):
        self.rectCol.x += self.dX
        self.rectCol.y += self.dY

    def __repr__(self):
        return(str(self.fruitId))