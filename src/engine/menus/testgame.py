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
    #Load in static assets
    groundSprite = pygame.image.load("../../data/assets/sprites/groundSprite1.png")
    groundSprite = pygame.transform.scale(groundSprite, ((groundSprite.get_width()) * scale, (groundSprite.get_height()) * scale))
    #Create player
    brian = player.Player(300,150, scale, pygame.K_w,
                          pygame.K_a, pygame.K_d,
                          pygame.image.load("../../data/assets/sprites/bolSprite.png"))

    images = [None, groundSprite]
    currMap = getGameMap()
    #Get a reference of the static tilemaps for colisions and draw it
    staticTiles= drawTileMap.generateTiles(currMap, images)
    for tile in staticTiles:
        print(tile.rectCol.x, tile.rectCol.y)
    isRunning=True

    while(isRunning):
        clock.tick(framerate)
        brian.update() #Check if user has pressed anything and update player position
        drawTileMap.drawScene(mainWindow, currMap, images) #Redraws the main window
        mainWindow.blit(brian.sprite, (brian.rect.x, brian.rect.y)) #Draws players after
        for event in pygame.event.get(): #If the user quits out, exit window
            if event.type == pygame.QUIT:
                isRunning=False
        collision.staticHandler(staticTiles, brian) #Check if player is colliding with anything
        brian.updateRect() #Update their position (rectangle collider)

        pygame.display.update()