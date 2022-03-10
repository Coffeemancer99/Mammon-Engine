"""
    About this file:
    this is a scratch file that WILL BE REFACTORED LATER into multiple files for physics
"""
# The box needs a Vector of doubles x and y and another class that implements Vector and has a mass and friction
# Treat force and acceleration as a 2d vector and treat them as x and y. Gravity = y vector direction = x vector

import pygame
from math import pi
from collections.abc import Iterable
from src.engine.physics.spritegen import *

import math
import sympy
import functools

#default values for objects, to be imported into subclass creators
airRes = 0.985
frictS = 0.7
frictD = 0.85
minMom = 0.005

class Object:
    def __init__(self, sprite, scale, x, y, name = "undefined", frict = frictS):

        self.sprite = pygame.transform.scale(sprite, ((sprite.get_width()) * scale, (sprite.get_height()) * scale)) #inherited code
        self.scale = scale
        self.x = x * scale # (x,y) refers to top-left position of object
        self.y = y * scale
        self.mask = pygame.mask.from_surface(self.sprite)
        self.name = name # development value for debug statements
        self.frict = frict

    def draw(self, window):
        window.blit(self.sprite,(self.x,self.y))

    def __repr__(self):
        return f'Object "{self.name}", (x,y) = ("{self.x}","{self.y}"), (width, height) = "{self.sprite.get_size()}"'

class RectObject(Object):
    def __init__(self, sprite, scale, x, y, name = "undefinedRect", frict = frictS):
        if isinstance(sprite, Iterable): # can pass sprite object or arguments for generate_rectangle
            print("iterable\n\n")
            sprite = generate_rectangle(*sprite)
        Object.__init__(self, sprite, scale, x, y, name, frict)
        self.mask.fill()

    def __repr__(self):
        return f'RectObject "{self.name}", (x,y) = ("{self.x}","{self.y}"), (width, height) = "{self.sprite.get_size()}"'

class DynamicObject(Object):
    def __init__(self, sprite, scale, x, y, name = "undefinedDynamic", mass = 10, frict = frictD):
        Object.__init__(self, sprite, scale, x, y, name, frict)
        self.mass = mass; assert not(mass < 0)
        self.momX = 0
        self.momY = 0
        self.dX = 0
        self.dY = 0

    def update(self, airRes = airRes, minMom = minMom, maxMom = None):
        if not maxMom: maxMom = 10*self.mass
        sign = [0,0]
        sign[0] = 1-2*(self.momX < 0); sign[1] = 1-2*(self.momY < 0)
        if(abs(self.momX) > maxMom): self.momX = sign[0]*maxMom
        if(abs(self.momY) > maxMom): self.momY = sign[1]*maxMom

        self.momX = self.momX*airRes
        if abs(self.momX/self.mass) < minMom: self.momX = 0
        self.momY = self.momY*airRes
        if abs(self.momY/self.mass) < minMom: self.momY = 0

        # fractional dXY values will accumulate allowing e.g. moving 1px every other frame
        if self.momX == 0: self.dX = 0
        else: self.dX += self.scale*self.momX/self.mass
        if self.momY == 0: self.dY = 0
        else: self.dY += self.scale*self.momY/self.mass

    def slide(self, obj2):
        print("'{}' sliding on '{}'! frict = {}".format(self.name,obj2.name, obj2.frict))
        self.momX = self.momX*(1-obj2.frict)
        self.momY = self.momY*(1-obj2.frict)

    def impact(self, obj2, sign):
        print("\nIMPACT:")
        print(self)
        overlap = self.mask.overlap(obj2.mask, (obj2.x-(self.x + int(self.dX) - sign[0]), obj2.y - (self.y + int(self.dY) - sign[1])))
        if not overlap:
            overlap = (-1,-1)
            print("[no overlap?]", end =  " ")
        else:
            print("[overlap = {}]".format(overlap), end = " ")
        print("'{}' hit '{}' at position ({},{})!".format(self.name, obj2.name, overlap[0] + self.x + int(self.dX) - sign[0], overlap[1] + self.y + int(self.dY)-sign[1]))
    def __repr__(self):
        return f'DynamicObject "{self.name}", (x,y) = ("{self.x}","{self.y}"), (dX,dY) = ("{self.dX}","{self.dY}"), (momX, momY) = ("{self.momX}","{self.momY}"), (width, height) = "{self.sprite.get_size()}"'

def velHandler(mover, objects):
    assert isinstance(mover, DynamicObject)
    for object in objects:
        if mover is object:
            continue
        velChecker(mover,object)
    mover.x += int(mover.dX)
    mover.y += int(mover.dY)
    mover.dX = mover.dX - int(mover.dX)
    mover.dY = mover.dY - int(mover.dY)

