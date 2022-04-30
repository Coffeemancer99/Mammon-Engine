import src.engine.physics.terrain as terrain
from src.engine.graphics.spritegen import *
import Tests.DanielTests.virtualLevel.virtual as virtualLevel
import pygame
from io import StringIO
from functools import partial
import unittest
import logging;


def load_tests(loader, standard_tests, pattern):
    print("loading tests...")
    testCases = [TerrainTests, PhysicsTests, SkewTests]
    suite = unittest.TestSuite()
    for testCase in testCases:
        tests = loader.loadTestsFromTestCase(testCase)
        suite.addTests(tests)
    # tests = loader.loadTestsFromTestCase(PhysicsTests)
    # suite.addTests(tests)
    # tests = loader.loadTestsFromTestCase(TerrainTests)
    # suite.addTests(tests)
    return suite

class TerrainTests(unittest.TestCase):
    def setUp(self):
        global obj; global outline; global edges
        points = [[0, 0], [69, 420], [33, 380], [11, 69]]
        obj = terrain.from_polygon(points, 1)
        outline = []; edges  = []
        for point in obj.mask.outline():
            if point not in outline:
                outline.append(point)
        for i in range(len(points)):
            edges.append(list(filter((partial(terrain.is_between, points[i], points[(i + 1) % len(points)])), outline)))

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

    def testIsBtwLeftovers(self): # are all points in an outline put into an edge?
        # Black-box test
        points = [[0,0],[68, 420],[33,380],[11,69]]
        global outline; global obj; global edges
        for point in outline:
            PointInEdges = False
            for edge in edges:
                if point in edge:
                    PointInEdges = True
                    break
            self.assertTrue(PointInEdges)

class PhysicsTests(unittest.TestCase):
    def setUp(self):
        log_stream = StringIO()

        logging.basicConfig(stream = log_stream, format = '%(message)s',level = logging.DEBUG)
        logger = logging.getLogger()
        logger.debug("######testImpact1")
        virtualLevel.testImpact(ballPow = 120)
        while logger.hasHandlers():
            logger.removeHandler(logger.handlers[0])
        logger.addHandler(logging.StreamHandler(log_stream))
        logger.debug("######testImpact2")
        virtualLevel.testImpact(ballPow = 120)

        print("\n\ntemp_out contents: \n", log_stream.getvalue())
    #
    # def testMoveX(self):
    #     # white-box test (need to know that velocity = momentum/mass)
    #     obj = physics.DynamicObject(grab_sprite("data/assets/sprites/bluebox.png", 1), 1, 0, 0, mass = 10)
    #     obj.momX = 100; obj.momY = 100
    #     obj.update(airRes = 1, maxMom = 101)
    #     physics.velHandler(obj, [obj]) # no other objects to run into
    #     self.assertTrue(obj.x == 10, "horizontal movement not proportional to momentum")
    #
    # def testMoveY(self):
    #     # white-box test (need to know that velocity = momentum/mass)
    #     obj = physics.DynamicObject(grab_sprite("data/assets/sprites/bluebox.png", 1), 1, 0, 0, mass = 10)
    #     obj.momX = 100; obj.momY = 100
    #     obj.update(airRes=1, maxMom=101)
    #     physics.velHandler(obj, [obj])  # no other objects to run into
    #     self.assertTrue(obj.y == 10, "vertical movement not proportional to momentum")

    def testImpact1(self):
        # black-box test. The actual test needs to live in a module which can be loaded by minigameManager in testManager,
        # so I use pseudoAssert statements which ultimately cause the test to fail.
        # This is a holistic test which makes sure typical events are happening in the physics engine.
        # weird stuff with stdout is used to catch a print statement given on impact and to have a pseudoAssert statement
        pass

    # def testImpact2(self):
    #     # black-box test
    #     temp_out = StringIO()
    #     backup = sys.stdout
    #     sys.stdout = temp_out
    #     if not virtualLevel.testImpact(ballPos=(25,30)): # ball starts closer to triangle
    #         sys.stdout = backup
    #         self.assertFalse(True, temp_out.getvalue().splitlines()[-1].rstrip()) # returns the statement given by the failed pseudoAssert
    #     sys.stdout = backup
    #
    # def testImpact3(self):
    #     #black-box test
    #     temp_out = StringIO()
    #     backup = sys.stdout
    #     sys.stdout = temp_out
    #     if not virtualLevel.testImpact(ballPow=120): # ball has much higher power when shot
    #         sys.stdout = backup
    #         self.assertFalse(True, temp_out.getvalue().splitlines()[-1].rstrip()) # returns the statement given by the failed pseudoAssert
    #     sys.stdout = backup
    #
    #
    #
    # def testManager(self):
    #     # integration test on minigameManager.runMinigame and physics
    #     # ensures that the typical physics tested by testImpact also work when loaded by minigameManager
    #
    #     # make it so that /src/minigame only contains virtualTest, then use runMinigame, which randomly selects a minigame
    #     print("testManager: getcwd() = " + os.getcwd())
    #     os.rename('/src/minigame', '/src/minigame1')
    #     os.mkdir("/src/minigame")
    #     # os.mkdir("/src/minigame/virtualTest"); shutil.copy("/Tests/DanielTests/virtualLevel/launch.py", "/src/minigame/virtualTest")
    #     # os.mkdir("/src/minigame/virtualTest2"); shutil.copy("/Tests/DanielTests/virtualLevel/launch.py", "/src/minigame/virtualTest2")
    #     # try: minigameManager.runMinigame(pygame.Surface((1000,1000)), 1, 60, 4, turbo = 2)
    #     # except:
    #     #     shutil.rmtree("/src/minigame")
    #     #     os.rename("/src/minigame1", "/src/minigame")
    #     #     assert False
    #     # shutil.rmtree("/src/minigame")
    #     # os.rename("/src/minigame1", "/src/minigame")

class SkewTests(unittest.TestCase):
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
    # def testFail(self):
    #     self.fail("supposed to fail")
if __name__ == '__main__':
    unittest.main()
