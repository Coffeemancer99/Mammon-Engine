import src.engine.physics.physics as physics
from src.engine.graphics.spritegen import * # allows shorter references
from src.engine.physics.physics import DynamicObject

"""
xSpeed and ySpeed are how fast the Player object propels itself when directed
The Platformer subclass jumps if grounded when space() is called, can move left and right.
The TopDown subclass can move in all 4 directions.
"""
class Player(DynamicObject):
    def __init__(self, sprite, scale, x, y, objects, xSpeed, ySpeed, name="undefinedPlayer", mass = 10, controls = None):
        DynamicObject.__init__(self, sprite, scale, x, y, objects, name, mass)
        self.controls = controls
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed


    def update(self, airRes=physics.airRes, minMom=physics.minMom, maxMom=None): # retrieves default values from physics module
        if self.controls: self.takeInputs()
        DynamicObject.update(self, airRes, minMom, maxMom)

    def takeInputs(self):
        try: key = pygame.key.get_pressed()
        except: return # pygame not initialized, so do nothing
        if key[self.controls['up']]:
            self.up()
        if key[self.controls['down']]:
            self.down()
        if key[self.controls['left']]:
            self.left()
        if key[self.controls['right']]:
            self.right()
        if key[self.controls['space']]:
            self.space()
        if key[self.controls['action']]:
            self.action()
        if key[self.controls['special']]:
            self.special()

    def up(self):
        pass
    def down(self):
        pass
    def left(self):
        pass
    def right(self):
        pass
    def space(self):
        pass
    def action(self):
        pass
    def special(self):
        pass

class Platformer(Player):
    # def __init__(self, sprite, scale, x, y, objects, xSpeed, ySpeed, name = "undefinedPlatformer", mass = 10, controls = None):
    #     Player.__init__(self, sprite, scale, x, y, objects, xSpeed, ySpeed, name, mass, controls)

    def left(self):
        if isinstance(self.xSpeed, Iterable): # separate speed values for left and right
            self.momX -= self.xSpeed[0]
        else: self.momX -= self.xSpeed
    def right(self):
        if isinstance(self.xSpeed, Iterable): # separate speed values for left and right
            self.momX += self.xSpeed[1]
        else: self.momX += self.xSpeed
    def space(self):
        if physics.grounded(self, self.objects):
            self.momY -= self.ySpeed

class TopDown(Player):
    # def __init__(self, sprite, scale, x, y, objects, xSpeed, ySpeed, name = "undefinedTopDown", mass = 10):
    #     Player.__init__(self, sprite, scale, x, y, objects, xSpeed, ySpeed, name, mass)

    def left(self):
        if isinstance(self.xSpeed, Iterable): # separate speed values for left and right
            self.momX -= self.xSpeed[0]
        else: self.momX -= self.xSpeed
    def right(self):
        if isinstance(self.xSpeed, Iterable): # separate speed values for left and right
            self.momX += self.xSpeed[1]
        else: self.momX += self.xSpeed
    def up(self):
        if isinstance(self.ySpeed, Iterable): # separate speed values for up and down
            self.momY -= self.ySpeed[0]
        else: self.momY -= self.ySpeed

    def down(self):
        if isinstance(self.ySpeed, Iterable): # separate speed values for up and down
            self.momY += self.ySpeed[1]
        else: self.momY += self.ySpeed