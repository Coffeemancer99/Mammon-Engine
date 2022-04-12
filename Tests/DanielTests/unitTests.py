import src.engine.physics.physics as physics
import src.engine.physics.terrain as terrain
import src.game.boardGame.minigameManager as minigameManager
from src.engine.physics.spritegen import *
import Tests.DanielTests.virtualLevel.virtual as virtualLevel
import pygame
from io import StringIO
from functools import partial
import sys, os, shutil
import unittest
import pathlib
workingDirectory = pathlib.PurePosixPath('../../src/engine')
revertDirectory = pathlib.PurePosixPath('../../Tests/DanielTests')


def initialize():
    global obj; global outline;
    points = [[0, 0], [69, 420], [33, 380], [11, 69]]
    obj = terrain.from_polygon(points, 1)
    outline = []
    for point in obj.mask.outline():
        if point not in outline:
            outline.append(point)

initialize()# does prep work for some tests

class MyTestCase(unittest.TestCase):
    def testMoveX(self):
        # white-box test (need to know that velocity = momentum/mass)
        obj = physics.DynamicObject(pygame.image.load(workingDirectory.joinpath("data/assets/sprites/bluebox.png")), 1, 0, 0, mass = 10)
        obj.momX = 100; obj.momY = 100
        obj.update(airRes = 1, maxMom = 101)
        physics.velHandler(obj, [obj]) # no other objects to run into
        self.assertTrue(obj.x == 10, "horizontal movement not proportional to momentum")

    def testMoveY(self):
        # white-box test (need to know that velocity = momentum/mass)
        obj = physics.DynamicObject(pygame.image.load(workingDirectory.joinpath("data/assets/sprites/bluebox.png")),1, 0, 0, mass=10)
        obj.momX = 100; obj.momY = 100
        obj.update(airRes=1, maxMom=101)
        physics.velHandler(obj, [obj])  # no other objects to run into
        self.assertTrue(obj.y == 10, "vertical movement not proportional to momentum")

    def testOverlap(self):
        # black-box test
        t1 = terrain.from_polygon([[0,0],[100,0],[100,2]],1)
        t2 = terrain.from_polygon([[0,0],[0,100],[2,100]],1)
        self.assertTrue(t1.mask.overlap(t2.mask,(0,0)), "terrain sharing a vertex not overlapping")

    def testhorizontal(self):
        # White-box test. Along with testvertical, testDiagonalSimple, and testDiagonal, achieves branch coverage.
        p1 = (0,0); p2 = (10,0)
        tPoints = [(0,0,True), (5,0, True), (15,0, False), (1,2, False)] # Including the outcomes in tPoints allows for
        # fewer lines of code
        for tPoint in tPoints:
            self.assertTrue(terrain.is_between(p1, p2, (tPoint[0], tPoint[1])) == tPoint[2])
            self.assertTrue(terrain.is_between(p2, p1, (tPoint[0], tPoint[1])) == tPoint[2]) # tests that the same happens when the points are reversed

    # def is_between(point1, point2, testPoint):
    #     if testPoint in [point1, point2]:
    #         return True
    #
    #     point1 = list(point1);
    #     point2 = list(point2);
    #     testPoint = list(testPoint)
    #     point1[1] = -point1[1];
    #     point2[1] = -point2[1];
    #     testPoint[1] = -testPoint[1]
    #
    #     if (abs(point1[1] - point2[1]) > abs(point1[0] - point2[0])):  # if dY > dX
    #         for point in [point1, point2,
    #                       testPoint]:  # rotate points to minimize computer error with slope calculation
    #             backup = point[1]
    #             point[1] = point[0]
    #             point[0] = backup
    #     (x1, y1) = point1;
    #     (x2, y2) = point2;
    #     (x3, y3) = testPoint
    #
    #     if (y2 == y1):  # horizontal or rotated vertical line
    #         return ((y3 in [y1, y1 - 1, y1 + 1]) and (x3 >= min(x1, x2)) and (x3 <= max(x1, x2)))
    #
    #     m = (y2 - y1) / (x2 - x1)
    #     b = y1 - (m * x1)
    #
    #     y = m * x3 + b
    #     floor = math.floor(y)
    #
    #     return ((floor == y3) or (floor + 1 == y3) or (floor - 1 == y3))


    def testvertical(self):
        # White-box test
        p1 = (0,0); p2 = (0,10)
        tPoints = [(0,0,True), (0,5, True), (0,15, False), (2,1, False)]

        for tPoint in tPoints:
            self.assertTrue(terrain.is_between(p1, p2, (tPoint[0], tPoint[1])) == tPoint[2])
            self.assertTrue(terrain.is_between(p2, p1, (tPoint[0], tPoint[1])) == tPoint[2])

    def testDiagonalSimple(self):
        # White-box test
        p1 = (0,0); p2 = (10,10)
        self.assertTrue(terrain.is_between(p1,p2, (5,5)))
        self.assertFalse(terrain.is_between(p1,p2, (2,0)))
        self.assertTrue(terrain.is_between(p2,p1, (5,5))) # tests when the points are reversed
        self.assertFalse(terrain.is_between(p2,p1, (2,0)))

    def testDiagonal(self):
        # White-box test, ensures large numbers don't cause problems
        p1 = (0,0); p2 = (200,69)
        self.assertTrue(terrain.is_between(p1,p2,(100,35)))
        self.assertFalse(terrain.is_between(p1,p2,(100,37)))
        self.assertTrue(terrain.is_between(p2,p1,(100,35))) # tests when the points are reversed
        self.assertFalse(terrain.is_between(p2,p1,(100,37)))


    def testIsBtwLeftoversCreation(self): # are all points in an outline put into an edge?
        # Black-box test
        points = [[0,0],[69,420],[33,380],[11,69]]
        obj = terrain.from_polygon(points,1)
        outline = []; edges = []
        for point in obj.mask.outline():
            if point not in outline:
                outline.append(point)
        for i in range(len(points)):
            edges.append(list(filter((partial(terrain.is_between, points[i], points[(i + 1) % len(points)])), outline)))

        for point in outline:
            PointInEdges = False
            for edge in edges:
                if point in edge:
                    PointInEdges = True
                    break
            self.assertTrue(PointInEdges)

    def testIsBtwLeftovers(self): # are all points in an outline put into an edge?
        # Black-box test
        points = [[0,0],[69,420],[33,380],[11,69]]
        # obj = terrain.from_polygon(points,1)
        # outline = [];
        edges = []
        # for point in obj.mask.outline():
        #     if point not in outline:
        #         outline.append(point)
        for i in range(len(points)):
            edges.append(list(filter((partial(terrain.is_between, points[i], points[(i + 1) % len(points)])), outline)))

        for point in outline:
            PointInEdges = False
            for edge in edges:
                if point in edge:
                    PointInEdges = True
                    break
            self.assertTrue(PointInEdges)

    def testImpact1(self):
        # black-box test. The actual test needs to live in a module which can be loaded by minigameManager in testManager,
        # so I use pseudoAssert statements which ultimately cause the test to fail.
        # This is a holistic test which makes sure typical events are happening in the physics engine.
        # weird stuff with stdout is used to catch a print statement given on impact and to have a pseudoAssert statement
        temp_out = StringIO()
        backup = sys.stdout
        sys.stdout = temp_out

        if not virtualLevel.testImpact():
            sys.stdout = backup
            self.assertFalse(True, temp_out.getvalue().splitlines()[-1].rstrip()) # returns the statement given by the failed pseudoAssert
        sys.stdout = backup

        # def pseudoAssert(condition, statement, backup):
        #     if not condition:
        #         sys.stdout = backup
        #         print(statement)
        #         return True
        #     return False

        # def testImpact(window=None, scale=1, framerate=60):
        #     if not isInitialized: initialize(window, scale, framerate)
        #     print("Scale = {}\nWindow = {}\nFramerate = {}".format(scale, mainWindow, framerate))
        #     print("{TESTING virtualTests.testImpact}")
        #     temp_out = StringIO()
        #     backup = sys.stdout
        #     sys.stdout = temp_out
        #
        #     triY = 30;
        #     triX = 55
        #     triangle = terrain.from_polygon([[20, 345], [20 + triX, 311], [20, 311 - triY]], scale,
        #                                     color=(0, 255, 0, 255), name="triangle")
        #     ballX = 25;
        #     ballY = 20
        #     myBall = ball.Ball(generate_circle(20), scale, ballX, ballY, name="myBall", mass=4, maxpower=80)
        #     objects = []
        #     objects.append(myBall)
        #     objects.append(triangle)
        #     objects.append(physics.RectObject((500, 100), scale, 20, 300, name="net"))
        #     objects.append(physics.RectObject((100, 300), scale, 300, 20, name="backboard"))
        #
        #     # Level looks like this:
        #     # myBall    ||
        #     #   0       || backboard
        #     # #\        ||
        #     # ##\
        #     # Triangle
        #     #   _____________
        #     #        net
        #     for i in range(60):
        #         for object in objects:
        #             if isinstance(object, physics.Dynamic):
        #                 if object is myBall:
        #                     myBall.momY += 1.5
        #                 object.update(maxMom=150)
        #                 if ((abs(object.dX) >= 1) or (abs(object.dY) >= 1)):
        #                     physics.velHandler(object, objects)
        #
        #     if pseudoAssert(physics.grounded(myBall, objects), "myBall not grounded by triangle", backup): return None
        #     string = temp_out.getvalue()
        #     if pseudoAssert(string.count("IMPACT") == 1, "numImpacts != 1", backup): return None
        #
        #     myBall.prime();
        #     myBall.launch();  # sends ball through the air
        #     for i in range(25):
        #         for object in objects:
        #             if isinstance(object, physics.Dynamic):
        #                 if object is myBall:
        #                     myBall.momY += 1.5
        #                 object.update(maxMom=150)
        #                 if ((abs(object.dX) >= 1) or (abs(object.dY) >= 1)):
        #                     physics.velHandler(object, objects)
        #     string = temp_out.getvalue()
        #     if pseudoAssert(string.count("IMPACT") == 2, "no impact with backboard", backup): return None
        #
        #     for i in range(50):
        #         for object in objects:
        #             if isinstance(object, physics.Dynamic):
        #                 if object is myBall:
        #                     myBall.momY += 1.5
        #                 object.update(maxMom=150)
        #                 if ((abs(object.dX) >= 1) or (abs(object.dY) >= 1)):
        #                     physics.velHandler(object, objects)
        #
        #     if pseudoAssert(physics.grounded(myBall, objects), "myBall not grounded by net", backup): return None
        #     string = temp_out.getvalue()
        #     if pseudoAssert(string.count("IMPACT") == 3, "myBall didn't impact net", backup): return None
        #
        #     # sys.__stdout__.write(temp_out.getvalue())
        #     sys.stdout = backup
        #     # print(temp_out.getvalue())
        #     return [1, 1, 1, 1]  # test not failed, return points like normal

    def testImpact2(self):
        # black-box test
        temp_out = StringIO()
        backup = sys.stdout
        sys.stdout = temp_out
        if not virtualLevel.testImpact(ballPos=(25,30)): # ball starts closer to triangle
            sys.stdout = backup
            self.assertFalse(True, temp_out.getvalue().splitlines()[-1].rstrip()) # returns the statement given by the failed pseudoAssert
        sys.stdout = backup

    def testImpact3(self):
        #black-box test
        temp_out = StringIO()
        backup = sys.stdout
        sys.stdout = temp_out
        if not virtualLevel.testImpact(ballPow=120): # ball has much higher power when shot
            sys.stdout = backup
            self.assertFalse(True, temp_out.getvalue().splitlines()[-1].rstrip()) # returns the statement given by the failed pseudoAssert
        sys.stdout = backup



    def testManager(self):
        # integration test on minigameManager.runMinigame and physics
        # ensures that the typical physics tested by testImpact also work when loaded by minigameManager

        # make it so that /src/minigame only contains virtualTest, then use runMinigame, which randomly selects a minigame
        print("testManager: getcwd() = " + os.getcwd())
        os.rename('../../src/minigame', '../../src/minigame1')
        os.mkdir("../../src/minigame")
        os.mkdir("../../src/minigame/virtualTest"); shutil.copy("virtualLevel/launch.py", "../../src/minigame/virtualTest")
        os.mkdir("../../src/minigame/virtualTest2"); shutil.copy("virtualLevel/launch.py", "../../src/minigame/virtualTest2")
        try: minigameManager.runMinigame(pygame.Surface((1000,1000)), 1, 60, 4, turbo = 2)
        except:
            shutil.rmtree("../../src/minigame")
            os.rename("../../src/minigame1", "../../src/minigame")
            assert False
        shutil.rmtree("../../src/minigame")
        os.rename("../../src/minigame1", "../../src/minigame")

    def testSkew1(self):
        canvas = pygame.Surface((15, 5), flags=pygame.SRCALPHA)
        canvas.blit(generate_rectangle(2, 5, color = (0,1,1), scale=1), (5, 0))
        canvas.blit(generate_rectangle(3, 5, scale=1), (7, 0))
        array = pygame.PixelArray(canvas)
        row = [col[0] for col in array]
        newRow = skew_line(row, 10)
        self.assertTrue(len(row) == len(newRow), "skew change line length from {} to {}".format(len(row), len(newRow)))
        row = newRow
        for col in range(len(array)):
            array[col][0] = row[col]
        print(array)

    def testSkew2(self):
        canvas = pygame.Surface((100, 5), flags=pygame.SRCALPHA)
        canvas.blit(generate_rectangle(2, 5, color = (0,1,1), scale=1), (5, 0))
        canvas.blit(generate_rectangle(3, 5, scale=1), (7, 0))
        array = pygame.PixelArray(canvas)
        row = [col[0] for col in array]
        newRow = skew_line(row, 10)
        self.assertTrue(len(row) == len(newRow), "skew change line length from {} to {}".format(len(row), len(newRow)))
        row = newRow
        for col in range(len(array)):
            array[col][0] = row[col]
        print(array)

if __name__ == '__main__':
    unittest.main()
