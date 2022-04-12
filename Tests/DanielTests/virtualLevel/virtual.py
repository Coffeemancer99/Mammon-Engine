import src.engine.physics.physics as physics
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
from src.engine.physics.spritegen import *
import src.engine.physics.terrain as terrain
import src.minigame.physicsTest.ball as ball
import unittest
import pygame
from io import StringIO
import sys
import logging

isInitialized = False

def initialize(windowArg = None, scaleArg = 1, framerateArg = 60):
    global mainWindow; global scale; global framerate; global isInitialized
    if windowArg: mainWindow = windowArg
    else: mainWindow = pygame.Surface((4000,4000))
    scale = scaleArg
    framerate = framerateArg
    isInitialized = True

def functTest():
    print("funky testing~")
    logging.info("info")
    return

def logState():
    global temp_out; global loggerChild; global backupHandler

    string = temp_out.getvalue()
    if(string.count("IMPACT")) == 1:
        loggerChild.debug("Pass")
    else:
        loggerChild.debug("Fail")


def pseudoAssert(condition, statement, backup):
    if not condition:
        sys.stdout = backup
        print(statement)
        return True
    return False

def testImpact(window = None, scale = 1, framerate = 60, gravity = 1.5, ballPos = (25,20), ballPow = 80):
    if not isInitialized: initialize(window, scale, framerate)
    global backupHandler; global temp_out; global logger; global loggerChild
    logger = logging.getLogger()
    backupHandler = logger.handlers[0]
    logger.removeHandler(backupHandler)
    loggerChild = logger.getChild('xyz')
    if not loggerChild.hasHandlers(): loggerChild.addHandler(backupHandler)
    temp_out = StringIO()
    logger.addHandler(logging.StreamHandler(temp_out))

    triY = 30; triX = 55
    triangle = terrain.from_polygon([[20, 345], [20 + triX, 311], [20, 311 - triY]], scale, color=(0, 255, 0, 255),name="triangle")
    (ballX, ballY) = ballPos
    myBall = ball.Ball(generate_circle(20,scale), scale, ballX, ballY, name="myBall", mass=4, maxpower=ballPow)
    objects = []
    objects.append(myBall)
    objects.append(triangle)
    objects.append(physics.RectObject((500, 100), scale, 20, 300, name="net"))
    objects.append(physics.RectObject((100, 300), scale, 300, 20, name="backboard"))

    # Level looks like this:
    # myBall    ||
    #   0       || backboard
    # #\        ||
    # ##\
    # Triangle
    #   _____________
    #        net
    for i in range(60):
        for object in objects:
            if isinstance(object, physics.Dynamic):
                if object is myBall:
                    myBall.momY += 1.5
                object.update(maxMom=150)
                if ((abs(object.dX) >= 1) or (abs(object.dY) >= 1)):
                    physics.velHandler(object, objects)


    logState()
    if (physics.grounded(myBall, objects)): loggerChild.debug("Pass")
    else: loggerChild.debug("Fail")

    myBall.prime(); myBall.launch();  # sends ball through the air
    for i in range(25):
        for object in objects:
            if isinstance(object, physics.Dynamic):
                if object is myBall:
                    myBall.momY += 1.5
                object.update(maxMom=150)
                if ((abs(object.dX) >= 1) or (abs(object.dY) >= 1)):
                    physics.velHandler(object, objects)
    logState()

    for i in range(50):
        for object in objects:
            if isinstance(object, physics.Dynamic):
                if object is myBall:
                    myBall.momY += 1.5
                object.update(maxMom=150)
                if ((abs(object.dX) >= 1) or (abs(object.dY) >= 1)):
                    physics.velHandler(object, objects)

    logState()
    if (physics.grounded(myBall, objects)): loggerChild.debug("Pass")
    else: loggerChild.debug("Fail")

    return [1,1,1,1,None] # test not failed, return points like normals

if __name__ == "__main__":
    print("main function!")