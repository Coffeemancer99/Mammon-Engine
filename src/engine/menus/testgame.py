import src.engine.scenecreator.drawTileMap as drawTileMap
import src.engine.scenecreator.tile as tile
import src.engine.player.playerController as player
import src.engine.collision as collision

import pygame
def getGameMap():
    L=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
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

    brian = player.Player(300,150, scale)

    images = [None, groundSprite]
    currMap = getGameMap()
    staticTiles= drawTileMap.generateTiles(currMap, images)
    for tile in staticTiles:
        print(tile.rectCol.x, tile.rectCol.y)
    isRunning=True

    while(isRunning):
        clock.tick(framerate)
        brian.update()

        #isCollided = False
        drawTileMap.drawScene(mainWindow, currMap, images) #Redraws the main window
        mainWindow.blit(brian.sprite, (brian.rect.x, brian.rect.y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        collision.staticHandler(staticTiles, brian)
        brian.updateRect()

        # if isCollided == False:
        #     brian.isGrounded = False
        pygame.display.update()