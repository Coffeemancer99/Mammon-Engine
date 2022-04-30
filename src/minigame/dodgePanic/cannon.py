import pygame
import math
import sys # for flushing stdout for dev statements, remove later
import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
from src.engine.player.playerController import *

defMaxPow = 110 # default max power
class Cannon(TopDown):
    def __init__(self, sprite, scale, x, y, objects, xSpeed, ySpeed, minAngle = 0, maxAngle = 2*math.pi, name="Cannon", mass = 10, controls = None):
        TopDown.__init__(self, sprite, scale, x, y, objects, xSpeed, ySpeed, name, mass, controls)
        assert isinstance(self, CannonX) or isinstance(self, CannonY)
        self.angle = minAngle
        self.power = 0
        self.minAngle = minAngle
        self.maxAngle = maxAngle
        assert (maxAngle <= 2*math.pi) and (minAngle <= 2*math.pi) and (minAngle >= 0) and (maxAngle >= 0) # valid values
        assert (maxAngle > minAngle)
        self.radius = 60*self.scale

    def angleUp(self, amount):
        self.angle += amount
        if self.angle > self.maxAngle:
            self.angle = self.maxAngle
        if self.angle > 2*math.pi:
            self.angle -= 2*math.pi

    def angleDown(self, amount):
        self.angle -= amount
        if self.angle < self.minAngle:
            self.angle = self.minAngle
        if self.angle < 0:
            self.angle += 2*math.pi

    def powerUp(self, amount):
        self.power += amount
        if self.power > defMaxPow:
            self.power = defMaxPow

    def powerDown(self, amount):
        self.power -= amount
        if self.power < 0:
            self.power = 0

    def action(self):
        self.powerUp(10)
    def special(self):
        self.launch()
        self.cooldown['special'] = 10

    def launch(self):
        # create object at x + radius*cos(), y + radius(sin)

        xPos = int(self.x + .5*self.sprite.get_width() + self.radius*math.cos(self.angle))
        yPos = int(self.y + .5*self.sprite.get_height() - self.radius*math.sin(self.angle))
        ball = DynamicObject(generate_circle(10,self.scale),self.scale, xPos, yPos, self.objects, name = "CannonBall")
        ball.momX = self.power*math.cos(self.angle)
        ball.momY = -1*self.power*math.sin(self.angle)
        for object in self.objects:
            if ball.overlap(object):
                print(self.name, "cannot create ball:\n\t",ball)
                return
        print(self.name, "creating CannonBall\n\t",ball)
        self.objects.append(ball)

    def __repr__(self):
        return f'Cannon "{self.name}"\n\t(x,y) = ("{self.x}","{self.y}"), (dX,dY) = ("{self.dX}","{self.dY}"),(momX, momY) = ("{self.momX}","{self.momY}"), (width, height) = "{self.sprite.get_size()}"\n\tpower, angle = ("{self.power}", "{self.angle}"), radius = "{self.radius}"'


class CannonX(Cannon):
    def up(self):
        self.angleUp(self.ySpeed)
    def down(self):
        self.angleDown(self.ySpeed)

class CannonY(Cannon):
    def left(self):
        self.angleUp(self.xSpeed)
    def right(self):
        self.angleDown(self.xSpeed)
