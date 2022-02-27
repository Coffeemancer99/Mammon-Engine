
import src.engine.scenecreator.drawTileMap as drawTileMap
import src.engine.scenecreator.tile as tile
import src.engine.player.playerController as player
import src.engine.collision as collision
import src.engine.physics.physics as physics
import src.minigame.physicsTest.ball as ball
import pygame
def getGameMap():
    L=[
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    ]
    return L

def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    #Load in sprites and get dimensions of sprites and window
    groundSprite = pygame.image.load("data/assets/sprites/groundSprite1.png")
    groundSprite = pygame.transform.scale(groundSprite, ((groundSprite.get_width()) * scale, (groundSprite.get_height()) * scale))

    coco = ball.Ball(pygame.image.load("data/assets/sprites/coconut.png"), scale, 240, 300, name="coco")
    lemon = physics.Object(pygame.image.load("data/assets/sprites/lemon.png"), 3*scale, 280, 300, name="lemon")
    currMap = getGameMap()


    isRunning=True
    print("\n-----------------------------------------------")
    print("PHYSICS TESTING")
    print("-----------------------------------------------")
    print("press u-i-o-j-k to manipulate the cannon settings")
    print("WASD to move, C to stop")

    while(isRunning):
        clock.tick(framerate)
        drawTileMap.drawScene(mainWindow, currMap, images)  # Redraws the main window



        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            coco.momY -= 3
        if key[pygame.K_s]:
            coco.momY += 3
        if key[pygame.K_a]:
            coco.momX -= 3
        if key[pygame.K_d]:
            coco.momX += 3
        # if key[pygame.K_f]:
        #     coco.x += 1
        if key[pygame.K_c]:
            coco.momX = 0
            coco.momY = 0

        if key[pygame.K_b]:
            print("\n------------------------------")
            print(coco)
            print(lemon)
            print("------------------------------\n")


        coco.update()
        if((abs(coco.dX) >= 1) or (abs(coco.dY) >= 1)):
            physics.velHandler(coco, lemon)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        lemon.draw(mainWindow)
        coco.draw(mainWindow)
        pygame.display.update()