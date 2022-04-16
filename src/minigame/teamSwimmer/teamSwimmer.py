import math
import time

import src.minigame.physicsTest.ball as ball
import src.minigame.cannonPanic.cannonPanicController as cannonPlayer
import pygame
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
import src.engine.physics.spritegen as spritegen
import src.engine.physics.physics as physics
import src.minigame.cannonPanic.playerController as player
import src.minigame.cannonPanic.cannonball as cannonball
import src.engine.scenecreator.tile as tile
import src.engine.scenecreator.drawTileMap as tilemap
from src.minigame.teamSwimmer import swimmerPlayer as swimmerPlayer
from src.minigame.teamSwimmer import seaItem as seaItem
import random
from src.minigame.timer.timer import timer as timer
from src.minigame.minigameData import minigameData as minigameData


#Daniels code
def removeObj(objects, object):
    if isinstance(object, DynamicObject): object.halt()
    if object in objects:
        objects.remove(object)

"""
    spawnCoin: This function spawns a coin in a random position. If the spawned coin location occupies the same
    space as an item already in the scene, it will assign a new position to that coin. There is also the chance
    this falling item may be a bad item(skull) which will cause the player to lose three points instead of gaining 1.
    Parameters:
        :param objects: The list of objects in the scene
        :param scale: The scale of the window
        :param bad: An optional parameter that determines if the parameter is a bad item or now  
"""
def spawnCoin(objects, scale, bad=False):
    random.seed(time.time())
    windowX, windowY = pygame.display.get_surface().get_size()
    scaleFancy = 0.05* scale
    coinSprite = spritegen.grab_sprite("data/assets/sprites/goodSprites/coinS.png", scaleFancy)
    skullSprite = spritegen.grab_sprite("data/assets/sprites/goodSprites/skull.png", scaleFancy)
    isValidDrop = True
    xPos = 0
    coin = None

    randSpeed =  random.randint(1,8)
    if(bad):
        coin = seaItem.seaItem(skullSprite, scale, xPos, 0, objects, randSpeed, bad)

        coin.cost = -3
    else:
        coin = seaItem.seaItem(coinSprite, scale, xPos, 0, objects, randSpeed)
        coin.cost = 1
    while(isValidDrop):
        xPos = random.randint(coinSprite.get_width(), windowX)-coinSprite.get_width()
        coin.x = xPos
        agentEnable = False
        for agents in objects:
            if ((coin.mask.overlap(agents.mask,(agents.x - coin.x, agents.y - coin.y)))):
               agentEnable = True
        if not agentEnable:
            isValidDrop = False

    objects.append(coin)

