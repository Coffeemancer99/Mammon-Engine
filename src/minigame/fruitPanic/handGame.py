import random
import src.minigame.fruitPanic.fruit as fruit
import src.engine.scenecreator.tile as tile
import src.minigame.fruitPanic.handController as player
import pygame
import time as time
import src.minigame.teamMasher.masher as masher

def dropFruit(scale, mainWindow, pId, position, randFruit):
    #Get the image of each fruit
    #TODO: Store this somewhere so we don't need to load the image every function call
    #Maybe pass in list of fruit images as function arg?
    coconut = pygame.image.load("data/assets/sprites/coconut.png")
    lemon = pygame.image.load("data/assets/sprites/lemon.png")
    pineapple = pygame.image.load("data/assets/sprites/pineapple.png")
    fruits = [coconut, lemon, pineapple]
    random.seed(time.time())
    lineWidth = 3 * scale
    #Get a random position for the fruit to drop and choose a random fruit
    fruitPost = random.randrange(position.left+lineWidth,position.right-lineWidth)
    cocoDrop = fruit.Fruit(fruitPost, position.top,  randFruit+1, scale, fruits[randFruit], pId,
                           (fruits[randFruit]==coconut)) #Check if the random fruit is a coconut (bad fruit = 1)
    return cocoDrop

#This function gets the dimensions of the window and draws a cross in the middle
#to segment each player. Scales for each window
#TODO: Put scale in a window object so we don't need to pass an additional arg every time?
def drawCross(mainWindow, scale):
    lineWidth = 3*scale
    windowX, windowY = pygame.display.get_surface().get_size()
    pygame.draw.line(mainWindow, (255, 255, 255), (windowX/2, 0), (windowX/2, windowY), lineWidth)
    pygame.draw.line(mainWindow, (255, 255, 255), (0, windowY/2), (windowX, windowY/2), lineWidth)

#Checks if a player is in bounds, similar to the tilemap collision code except this is restricted to x movement
def checkBound(player, boundaries, scale):
    for currTile in boundaries:
        if currTile.rectCol.colliderect(player.rect.x + player.dX, player.rect.y, player.width, player.height):
            player.dX = 0

def checkFruit(players, fruits):
    windowX, windowY = pygame.display.get_surface().get_size()
    existingFruit = [] #Fruit that were not caught yet
    for currFruit in fruits: #Every fruit that is active
        fruitFalling = True
        for player in players: #Every player that is active
            if (currFruit.fruitId == player.pId): #If the fruit "belongs" to the player
                if currFruit.rectCol.colliderect(player.rect.x + player.dX, player.rect.y, player.width, player.height):
                    fruitFalling = False #The fruit is no longer falling, don't add it at end
                    if(currFruit.badFruit==1): #If the player catches a bad fruit, they lose a few points
                        print("BAD")
                        player.score -= 3 #
                    else:
                        player.score += 1 #They caught it, so increase their score
                if(currFruit.rectCol.top>=player.rect.top): #The fruit fell on the ground...
                    fruitFalling = False #No longer falling, they messed up big time
        if(fruitFalling): #If the fruit was not caught, it is still falling. Put it in a list to hand off
            existingFruit.append(currFruit)
    return existingFruit #All the fruist that are still falling will be returned



