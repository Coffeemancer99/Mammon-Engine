import src.engine.scenecreator.drawTileMap as drawTileMap
import src.engine.scenecreator.tile as tile
import src.engine.player.playerController as player
import pygame
def getGameMap():
    L=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1],
        [1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    return L

def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    #TEST IMAGES

    #groundTile = tile.tile("../../data/assets/sprites/groundSprite1.png", 0, 0)
    #groundTile.scale(scale)
    groundSprite = pygame.image.load("../../data/assets/sprites/groundSprite1.png")
    groundSprite = pygame.transform.scale(groundSprite, ((groundSprite.get_width()) * scale, (groundSprite.get_height()) * scale))

    brian = player.Player(300,150)

    images = [None, groundSprite]
    currMap = getGameMap()
    staticTiles=drawTileMap.drawScene(mainWindow, currMap, images)
    for tile in staticTiles:
        print(tile.rectCol.x, tile.rectCol.y)
    isRunning=True

    while(isRunning):
        clock.tick(framerate)
        brian.update()
        isCollided = False
        tile = drawTileMap.drawScene(mainWindow, currMap, images)
        mainWindow.blit(brian.sprite, (brian.rect.x, brian.rect.y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
            # if event.type == pygame.MOUSEBUTTONUP:
                # pos = pygame.mouse.get_pos()
                # mainWindow.blit(groundSprite, pos)
                # rect=groundSprite.get_rect()
                # rect.x=pos[0]
                # rect.y=pos[1]
                # #print(rect.x)
        for tile in staticTiles:
            if tile.rectCol.colliderect(brian.rect):
                isCollided=True
                print("collision")
                brian.isGrounded=True
                brian.rect.y=tile.rectCol.top-32
            if isCollided==False:
                brian.isGrounded=False

        pygame.display.update()