from src.engine.graphics.spritegen import *
import logging

#default values for objects, to be imported into subclass creators
airRes = 0.985
frictS = 0.75
frictD = 0.85
minMom = 0.05

class Object:
    def __init__(self, sprite, scale, x, y, objects, name = "undefined", frict = frictS, animation = None, bounce = 0):
        # print("Initializing object ", name, ": \n\tscale = ", scale, "\n\tx = ", x* scale, "\n\ty = ", y*scale)
        self.sprite = sprite
        self.scale = scale
        self.objects = objects
        self.x = x * scale # (x,y) refers to top-left position of object
        self.y = y * scale
        self.mask = pygame.mask.from_surface(self.sprite)
        self.name = name # development value for debug statements
        self.frict = frict
        self.animation = animation
        self.bounce = bounce

    def draw(self, window, advance = True):
        if (self.animation and advance): # has animation and advance = True
            self.animation.update(self.sprite)
        window.blit(self.sprite,(self.x,self.y))

    def __repr__(self):
        return f'Object "{self.name}", (x,y) = ("{self.x}","{self.y}"), (width, height) = "{self.sprite.get_size()}"'

    def overlap(self, obj2, offsetX = 0, offsetY = 0):
        offsetX = int(offsetX); offsetY = int(offsetY)
        return (self.mask.overlap(obj2.mask, (obj2.x - (self.x + offsetX), obj2.y - (self.y + offsetY))))

    def impact(self, obj2):
        pass

class RectObject(Object):
    def __init__(self, sprite, scale, x, y, objects, name = "undefinedRect", frict = frictS, color = (0,255,255), bounce = 0):
        if isinstance(sprite, Iterable): # can pass sprite object or arguments for generate_rectangle
            sprite = generate_rectangle(*sprite, scale, color = color)
        Object.__init__(self, sprite, scale, x, y, objects, name, frict, bounce = bounce)
        self.mask.fill()
        self.width = sprite.get_width()
        self.height = sprite.get_height()

    def __repr__(self):
        return f'RectObject "{self.name}", (x,y) = ("{self.x}","{self.y}"), (width, height) = "{self.sprite.get_size()}"'

class Dynamic():
    def __init__(self, mass, name):
        self.mass = mass; assert not(mass < 0)
        self.momX = 0
        self.momY = 0
        self.dX = 0
        self.dY = 0
        self.name = name

    def update(self, airRes = airRes, minMom = minMom, maxMom = None):
        assert(isinstance(self, DynamicObject) or isinstance(self, DynamicRect)) # can't have object of type Dynamic
        if not maxMom: maxMom = 10*self.mass
        sign = [0,0]
        sign[0] = 1-2*(self.momX < 0)
        sign[1] = 1-2*(self.momY < 0)
        if(abs(self.momX) > maxMom): self.momX = sign[0]*maxMom
        if(abs(self.momY) > maxMom): self.momY = sign[1]*maxMom

        self.momX = self.momX*airRes
        if abs(self.momX/self.mass) < minMom: self.momX = 0
        self.momY = self.momY*airRes
        if abs(self.momY/self.mass) < minMom: self.momY = 0

        # fractional dXY values will accumulate allowing i.e. moving 1px every other frame
        if self.momX == 0: self.dX = 0
        else: self.dX += self.scale*self.momX/self.mass
        if self.momY == 0: self.dY = 0
        else: self.dY += self.scale*self.momY/self.mass



    def slide(self, obj2):
        logging.debug("'{}' sliding on '{}'! frict = {}".format(self.name,obj2.name, obj2.frict))
        self.momX = self.momX*(1-obj2.frict)
        self.momY = self.momY*(1-obj2.frict)

    def halt(self): # sets movement to 0, returns previous values
        toReturn = [self.dX, self.dY, self.momX, self.momY]
        self.dX = 0; self.dY = 0
        self.momX = 0; self.momY = 0
        return toReturn


