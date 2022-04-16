import pygame

from src.engine.physics import physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect


class SwimmerPlayer(DynamicObject):
    def __init__(self, x, y, scale, upKey, leftKey, rightKey, downKey, sprite, pId, objects, name="Unused", mass=10):
        DynamicObject.__init__(self, sprite, scale, x, y, objects, name, mass)
        self.scale = scale
        self.sprite = sprite
        self.sprite = pygame.transform.scale(self.sprite,
                                             ((self.sprite.get_width()) * scale, (self.sprite.get_height()) * scale))

        self.pId = pId
        self.upKey = upKey
        self.leftKey = leftKey
        self.rightKey = rightKey
        self.downKey = downKey

        self.facingRight = True
        self.facingLeft = False
        self.facingUp = False
        self.rotatedUp = False

    # TODO figure out why i cant go up left up left on the rotations (same with right)
    #   adding checks breaks rotations (wanted to match ifs and elses flag setting)
    #   maybe print flags every time around?
    #   Fixed mostly... right up left sequence results in upsidedown player,
    #   keep messing with flags (maybe add third to all checks)

    def takeInputs(self, objects):
        key = pygame.key.get_pressed()
        if key[self.leftKey]:
            if not self.facingLeft:
                if self.facingUp:
                    self.sprite = pygame.transform.rotate(self.sprite, -270)
                    self.sprite = pygame.transform.flip(self.sprite, True, False)
                    self.facingUp = False
                    self.facingLeft = False

                else:
                    self.sprite = pygame.transform.flip(self.sprite, True, False)
                    self.facingRight = False
                    self.facingLeft = True
                    self.facingUp = False

        if key[self.rightKey]:
            if not self.facingRight:
                if self.facingUp:
                    self.sprite = pygame.transform.rotate(self.sprite, 270)
                    self.sprite = pygame.transform.flip(self.sprite, True, False)
                    self.facingUp = False
                    self.facingRight = False
                else:
                    self.sprite = pygame.transform.flip(self.sprite, True, False)
                    self.facingRight = True
                    self.facingLeft = False
                    self.facingUp = False

        if key[self.upKey]:
            # would like to rotate upward, but messes with hitboxes
            # maybe use a square or round player? Would work fine
            if not self.facingUp:
                if self.facingLeft and (not self.facingUp):
                    self.sprite = pygame.transform.rotate(self.sprite, 270)
                    self.facingUp = True
                    self.facingLeft = False
                if self.facingRight and (not self.facingUp):
                    self.sprite = pygame.transform.rotate(self.sprite, -270)
                    self.facingUp = True
                    self.facingRight = False

                self.facingUp = True

        if key[self.downKey]:
            pass

    def fightCurrent(self, buttons):
        pushDown = True
        for button in buttons:
            if self.upKey == button.key:
                print("hit up")
                self.momY -= 7
                pushDown = False
            if self.leftKey == button.key:
                print("Hit Left")
                self.momX -= 7
            if self.rightKey == button.key:
                print("Hit Right")
                self.momX += 7

        if pushDown:
            # self.momY += 0.35
            self.momY += 0.0

    def update(self, airRes=physics.airRes, minMom=physics.minMom,
               maxMom=None):  # retrieves default values from physics module
        try:
            self.takeInputs(pygame.key.get_pressed())
        except:
            pass  # pygame not initialized, so ignore takeInputs
        DynamicObject.update(self, airRes, minMom, maxMom)
