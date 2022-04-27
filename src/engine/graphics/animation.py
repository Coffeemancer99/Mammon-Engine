from src.engine.graphics.spritegen import *

class Animation:
    def __init__(self, frames, framerate = 45):
        self.tick = 0
        self.currentFrame = 0
        self.frames = frames
        self.framerate =  framerate # number of in-game frames to wait before advancing a frame
    def update(self, mySprite):
        self.tick += 1
        if self.tick == self.framerate: # next frame
            self.tick = 0
            self.currentFrame = (self.currentFrame + 1)%(len(self.frames))
            mySprite.blit(self.frames[self.currentFrame], (0,0))
def animate_movement(canvas, object, p1, p2, frames):
    (x1, y1) = p1; (x2, y2) = p2
    dX = int((x2 - x1)/frames); dY = int((y2 - y1)/frames) # distance traveled in a frame
    if isinstance(canvas, Iterable):  # can pass sprite object or arguments for generate_rectangle
        canvas = generate_rectangle(*canvas)
    toReturn = []
    print("Animating from p1 {} to p2 {}".format(p1, p2))
    for i in range(frames+1):
        print("object pos = {}".format((x1 + dX*i, y1 + dY*i)))
        toReturn.append(pygame.Surface((canvas.get_width(), canvas.get_height())))
        toReturn[i].blit(canvas, (0,0))
        toReturn[i].blit(object,(x1 + dX*i, y1 + dY*i))
    return Animation(toReturn)