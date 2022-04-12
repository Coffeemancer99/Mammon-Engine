import pygame
import src.engine.physics.physics as physics
from src.engine.physics.spritegen import * # allows shorter references
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect


"""
Physics Classes Overview:
All objects have the class Object
If an object is moving, it will have the class Dynamic
If it is static, it will not have the class Dynamic
DO NOT EXTEND FROM DYNAMIC- use DynamicObject or DynamicRect instead
RectObject and DynamicRect are for rectangular objects, allowing certain optimizations. They are not necessary to use.
"""

class Ball(DynamicObject):
    # if you want to extend from someone else's object class, replace DynamicObject with the name of the other class
    def __init__(self, sprite, scale, x, y, name="undefinedBall", mass = 10, launchKey = pygame.K_l):
        DynamicObject.__init__(self, sprite, scale, x, y, name, mass)
        self.launchKey = launchKey
        self.points = 0

    def update(self, airRes=physics.airRes, minMom=physics.minMom, maxMom=None): # retrieves default values from physics module
        try: self.takeInputs(pygame.key.get_pressed())
        except: pass # pygame not initialized, so ignore takeInputs
        DynamicObject.update(self, airRes, minMom, maxMom)

    def takeInputs(self, key):
        if key[pygame.K_p]:
            print(self.name + " points = " + str(self.points))
        if key[pygame.K_o]:
            print("incrementing points")
            self.points += 1
        if key[self.launchKey]:
            self.launch()

    def launch(self):
        print("LAUNCHED")

    def impact(self, obj2, sign): # is called when this Ball *impacts* obj2- haven't finished testing it tho - Daniel
        DynamicObject.impact(self, obj2, sign)
        if isinstance(obj2, Crate):
            self.points += obj2.value
            obj2.explode()


class Crate(RectObject):
    def __init__(self,sprite, scale, x, y, value, name = "undefinedCrate"):
        RectObject.__init__(self, sprite,scale, x, y, name)

        self.value = value

    def explode(self):
        if(self.value):
            print("BOOOM")
            self.value = 0
        # I will soon implement an object removing itself so this can work better- Daniel

