import random
import src.minigame.fruitPanic.fruit as fruit
import src.engine.scenecreator.tile as tile
import src.minigame.fruitPanic.handController as player
import pygame
import time as time

def dropFruit(scale, mainWindow):
    windowX, windowY = pygame.display.get_surface().get_size()
    coconut = pygame.image.load("data/assets/sprites/coconut.png")
    lemon = pygame.image.load("data/assets/sprites/lemon.png")
    pineapple = pygame.image.load("data/assets/sprites/pineapple.png")
    fruits = [coconut, lemon, pineapple]
    random.seed(time.time())
    randFruit = random.randrange(0,3)
    fruitPost = random.randrange(0,int(windowX/4))
    cocoDrop = fruit.Fruit(fruitPost, 0,  randFruit+1, scale, fruits[randFruit])
    return cocoDrop

def drawCross(mainWindow, scale):
    lineWidth = 3*scale
    windowX, windowY = pygame.display.get_surface().get_size()
    pygame.draw.line(mainWindow, (255, 255, 255), (windowX/2 +lineWidth, 0), (windowX/2 +lineWidth, windowY), lineWidth)
    pygame.draw.line(mainWindow, (255, 255, 255), (0, windowY/2 + lineWidth), (windowX, windowY/2 + lineWidth), lineWidth)

def checkBound(player, boundaries, scale):
    windowX, windowY = pygame.display.get_surface().get_size()
    lineWidth = 3*scale
    xVal =(player.rect.x * -1)
    for currTile in boundaries:

        if currTile.rectCol.colliderect(player.rect.x + player.dX, player.rect.y, player.width, player.height):
            player.dX = 0




def checkFruit(players, fruits):
    windowX, windowY = pygame.display.get_surface().get_size()
    existingFruit = [] #Fruit that were not caught yet
    for currFruit in fruits:
        fruitFalling = True
        for player in players:
            if currFruit.rectCol.colliderect(player.rect.x + player.dX, player.rect.y, player.width/2, player.height/4):
                fruitFalling = False
                print(player.score)
                player.score += 1
        if(fruitFalling):
            existingFruit.append(currFruit)
    return existingFruit



#Testing out a 4 player minigame
#Each player gets to move "hands" around the screen to move some stuff around
def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    groundSprite = pygame.image.load("data/assets/sprites/groundSprite1.png")
    groundSprite = pygame.transform.scale(groundSprite, ((groundSprite.get_width()) * scale, (groundSprite.get_height()) * scale))
    windowX, windowY = pygame.display.get_surface().get_size()
    pirateSprite = pygame.image.load("data/assets/sprites/pirateHand.png")
    pirateX = pirateSprite.get_width() * scale
    pirateY = pirateSprite.get_height() * scale
    lineLength = 3 * scale
    p1Pos = [windowX/4-windowX/16, (windowY/2)-(pirateY/2)-lineLength]
    p2Pos = [windowX - windowX/4 -windowX/16, (windowY/2)-(pirateY/2)-lineLength]
    p3Pos = [windowX - windowX/4 - windowX/16 , windowY-(pirateY/2)-lineLength]
    p4Pos = [windowX/2 - windowX/4 -windowX/16, windowY-(pirateY/2)-lineLength ]

    barVert = pygame.image.load("data/assets/sprites/barVert.png")
    barVert = pygame.transform.scale(barVert, (barVert.get_width()*scale, barVert.get_height()*scale))
    images=[None, barVert]
    boundaryLeft = tile.tile(barVert, -16, 0)
    boundaryMid= tile.tile(barVert, windowX/2 + lineLength, 0)
    boundaryRight = tile.tile(barVert, windowX+16, 0)
    Lz = [boundaryLeft, boundaryMid, boundaryRight]

    brian = player.Player(p1Pos[0],p1Pos[1], scale, pygame.K_w,
                          pygame.K_a, pygame.K_d, pygame.K_s,
                          pirateSprite)

    jerry = player.Player(p2Pos[0],p2Pos[1], scale, pygame.K_UP,
                          pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN,
                          pirateSprite)

    sally = player.Player(p3Pos[0],p3Pos[1], scale, pygame.K_t,
                          pygame.K_f, pygame.K_h, pygame.K_g,
                          pirateSprite)

    henry = player.Player(p4Pos[0],p4Pos[1], scale, pygame.K_i,
                          pygame.K_j, pygame.K_l, pygame.K_k,
                          pirateSprite)
    isRunning=True

    players = [brian, jerry, sally, henry]

    p1Camera = pygame.Rect(0, 0, windowX/4, windowY/4)
    p2Camera = pygame.Rect(windowX - windowX/4, 0, windowX/4, windowY/4)
    p3Camera = pygame.Rect(0, windowY - windowY/4, windowX/4, windowY/4)
    p4Camera = pygame.Rect(windowX - windowX/4, windowY - windowY/4, windowX/4, windowY/4)
    cameras = [p1Camera, p2Camera, p3Camera, p4Camera]
    coco=None
    fruitTimer = 120
    fruitList = []

    while(isRunning):
        clock.tick(framerate)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        mainWindow.fill((0, 0, 0))

        drawCross(mainWindow, scale)
        if(fruitTimer<=0):
            coco=dropFruit(scale, mainWindow)
            fruitList.append(coco)

            random.seed(time.time())
            print("YO")
            fruitTimer=random.randrange(1,75)
        fruitList = checkFruit(players, fruitList)
        if(len(fruitList)>0):
            list(map(lambda x: x.update(), fruitList))  #Fruit falling
            list(map(lambda x: x.updateRect(), fruitList))  # Update collision
            list(map(lambda x: mainWindow.blit(x.sprite, (x.rectCol.x, x.rectCol.y)), fruitList))  # Draw fruits
        fruitTimer -= 1

        list(map(lambda x: x.update(), players)) #Get player input
        list(map(lambda x: checkBound(x, Lz, scale), players)) #Confirm that players are in bounds of game
        list(map(lambda x: x.updateRect(), players)) #Update collision
        list(map(lambda x: mainWindow.blit(x.sprite, (x.rect.x, x.rect.y)), players))  # Draw players
        pygame.display.update() #Update display window
