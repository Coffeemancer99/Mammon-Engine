import unittest
import src.minigame.timer.timer as timer
import src.minigame.fruitPanic.handGame as fruitPanic
import src.minigame.cannonPanic.cannonPanic as cannonPanic
import src.engine.scenecreator.tile as tile
import src.minigame.fruitPanic.handController as player
import pygame

class timerTests(unittest.TestCase):
    #87 LINES
    """

    ->White Box Test: Along with [test_timerCompleteFromEmpty], achieves Full Branch Coverage
        Testing
        def isFinished(self):
            if(self.currTime<=0):
                return 1 #If return 1 the game is over
            return 0 #If return 0 the game is still going
    """
    def test_timerCompleteFromNew(self): #Tests to see that a new timer still runs the game
        framerate = 1
        initialTime = 3
        theTimer = timer.timer(initialTime, framerate)
        self.assertFalse(theTimer.isFinished(), "This should be false, the game is not over as there is more time to exhaust")

    """
    
    ->Integration Test[bottom-up] Units being tested: halt(), isFinished()
     Along with [test_timerCompleteFromNew], achieves Full Branch Coverage
        Testing
        def isFinished(self):
            if(self.currTime<=0):
                return 1 #If return 1 the game is over
            return 0 #If return 0 the game is still going
        def halt(self):
            self.stopped=True
    """
    def test_timerCompleteFromEmpty(self):
        framerate = 1
        initialTime = 0
        theTimer = timer.timer(initialTime, framerate)
        self.assertTrue(theTimer.isFinished(), "This should be true, the game is over because the time is 0")

    """ This test proves the decrement function and if it decrements the appropriate times. It is used with isFinished
    to determine if the game is complete.
    
    ->Integration Test[bottom-up] Units being tested: decrement(), isFinished()
    : Along with [timerDecrementFromHaltedTimer], achieves Full Branch Coverage 
        Testing  
            def decrement(self):
                if(self.stopped==0):
                    self.currTime-=1
                    
    """
    def test_timerCompleteFromDecrements(self):
        framerate = 1
        initialTime = 3
        theTimer = timer.timer(initialTime, framerate)
        #Decrement the timer a few times
        theTimer.decrement()
        theTimer.decrement()
        theTimer.decrement()
        self.assertTrue(theTimer.isFinished(), "The timer is not halted, so the time should be at 0")

    """ 
    This test proves if a halted time will not decrement, useful for games that pause the timer but still have 
    occasional updates.
    
    ->White Box Test: Along with [test_timerCompleteFromDecrements], achieves Full Branch Coverage 
        Testing  
            def decrement(self):
                if(self.stopped==0):
                    self.currTime-=1

    """
    def test_timerDecrementFromHaltedTimer(self):
        framerate = 1
        initialTime = 3
        theTimer = timer.timer(initialTime, framerate)
        theTimer.halt() #Pause the timer (prevent it from being decremented)
        theTimer.decrement() #Try to decrement timer
        theTimer.decrement()  # Try to decrement timer
        theTimer.decrement()  # Try to decrement timer
        self.assertEqual(initialTime, theTimer.getTime(), "This should be the same as the initial timer because it is halted")

    """ 
    This test proves if the conversion from seconds to frames work. A sample minigame time at 100 seconds is used
    to compare with the conversion function
    
    ->White Box Test: Statement/Function coverage
        Testing  
        def secondsToFrames(self, seconds, framerate):
            return seconds*framerate

    """
    def test_framesToSecondsConversion(self):
        totalFrames = 3000 #The current minigame has 3000 frames (100 seconds)
        framerate = 30
        initialTime = 100
        theTimer = timer.timer(initialTime, framerate)
        self.assertEqual(totalFrames, theTimer.secondsToFrames(initialTime, framerate), "The framerate * seconds should be 30000 ")