"""
    TeamSwimmer: This game is a 2v2 minigame where players assume the role of a barrel-submarine to grab coins which
    are mysteriously falling into the ocean. Controls are split between each team member, such that one person
    controls the steering (left and right movement) and the other player controls the depth (up and down). Coins 
    get the team 1 point, skulls make the team lose 3 points and immobile for 1.5 seconds. Whoever collects the most
    points within 60 seconds wins the minigame and is awarded back in the board game state. 
     
    startGame: This function loads all initial assets and sets up the physics properties for each team. The controls
    are also defined at the beginning here which splits it between each team member. The main game loop is the 
    middle ground for connecting the rendering and game logic together. Rendering, physics handling, and player input 
    are all handled at a farme-by-frame basis.
    Parameters: 
        :param mainWindow: The main window that the user sees (pygame object)
        :param scale: The scale of the assets, default is 1 but can be scaled further
        :param framerate: The framerate that the game runs in, the default is 60.    
"""
def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    windowX = mainWindow.get_width() #Dimensions of window
    windowY = mainWindow.get_height()
    isRunning = True #Determines if the main game loop is running
    gravity = 2.0 * scale
    scaleFancy = 0.0375 * scale #A smaller scale for the giant fancy sprites
    #Load game assets and set up starting posiitons
    subSprite = spritegen.grab_sprite("data/assets/sprites/goodSprites/barrelSub.png", scaleFancy)
    bg1 = spritegen.grab_sprite("data/assets/sprites/layers/layer1.png", scale)
    bg2 = spritegen.grab_sprite("data/assets/sprites/layers/layer2.png", scale)
    bg = [bg1, bg2]
    vertSprite = spritegen.grab_sprite("data/assets/sprites/barVert.png", scale)
    horSprite = spritegen.grab_sprite("data/assets/sprites/horVert.png", scale)
    team1X = subSprite.get_width()
    team1Y = windowY - windowY/2
    team2X = windowX - subSprite.get_width()*2
    team2Y = windowY - windowY/2
    print(windowY)
    #The controls for team 1
    #This is the player who moves the sub left and right
    team1AControls = {
        "left": pygame.K_a,
        "right": pygame.K_d
    }
    #This is the player who controls the depth
    team1BControls = {
        "up": pygame.K_w
    }

    #The controls for team 2
    #This is the player who moves the sub left and right
    team2AControls = {
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT
    }
    #This is the player who controls the depth
    team2BControls = {
        "up": pygame.K_UP
    }
    objects = []
    maxHeight = windowY/8
    team1Sub = swimmerPlayer.swimmerPlayer(subSprite, scale, team1X, team1Y, objects, team1AControls, team1BControls, maxHeight)
    team2Sub = swimmerPlayer.swimmerPlayer(subSprite, scale, team2X, team2Y, objects, team2AControls, team2BControls, maxHeight)

    vert1 = DynamicObject(vertSprite, scale, -1, 0, objects)
    vert2 = DynamicObject(vertSprite, scale, windowX, 0, objects)
    hor1 = DynamicObject(horSprite, scale, 0, -1, objects)
    hor2 = DynamicObject(horSprite, scale, 0, windowY, objects)
    pygame.mixer.init()
    bloopSound = "data/assets/sounds/sfx.mp3"

    sound1 = pygame.mixer.Sound(bloopSound)
    theSound=pygame.mixer.music.load(bloopSound) #Load the bloop sound
    sound1.set_volume(100000000)
    sound1.play(loops=-1)
    gameTimer = timer(60, framerate)
    # pygame.mixer.music.play(loops=-1) #Loop forever
    pygame.event.wait()


    objects.extend((team1Sub, team2Sub, vert1, vert2, hor1, hor2))
    #Extend is a function that lets you append multiple things at once
    #Old garbage code:
        # objects.append(team1Sub)
        # objects.append(team2Sub)
        # objects.append(vert1)
        # objects.append(vert2)
        # objects.append(hor1)
        # objects.append(hor2)
    timers = []
    goldTimer = timer(3, framerate)
    timers.append(goldTimer)
    EXTRA_GOLD = False
    if(EXTRA_GOLD):
        goldTimer2 = timer(3, framerate)
        timers.append(goldTimer2)
    while(isRunning):
        clock.tick(framerate)
        gameTimer.decrement()
        if(gameTimer.isFinished()):
            print("==========GAME OVER===========")
            gameStats=""
            if(team1Sub.score>team2Sub.score):
                gameStats = minigameData.minigameData(1, 1, 0, 0, 10, 10, 0, 0)

                print("Team 1 won")
            elif(team1Sub.score<team2Sub.score):
                gameStats = minigameData.minigameData(0, 0, 1, 1, 0, 0, 10, 10)
                print("Team 2 wons")
            else:
                gameStats = minigameData.minigameData(0, 0, 0, 0, 0, 0, 0, 0)
                print("Draw!")
            return gameStats
        primedInputs = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
            #Get every time the button is held up (Prevent holding down the button)_
            if event.type == pygame.KEYUP:
                primedInputs.append(event)



        for i in range(len(timers)):
            timers[i].decrement()
            if(timers[i].isFinished()):
                val = random.randint(0,50)%8
                val = (val<=1)
                timers[i] = timer(random.randint(0,3), framerate)
                spawnCoin(objects, scale, val)

        for objectz in objects:
            if(isinstance(objectz, physics.Dynamic)):
                objectz.update(maxMom=15)

            if(isinstance(objectz, swimmerPlayer.swimmerPlayer)):
                objectz.floatSub(primedInputs)

            if (isinstance(objectz, seaItem.seaItem)):
                objectz.fall()

            if ((abs(objectz.dX) >= 1) or (abs(objectz.dY) >= 1)):
                collisions = physics.velHandler(objectz, objects)
                if(collisions!=[]):
                    if (isinstance(objectz, seaItem.seaItem)):
                        for agents in collisions:
                            if(isinstance(agents, swimmerPlayer.swimmerPlayer)):
                                agents.changeScore(objectz.cost)
                                objectz.damagedSound(agents.consec)
                                if(objectz.isBad):
                                    agents.paralyzed=True
                                    agents.consec=0
                                else:
                                    agents.consec+=1
                                print("agents score %s" %agents.score)
                                break #only want one agent getting the loot
                        removeObj(objects, objectz)
                    if (isinstance(objectz, swimmerPlayer.swimmerPlayer)):
                        for agents in collisions:
                            if(isinstance(agents, seaItem.seaItem)):
                                objectz.changeScore(agents.cost)
                                agents.damagedSound(objectz.consec)
                                if(agents.isBad):
                                    objectz.paralyzed=True
                                    agents.consec = 0
                                else:
                                    objectz.consec+=1


                                removeObj(objects, agents)
        mainWindow.fill((0, 0, 0))
        mainWindow.blit(bg1, (0,0))
        for objectz in objects:
            mainWindow.blit(objectz.sprite, (objectz.x, objectz.y))
        mainWindow.blit(bg2, (0, 0))
        pygame.display.update()
