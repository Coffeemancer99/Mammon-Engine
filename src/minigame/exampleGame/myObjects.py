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
Terrain is an unfinished Object class which supports edges, to be used in calculating normal forces.
"""



class Ball(DynamicObject):
    # if you want to extend from someone else's object class, replace DynamicObject with the name of the other class
    def __init__(self, sprite, scale, x, y, objects, name="undefinedBall", mass = 10):
        DynamicObject.__init__(self, sprite, scale, x, y, objects, name, mass)
        self.points = 0
        self.controls = {
            'up': pygame.K_w,
            'down': pygame.K_s,
            'left': pygame.K_a,
            'right': pygame.K_d,
            'space': pygame.K_SPACE,
            'action': pygame.K_u
        }

    def update(self, airRes=physics.airRes, minMom=physics.minMom, maxMom=None): # retrieves default values from physics module
        try: self.takeInputs(pygame.key.get_pressed())
        except: pass # pygame not initialized, so ignore takeInputs
        DynamicObject.update(self, airRes, minMom, maxMom)

    def takeInputs(self, key):
        if key[self.controls['up']]:
            self.momY -= 3
        if key[self.controls['down']]:
            self.momY += 3
        if key[self.controls['left']]:
            self.momX -= 3
        if key[self.controls['right']]:
            self.momX += 3
        if key[self.controls['space']]:
            if physics.grounded(self, self.objects):
                self.momY -= 10
                print("JUMP")
        if key[pygame.K_p]:
            print(self.name + " points = " + str(self.points))
        if key[pygame.K_o]:
            print("incrementing points")
            self.points += 1

    def launch(self):
        print("LAUNCHED")

    def impact(self, obj2, sign): # is called when this Ball *impacts* obj2- unreliable triggering at low velocity- Daniel
        DynamicObject.impact(self, obj2, sign)
        if isinstance(obj2, Crate):
            self.points += obj2.value
            obj2.explode()


class Crate(RectObject):
    def __init__(self,sprite, scale, x, y, objects, value, name = "undefinedCrate"):
        RectObject.__init__(self, sprite, scale, x, y, objects, name)

        self.value = value

    def explode(self):
        print("BOOOM")
        self.value = 0
        i = 0
        for object in self.objects:
            if object is self:
                self.objects.pop(i)
                break
            i += 1