class fruitTests(unittest.TestCase):

    """
    This test proves if the player is within the bounds of the game, the function should return True if the player is
    in range, and false if they are not.

    ->Integration Test[Bottom Up]: Using the tile class, pygame API, player class, and checkBounds()
    Along with [test_playerOutsideBounds], achieves Full Branch Coverage
    def checkBound(player, boundaries, scale):
        for currTile in boundaries:
            if currTile.rectCol.colliderect(player.rect.x + player.dX, player.rect.y, player.width, player.height):
                player.dX = 0
                return False
        return True
    """

    def test_playerInBounds(self):
        pirateSprite = pygame.image.load("data/assets/sprites/pirateHand.png")
        barVert = pygame.image.load("data/assets/sprites/barVert.png")
        brian = player.Player(448, 0, 1, pygame.K_w, #The palyer that we will check to see if they are in range
                              pygame.K_a, pygame.K_d, pygame.K_s,
                              pirateSprite, 0)
        boundaryLeft = tile.tile(barVert, -16, 0)
        windowX=512
        lineLength=3
        boundaryMid = tile.tile(barVert, windowX / 2 + lineLength, 0)
        boundaryRight = tile.tile(barVert, windowX + 16, 0)
        Lz = [boundaryLeft, boundaryMid, boundaryRight]  # Use as a "box collider" for checking players are in bounds
        self.assertTrue(fruitPanic.checkBound(brian, Lz, 1), "The player should be inside of the game area here")

    """
        This test proves if the player is within the bounds of the game, the function should return True if the player is
        in range, and false if they are not.
        
        ->Integration Test[Bottom Up]: Using the tile class, pygame API, player class, and checkBounds()
        Along with [test_playerInBounds], achieves Full Branch Coverage
    """

    def test_playerOutsideBounds(self):
        pirateSprite = pygame.image.load("data/assets/sprites/pirateHand.png")
        barVert = pygame.image.load("data/assets/sprites/barVert.png")
        brian = player.Player(-32, 0, 1, pygame.K_w,  # The palyer that we will check to see if they are in range
                              pygame.K_a, pygame.K_d, pygame.K_s,
                              pirateSprite, 0)
        boundaryLeft = tile.tile(barVert, -16, 0)
        windowX = 512
        lineLength = 3
        boundaryMid = tile.tile(barVert, windowX / 2 + lineLength, 0)
        boundaryRight = tile.tile(barVert, windowX + 16, 0)
        Lz = [boundaryLeft, boundaryMid, boundaryRight]  # Use as a "box collider" for checking players are in bounds
        self.assertFalse(fruitPanic.checkBound(brian, Lz, 1), "The player should be outside the game area here") #Player is outside game area, so this should be False

"""
    Cool Cam in a nutshell: Cannon Panic, 2v2 minigame where players fire a cannon at each other. 
    Black Box Tests
"""
class cannonPanicTests(unittest.TestCase):
    """
    This tests proves if a cannon has been successfully shot. The fire cannon method will return true if the cannon
    was successfully fired, or false if not

    ->Acceptance test/Black Box Test: Testing the utility of the cannon and ensuring that it cannot fire when it is not loaded.
    """
    def test_checkCannonFireEmpty(self):
        myCannon = cannonPanic.cannon()
        self.assertFalse(myCannon.fireCannon(), "The cannon should not be able to fire (False)")
    """
    ->Acceptance test/Black Box Test: Testing the utility of the cannon and ensuring that it cannot fire when it is not loaded.
    """
    def test_checkCannonFireLoaded(self):
        myCannon = cannonPanic.cannon()
        myCannon.addAmmo()
        self.assertTrue(myCannon.fireCannon(), "The cannon should be able to fire (True)")
    """
    ->Acceptance test/Black Box Test: Testing to see if a player is carrying a ball
    """
    def test_checkPlayerLoadsCannonBall(self):
        cannonLoader = cannonPanic.cannonLoader()
        cannonBall = cannonPanic.cannonBall(5,5)
        self.assertFalse(cannonLoader.carryingBall) #Check to see that they have no ball
        cannonLoader.pickUpBall(cannonBall) #Pick up the ball
        self.assertTrue(cannonLoader.carryingBall, "Player should be holding ball (True)") #Check to see that the ball is in their hands
    """
    ->Acceptance test/Black Box Test: Testing to see if a player unloading a ball works
    """
    def test_checkPlayerUnloadsCannonBall(self):
        cannonLoader = cannonPanic.cannonLoader()
        cannonBall = cannonPanic.cannonBall(5, 5)
        self.assertFalse(cannonLoader.carryingBall) #Check before they pick up the ball
        cannonLoader.pickUpBall(cannonBall) #Pick up the ball
        self.assertTrue(cannonLoader.carryingBall) #Check to see if they are carrying a ball
        cannonLoader.placeBall(cannonLoader) #Insert the ball
        self.assertFalse(cannonLoader.carryingBall, "Player should not be holding ball(False)") #Check to see if the ball is no longer in their hands

    """
    ->Acceptance test/Black box test: Testing to see that the cannon's ammo is empty after fire
    """
    def test_checkCannonFiredEmptied(self):
        myCannon = cannonPanic.cannon()
        myCannon.addAmmo()
        myCannon.fireCannon()
        self.assertFalse(myCannon.loaded, "Cannon should be empty (False)")










