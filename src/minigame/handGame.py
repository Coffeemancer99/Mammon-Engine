import src.engine.scenecreator.drawTileMap as drawTileMap
import src.engine.scenecreator.tile as tile
import src.minigame.handController as player
import src.engine.collision as collision
import src.engine.menus.testgame as testgame
import pygame
import src.engine.scenecreator.drawTileMap as drawTileMap



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
    # if (player.rect.x + player.dX <= (-(player.width - 1) / 2)+lineWidth):
    #     print("FUCK YOU")
    #     player.dX = 0
    return player


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

    p1_camera = pygame.Rect(0, 0, 400, 300)
    p2_camera = pygame.Rect(400, 0, 400, 300)
    p3_camera = pygame.Rect(0, 300, 400, 300)
    p4_camera = pygame.Rect(400, 300, 400, 300)

    while(isRunning):
        clock.tick(framerate)
        mainWindow.fill((0, 0, 0))

        drawCross(mainWindow, scale)
        players= list(map(lambda x: x.update(), players))

        players = list(map(lambda x: checkBound(x, Lz, scale), players))


        map(lambda x: mainWindow.blit(x.sprite, (x.rect.x, x.rect.y)), players)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False

        brian.updateRect()
        jerry.updateRect()
        sally.updateRect()
        henry.updateRect()


        pygame.display.update()
