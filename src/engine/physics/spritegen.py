import pygame
from collections.abc import Iterable
import math
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

def skew_line(line, m): # WORK IN PROGRESS m = end length
    print("line going to width {} from:\n{}".format(m,line))
    n = 0 # n = start length, not counting empty pixels
    for pixel in line:
        if pixel: n += 1
    r = m/n # each pixel in line gets stretched to r pixels, on average
    empty = len(line) - m # amount of empty space left after skewing
    assert r > 1
    toReturn = [0]*(int(empty/2)); empty -= int(empty/2)
    print("toReturn = ", toReturn)
    print("m = {}, n = {}, r = {}, empty: {}, {}".format(m,n,r, empty, int(empty/2)))
    score = 0
    numAdded = 0
    for pixel in line:
        if not pixel: continue
        score += r
        while score >= 1:
            score -= 1
            toReturn.append(pixel)
            numAdded += 1
    if(score > 0):
        score = 0
        toReturn.append(toReturn[-1])
    if(empty):
        for i in range(empty):
            toReturn.append(0)
    print("m = {}, n = {}, r = {}, score: {}".format(m,n,r, score))
    print("toReturn = ", toReturn)

    return toReturn

def skew_image(image, scale): # WORK IN PROGRESS
    # TODO: rotate image before and after
    height = image.get_height()
    width = image.get_width()
    array = pygame.PixelArray(image)
    for i in len(array):
        row = [col[i] for col in array]

    row = [col[0] for col in array]
    numPixels = 0
    for pixel in row:
        if not pixel: continue
        numPixels += 1


    array.close
    return toReturn


def grab_sprite(address, scale):
    sprite = pygame.image.load(address)
    sprite = pygame.transform.scale(sprite, (int((sprite.get_width()) *scale), int((sprite.get_height()) *scale)))    # scales the sprites
    return sprite

def generate_polygon(points, scale, color = (0,255,0,255), size = None):
    points = [(scale*point[0], scale*point[1]) for point in points]
    if size:
        size = [scale*x for x in size]
    else: # size = size of box encapsulating points

        xValues = [scale*point[0] for point in points]
        yValues = [scale*point[1] for point in points]
        size = [max(xValues) - min(xValues), max(yValues) - min(yValues)]
    print("\tsize = ", size)
    sprite = pygame.Surface(size, flags=pygame.SRCALPHA)
    pygame.draw.polygon(sprite, color, points)
    # sprite = pygame.transform.scale(sprite, (int((sprite.get_width()) *scale), int((sprite.get_height()) *scale)))
    return sprite

def generate_circle(radius, scale, color = (255,0,0,255)):
    return generate_ellipse(2*radius,2*radius, scale, color)

def generate_ellipse(width, height, scale, color = (255,255,0,255)):
    # scale = math.sqrt(scale)
    sprite = pygame.Surface((scale*width, scale*height), flags = pygame.SRCALPHA)
    pygame.draw.ellipse(sprite,color,pygame.Rect((0,0),(scale*width,scale*height)))
    return sprite

def generate_rectangle(width, height, scale, color = (0,255,255)):
    return generate_polygon([[0,0],[width,0], [width,height], [0,height]], scale, color, size = (width,height))