#Testing out a 4 player minigame
#Fruits drop from the sky and each player has to catch them. They play as a pirate hook for this one
#When they catch a fruit they get a score, to win you must catch the most
def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30*scale) #Font for keeping score
    #Load in sprites and get dimensions of sprites and window
    groundSprite = pygame.image.load("data/assets/sprites/groundSprite1.png")
    groundSprite = pygame.transform.scale(groundSprite, ((groundSprite.get_width()) * scale, (groundSprite.get_height()) * scale))
    windowX, windowY = pygame.display.get_surface().get_size()
    pirateSprite = pygame.image.load("data/assets/sprites/pirateHand.png")
    barVert = pygame.image.load("data/assets/sprites/barVert.png")
    barVert = pygame.transform.scale(barVert, (barVert.get_width()*scale, barVert.get_height()*scale))
    pirateX = pirateSprite.get_width() * scale
    pirateY = pirateSprite.get_height() * scale
    lineLength = 3 * scale

    #Position of each player based off relative window length
    #TODO: Look at bug that causes sprites to be rendered differently on higher resolutions
    ##p1Pos = [windowX/4-windowX/16, (windowY/2)-pirateY-lineLength]
    p1Pos = [windowX/4-windowX/16, (windowY/2)-(pirateY/2)-lineLength]
    p2Pos = [windowX - windowX/4 -windowX/16, (windowY/2)-(pirateY/2)-lineLength]
    p4Pos = [windowX - windowX/4 - windowX/16, windowY-(pirateY/2)-lineLength]
    p3Pos = [windowX/2 - windowX/4 -windowX/16, windowY-(pirateY/2)-lineLength ]

    images=[None, barVert] #Static images
    boundaryLeft = tile.tile(barVert, -16, 0)
    boundaryMid= tile.tile(barVert, windowX/2 + lineLength, 0)
    boundaryRight = tile.tile(barVert, windowX+16, 0)
    Lz = [boundaryLeft, boundaryMid, boundaryRight] #Use as a "box collider" for checking players are in bounds
    #Initialize each player and give them their own inputs and respective position
    #TODO: Look at ways to use the pygame "joystick" library instead of keyboard inputs
    brian = player.Player(p1Pos[0],p1Pos[1], scale, pygame.K_w,
                          pygame.K_a, pygame.K_d, pygame.K_s,
                          pirateSprite, 0)
    jerry = player.Player(p2Pos[0],p2Pos[1], scale, pygame.K_UP,
                          pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN,
                          pirateSprite, 1)
    sally = player.Player(p3Pos[0],p3Pos[1], scale, pygame.K_t,
                          pygame.K_f, pygame.K_h, pygame.K_g,
                          pirateSprite, 2)
    henry = player.Player(p4Pos[0],p4Pos[1], scale, pygame.K_i,
                          pygame.K_j, pygame.K_l, pygame.K_k,
                          pirateSprite, 3)
    isRunning=True
    players = [brian, jerry, sally, henry] #Put all players in list for functional operator shenanigans

    #"Cameras" aka spicy box colliders to segment each player's window
    p1Camera = pygame.Rect(0, 0, windowX/2, windowY/2)
    p2Camera = pygame.Rect(windowX/2, 0, windowX/2, windowY/2)
    p3Camera = pygame.Rect(0, windowY/2, windowX/2, windowY/2)
    p4Camera = pygame.Rect(windowX/2, windowY/2, windowX/2, windowY/2)

    cameras = [p1Camera, p2Camera, p3Camera, p4Camera]#Put all cameras in list for functional operator shenanigans
    fruitTimer = 120 #When the timer reaches 0, drop a fruit and give a new timer randomly
    fruitList = []
    testGame = 1
    while(isRunning):
        clock.tick(framerate)
        #TODO: Work out a way to use functional operators and move it over to the window blit functionality
        #Get a render of everyone's current score
        score = myfont.render(str(brian.score), False, (50, 0, 0))
        score1 = myfont.render(str(jerry.score), False, (50, 0, 0))
        score2 = myfont.render(str(sally.score), False, (50, 0, 0))
        score3 = myfont.render(str(henry.score), False, (50, 0, 0))
        #If the user exits the game, quit out the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        mainWindow.fill((40, 120, 120)) #Fill with a solid color
        list(map(lambda x: mainWindow.blit(x.sprite, (x.rect.x, x.rect.y)), players))  # Draw players
        list(map(lambda x: mainWindow.blit(x.sprite, (x.rectCol.x, x.rectCol.y)), fruitList))  # Draw fruits
        #Render the score and draw the cross on top of everything
        #TODO: Work out a way to use functional operators with the GUI
        mainWindow.blit(score, p1Camera)
        mainWindow.blit(score1, p2Camera)
        mainWindow.blit(score2, p3Camera)
        mainWindow.blit(score3, p4Camera)
        drawCross(mainWindow, scale)


        if(testGame):
            testGame = False
            winner = masher.startGame(mainWindow, scale, framerate)

        if(fruitTimer<=0): #When the fruit timer ticks to 0(-1 every frame) everyone gets a new fruit
            randFruit = random.randrange(0, 3) #Grab a random fruit
            #coco=dropFruit(scale, mainWindow, 3, p3Camera, randFruit)
            for playerz in range(len(players)): #For every player, drop the same fruit for them (even playing field)
                nom = dropFruit(scale, mainWindow, playerz, cameras[playerz], randFruit)
                fruitList.append(nom) #Append that to the list of active fruits
           # coco = list(map(lambda x, y: dropFruit(scale, mainWindow, x, y, randFruit), range(len(players)), cameras))
            random.seed(time.time())
            fruitTimer=random.randrange(1,75) #Get a new fruit timer
        fruitList = checkFruit(players, fruitList) #Check for colisions of players and fruits
        if(len(fruitList)>0):
            list(map(lambda x: x.update(), fruitList))  #Fruit falling due to gravity
            list(map(lambda x: x.updateRect(), fruitList))  # Update collision
        fruitTimer -= 1

        list(map(lambda x: x.update(), players)) #Get player input
        list(map(lambda x: checkBound(x, Lz, scale), players)) #Confirm that players are in bounds of game
        list(map(lambda x: x.updateRect(), players)) #Update collision
        pygame.display.update() #Update display window