class DynamicObject(Dynamic,Object):
    def __init__(self, sprite, scale, x, y, objects, name = "Dynamic", mass = 10, frict = frictD):
        Object.__init__(self, sprite, scale, x, y, objects, name, frict)
        Dynamic.__init__(self,mass, name)



    # def impact(self, obj2, sign):
    #     # logging.debug("IMPACT: %s", repr(self))
    #     # overlap = self.mask.overlap(obj2.mask, (obj2.x-(self.x + int(self.dX) - sign[0]), obj2.y - (self.y + int(self.dY) - sign[1])))
    #     # if not overlap:
    #     #     overlap = (-1,-1)
    #     #     logging.debug("[no overlap?]")
    #     # else:
    #     #     logging.debug("[overlap = {}]".format(overlap))
    #     # logging.debug("'{}' hit '{}' at position ({},{})!".format(self.name, obj2.name, overlap[0] + self.x + int(self.dX) - sign[0], overlap[1] + self.y + int(self.dY)-sign[1]))
    #     pass
    def __repr__(self):
        return f'DynamicObject "{self.name}", (x,y) = ("{self.x}","{self.y}"), (dX,dY) = ("{self.dX}","{self.dY}"), (momX, momY) = ("{self.momX}","{self.momY}"), (width, height) = "{self.sprite.get_size()}"'

class DynamicRect(Dynamic, RectObject):
    def __init__(self, sprite, scale, x, y, objects, name = "DynamicRect", mass = 10, frict = frictD):
        RectObject.__init__(self,sprite, scale, x, y, objects, name, frict)
        Dynamic.__init__(self, mass, name)

    def __repr__(self):
        return f'DynamicRect "{self.name}", (x,y) = ("{self.x}","{self.y}"), (dX,dY) = ("{self.dX}","{self.dY}"), (momX, momY) = ("{self.momX}","{self.momY}"), (width, height) = "{self.sprite.get_size()}"'

def velHandler(mover, objects):
    assert isinstance(mover, Dynamic)
    agents = []
    didImpact = False
    for object in objects:
        if mover is object:
            continue
        if isinstance(mover, RectObject):
            didImpact = velChecker2(mover,object)
        else:
            didImpact = velChecker(mover,object)
        if(didImpact):
            agents.append(object)
            didImpact=False
    # print("moving {}:\n\tx: {} + {}\ty: {} + {}".format(mover.name, mover.x, mover.dX, mover.y, mover.dY))
    mover.x += int(mover.dX)
    mover.y += int(mover.dY)
    mover.dX = mover.dX - int(mover.dX)
    mover.dY = mover.dY - int(mover.dY)
    return agents


def velChecker(obj1, obj2, impactThresh = 2):

    # assert not(obj1.overlap(obj2)) # Assert: are the objects already overlapping?
    impacted = False

    if obj1.overlap(obj2, obj1.dX, obj1.dY):
        stopping = [0,0]
        for index, item in enumerate([[1,0],[-1,0],[0,1],[0,-1]]):
            if obj1.overlap(obj2, item[0], item[1]):
            # if obj1.mask.overlap(obj2.mask, (obj2.x - (obj1.x + int(obj1.dX) + item[0]),obj2.y - (obj1.y + int(obj1.dY)) + item[1])):
                stopping[abs(item[1])] = 1 - 2*(index%2)
                # if item is adjacent to the left, stopping[0] = -1; if item is adjacent to the right, stopping[0] = 1
        if stopping[0]: # if obj1 is horizontally adjacent to obj2
            if(obj1.momX > impactThresh):
                impacted = True
            obj1.dX = 0
            obj1.momX = -1*(obj1.bounce + obj2.bounce)*obj1.momX
        if stopping[1]: # if obj1 is vertically adjacent to obj2
            if(obj1.momY > impactThresh):
                impacted = True
            obj1.dY = 0
            obj1.momY = -1*(obj1.bounce + obj2.bounce)*obj1.momY

        if not obj1.overlap(obj2, obj1.dX, obj1.dY):
            return impacted # The objects were only touching

        dX = int(obj1.dX)
        while obj1.overlap(obj2, offsetX = dX): # using dX, ignore obj1.dY
            if(dX == 0):
                break
            dX -= int(dX/abs(dX))
        # ok dX found
        if (abs(dX - obj1.dX) >= 1) and (abs(obj1.momX) >= impactThresh):
            impacted = True
        obj1.dX = dX

        dY = int(obj1.dY)
        while obj1.overlap(obj2, offsetX = obj1.dX, offsetY = dY):
            if(dY == 0):
                break
            dY -= int(dY/abs(dY))
        # ok dY found
        if (abs(dY - obj1.dY) >= 1) and (abs(obj1.momY) >= impactThresh):
            impacted = True
        obj1.dY = dY
        # print("overlapping finished: dX =", obj1.dX, "dY =", obj1.dY)

        if(impacted):
            obj1.impact(obj2)
            obj2.impact(obj1)
            return True

    return False