def velChecker(obj1, obj2):

    assert not(obj1.mask.overlap(obj2.mask,(obj2.x - obj1.x, obj2.y - obj1.y) )) # Assert: are the objects already overlapping?
    # if obj1.mask.overlap(obj2.mask,(obj2.x - obj1.x, obj2.y - obj1.y) ):
    #     print("ERROR: already overlapping. Attempting escape...")
    #     for direction in [[0,1],[1,0],[0,-1],[-1,0],  [1,1],[-1,1],[1,-1],[-1,1]]:
    #         if not obj1.mask.overlap(obj2.mask,(obj2.x - (obj1.x + direction[0]), obj2.y - (obj1.y + direction[1]))):
    #             print("escape successful! calling velChecker again...")
    #             obj1.x += direction[0]
    #             obj1.y += direction[1]
    #             velChecker(obj1, obj2)
    #             return
    #     print("")

    overlap = obj1.mask.overlap(
        obj2.mask, (obj2.x - (obj1.x + int(obj1.dX)), obj2.y - (obj1.y + int(obj1.dY)))
    )
    if overlap:
        # print("            overlapping- initial (dX, dY) = (" + str(obj1.dX) + " / " + str(int(obj1.dX)) + ", " + str(obj1.dY) + " / " + str(int(obj1.dY)) + ")")
        sign = [0,0] # indicates the sign of dX and dY
        if obj1.dX < 0: sign[0] = 1
        else: sign[0] = -1
        if obj1.dY < 0: sign[1] = 1
        else: sign[1] = -1

        impacted = False


        for weight in [[1,0],[0,1]]: # first dX is handled, then dY
            if weight[0]:
                weight[0] = int(obj1.dX)
                dXbackup = obj1.dX
                obj1.dX = 0
            if weight[1]:
                weight[1] = int(obj1.dY)
                dYbackup = obj1.dY
                obj1.dY = 0

            if(weight == [0,0]):continue
            for i in range(abs(max(weight, key=abs))): # max(weight) will return obj1.dX or obj1.dY
                overlap = obj1.mask.overlap(
                    obj2.mask, (obj2.x - (obj1.x + weight[0] + int(obj1.dX)), obj2.y - (obj1.y + weight[1])) # here, int(dX) never leads to a collision between the two objects
                )
                if not overlap: # an acceptable new position for obj1 was found
                    # print("overlap ended!")
                    if weight[0]:
                        if(weight[0] != int(dXbackup)):
                            impacted = True
                            obj1.dX = weight[0]
                            # obj1.impact(obj2,(obj2.x - (obj1.x + int(obj1.dX) - sign[0]), obj2.y - (obj1.y + weight[1])))

                        else: # sliding along the dX direction, apply friction
                            obj1.dX = dXbackup
                            obj1.slide(obj2)
                    if weight[1]:
                        if(weight[1] != int(dYbackup)):
                            impacted = True
                            obj1.dY = weight[1]
                            # obj1.impact( obj2, obj1.mask.overlap(obj2.mask,(obj2.x - (obj1.x + weight[0] + int(obj1.dX)), obj2.y - (obj1.y + weight[1] - sign[1]))) )
                        else:  # sliding along the dY direction, apply friction
                            obj1.dY = dYbackup
                            obj1.slide(obj2)
                    break
                else:
                    if abs(weight[0]) == 1: # adjacent horizontally
                        # print("dX: found to be adjacent, dX->0. (dX,dY) = (" + str(weight[0]) + ", " + str(weight[1]) + ")")

                        obj1.dX = 0
                        obj1.momX = 0
                    if abs(weight[1]) == 1: # adjacent vertically
                        # # print("dY: found to be adjacent, dY->0. (dX,dY) = (" + str(weight[0]) + ", " + str(weight[1]) + ")")
                        # if (obj1.momY/obj1.mass) > minMom:
                        #     obj1.dY = -sign[1]
                        #     obj1.impact(obj2, (-42,-42))
                        obj1.dY = 0
                        obj1.momY = 0
                if weight[0]: weight[0] += sign[0]
                if weight[1]: weight[1] += sign[1]

        if impacted:
            obj1.impact(obj2, sign)

def touching(obj1, obj2):
    return ((obj1.mask.overlap(obj2.mask, (obj2.x - obj1.x + 1, obj2.y - obj1.y + 1))) or (obj1.mask.overlap(obj2.mask,(obj2.x - obj1.x - 1, obj2.y - obj1.y - 1) )))

def grounded(obj1, objects, onlyStatics = False):
    for obj2 in objects:
        if obj1 is obj2:
            continue
        if onlyStatics and isinstance(obj2, DynamicObject):
            continue
        if (obj1.mask.overlap(obj2.mask, (obj2.x - obj1.x, obj2.y - (obj1.y + 1))) ):
            (x,y) = obj1.mask.overlap(obj2.mask, (obj2.x - obj1.x, obj2.y - (obj1.y + 1)))
            obj2.sprite.set_at((x + obj1.x - obj2.x, y + (obj1.y + 1) - obj2.y), 100)
            return True



# Gravity created by Andrew Bunn, extracted from
# playerController.py by Joel Tanig
def applyGravityPlayer(velY, fallSpeed, terminalV):
    velY += fallSpeed # Falling here
    if velY > terminalV: # Terminal Velocity
        velY = terminalV
    return velY



def movementLeftRight(dx, speed):
    dx += speed
    return float(dx)


def collision():
    pass


""" (Force formula)

    Uses mass and multiplies it by acceleration
    This function needs to be looped so it can be updated

    :param mass: - the mass that needs to be computed
    :param acceleration: - that acceleration that needs to be computed

    :return: - float type: the force 

"""


def force(mass, acceleration, obj1, obj2):
    return float(mass * acceleration)


""" (Normal Force formula)

    Uses the earth's gravity and multiples it by the mass provided 
    This function needs to be looped so it can update 
    
    :param mass: - the mass that needs to be computed for force
    
    :return: - float type: normal force with mass 
    
"""


def computeMovementForce(mass):
    return float(mass * -9.81)


""" (Friction formula)

    f = mu*N
    mu = coefficient of friction
    N = Normal force
    
    Note: Must call the force function before you can use friction, and must pass in a known friction coefficient
    
    Uses the mass provided to calculate normal force then multiples it by the coefficientOfFriction provided
    
    :param mass: - the mass that needs to be provided :param coefficientOfFriction: - coefficientOfFriction that can 
    be calculated or remained as a constant that will determined later 

    :return: - float type: friction
    
"""


def friction(mass, coefficientOfFriction):
    return float(coefficientOfFriction * computeMovementForce(mass))
