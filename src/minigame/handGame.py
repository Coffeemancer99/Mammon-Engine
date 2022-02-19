import src.engine.scenecreator.drawTileMap as drawTileMap
import src.engine.scenecreator.tile as tile
import src.minigame.handController as player
import src.engine.collision as collision
import pygame




def drawCross(mainWindow, scale):
    windowX, windowY = pygame.display.get_surface().get_size()
    pygame.draw.line(mainWindow, (255, 255, 255), (windowX/2, 0), (windowX/2, windowY), 5*scale)
    pygame.draw.line(mainWindow, (255, 255, 255), (0, windowY/2), (windowX, windowY/2), 5*scale)

def checkBound(player, mainWindow):
    windowX, windowY = pygame.display.get_surface().get_size()
    if(player.rect.y <=0):
        pass
    if(player.rect.y >= windowX):
        pass
    if(player.rect.x <= 0):
        pass
    if(player.rect.x >= windowY):
        pass

#Testing out a 4 player minigame
#Each player gets to move "hands" around the screen to move some stuff around
def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    groundSprite = pygame.image.load("../../data/assets/sprites/groundSprite1.png")
    groundSprite = pygame.transform.scale(groundSprite, ((groundSprite.get_width()) * scale, (groundSprite.get_height()) * scale))
    windowX, windowY = pygame.display.get_surface().get_size()
    p1Pos = [windowX/4, windowY/4]
    p2Pos = [windowX - windowX/4, windowY/2 - windowY/4]
    p3Pos = [windowX - windowX/4, windowY - windowY/4]
    p4Pos = [windowX/2 - windowX/4, windowY - windowY/4]

    brian = player.Player(p1Pos[0],p1Pos[1], scale, pygame.K_w,
                          pygame.K_a, pygame.K_d, pygame.K_s,
                          pygame.image.load("../../data/assets/sprites/pirateHand.png"))

    jerry = player.Player(p2Pos[0],p2Pos[1], scale, pygame.K_UP,
                          pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN,
                          pygame.image.load("../../data/assets/sprites/pirateHand.png"))

    sally = player.Player(p3Pos[0],p3Pos[1], scale, pygame.K_t,
                          pygame.K_f, pygame.K_h, pygame.K_g,
                          pygame.image.load("../../data/assets/sprites/pirateHand.png"))

    henry = player.Player(p4Pos[0],p4Pos[1], scale, pygame.K_i,
                          pygame.K_j, pygame.K_l, pygame.K_k,
                          pygame.image.load("../../data/assets/sprites/pirateHand.png"))
    isRunning=True


    while(isRunning):
        clock.tick(framerate)
        drawTileMap.drawScene(mainWindow, [], [])  # Redraws the main window
        drawCross(mainWindow, scale)
        brian.update()
        jerry.update()
        sally.update()
        henry.update()

        checkBound(brian, mainWindow)


        mainWindow.blit(brian.sprite, (brian.rect.x, brian.rect.y))
        mainWindow.blit(jerry.sprite, (jerry.rect.x, jerry.rect.y))
        mainWindow.blit(sally.sprite, (sally.rect.x, sally.rect.y))
        mainWindow.blit(henry.sprite, (henry.rect.x, henry.rect.y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False

        brian.updateRect()
        jerry.updateRect()
        sally.updateRect()
        henry.updateRect()


        pygame.display.update()