def velChecker2(obj1, obj2): # Optimized collision checking for two RectObjects
    if not (isinstance(obj1, RectObject) and isinstance(obj2, RectObject)): return
    bX = 1; bY = 1 # bX and bY stand for how 'bad' of an x or y position obj1 is trying to occupy.

    # FINDING bX
    if((obj1.x + obj1.dX) >= (obj2.x + obj2.width)): bX = 0 # passing to the right, no collision possible
    if(((obj1.x + obj1.dX) + obj1.width) <= obj2.x): bX = 0 # passing to the left, no collision possible
    if bX and obj1.dX >= 0:  # bX != 0 and not moving left
        bX = int((obj1.x + obj1.dX) - (obj2.x - obj1.width))
    elif(bX): # approaching from right
        bX = int((obj2.x + obj2.width) - (obj1.x + obj1.dX))

    # FINDING bY
    if((obj1.y + obj1.dY) >= (obj2.y + obj2.height)):bY = 0 # passing below, no collision possible
    if((((obj1.y + obj1.dY) + obj1.height) <= obj2.y)):bY = 0 # passing above, no collision possible
    if bY and obj1.dY >= 0: # bY != 0 and not moving from below
        bY = int((obj1.y + obj1.dY) - (obj2.y - obj1.height))
    elif(bY): # bY != 0 and moving from below
        bY = int((obj2.y + obj2.height) - (obj1.y + obj1.dY))

    bXflag = bX; bYflag = bY
    if bYflag and (obj1.x == (obj2.x + obj2.width)) and (obj1.dX < 0): obj1.dX = 0; obj1.momX = 0; bX = 0 # obj1 at right side of obj2
    if bYflag and ((obj1.x + obj1.width) == obj2.x) and (obj1.dX > 0): obj1.dX = 0; obj1.momX = 0; bX = 0 # obj1 at left side of obj2

    if bXflag and (obj1.y == (obj2.y + obj2.height)) and (obj1.dY < 0): obj1.dY = 0; obj1.momY = 0; bY = 0 # obj1 directly below obj2
    if bXflag and ((obj1.y + obj1.height) == obj2.y) and (obj1.dY > 0): obj1.dY = 0; obj1.momY = 0; bY = 0 # obj1 directly above obj2

    if (not (bX and bY)) or (not (obj1.dX or obj1.dY)): return True
    # bX/bY value of 0 means collision is impossible, return. If obj1 is no longer moving return.
    if(bX < bY):
        obj1.momX = 0
        if(obj1.dX > 0):
            obj1.dX = obj2.x - (obj1.x + obj1.width)
        else:
            obj1.dX = (obj2.x + obj2.width) - obj1.x
    else:
        obj1.momY = 0
        if(obj1.dY > 0):
            obj1.dY = obj2.y - (obj1.y + obj1.height)
        else:
            obj1.dY = (obj2.y + obj2.height) - obj1.y

    assert not obj1.overlap(obj2, obj1.dX, obj1.dY)
    assert not (abs(obj1.dX) > 50 or abs(obj1.dY) > 50) # glitched movement
    return True



def touching(obj1, obj2):
    return obj1.overlap(obj2, 1, 1) or obj1.overlap(obj2, -1, -1)

def grounded(obj1, onlyStatics = False):
    for obj2 in obj1.objects:
        if obj1 is obj2:
            continue
        if onlyStatics and isinstance(obj2, Dynamic):
            continue
        if obj1.overlap(obj2, offsetY = 1):
            return obj1.overlap(obj2, offsetY = 1)

def main():
    print("physics maine\n")
    objects = []; scale = 1
    coco = DynamicObject(generate_rectangle(20,20,1), scale, 0, 0, objects, "coco", 5)
    coco.momY = 22
    box = Object(generate_rectangle(20,20,1), scale, 0, 22, objects, "box")
    coco.update()
    objects.append(coco); objects.append(box)
    print("\n\n###############################################################################################################")
    print("###############################################################################################################")
    print("###############################################################################################################\n")
    if(coco.overlap(box)): print("FAILED")
    else: print("PASSED\n")

    for object in objects: print(object)
    print("")
    velHandler(coco,objects)



    print("")
    for object in objects: print(object)
    print("")
    print("###############################################################################################################\n")
    if(coco.overlap(box)): print("FAILED")
    else: print("PASSED")


if(__name__ == "__main__"):
    main()