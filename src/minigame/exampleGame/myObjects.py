from src.engine.physics.physics import RectObject
from src.engine.player.playerController import *


"""
Physics Classes Overview:
All objects have the class Object
If an object is moving, it will have the class Dynamic
If it is static, it will not have the class Dynamic
DO NOT EXTEND FROM DYNAMIC- use DynamicObject or DynamicRect instead
RectObject and DynamicRect are for rectangular objects, allowing certain optimizations. They are not necessary to use.
Terrain is an unfinished Object class which supports edges, to be used in calculating normal forces.
"""


class Pirate(Platformer):
    """ Player Documentation:
    xSpeed and ySpeed are how fast the Player object propels itself when directed
    The Platformer subclass jumps if grounded when space() is called, can move left and right.
    The TopDown subclass can move in all 4 directions.
    """
    def __init__(self, sprite, scale, x, y, objects, xSpeed, ySpeed, name="undefinedPirate", mass=10, controls = None):
        Platformer.__init__(self, sprite, scale, x, y, objects, xSpeed, ySpeed, name, mass, controls)
        self.points = 0

    def special(self):
        print(self.name + " points = " + str(self.points))

class Crate(RectObject):
    def __init__(self,sprite, scale, x, y, objects, value, name = "undefinedCrate"):
        RectObject.__init__(self, sprite, scale, x, y, objects, name)
        self.value = value

    def impact(self, obj2): # is called when this object is *impacted* by some obj2- unreliable triggering at low velocity
        if isinstance(obj2, Pirate):
            obj2.points += self.value
        self.explode()

    def explode(self):
        print("BOOOM")
        for object in self.objects:
            if object is self:
                self.objects.remove(self)
                break
