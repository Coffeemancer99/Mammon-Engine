
import src.engine.scenecreator.drawTileMap as drawTileMap
import src.engine.scenecreator.tile as tile
import src.engine.player.playerController as player
import src.engine.collision as collision
import src.engine.physics.physics as physics
import src.minigame.physicsTest.ball as ball
import pygame
import time
def getGameMap():
    L=[
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    return L

def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    #Load in sprites and get dimensions of sprites and window
    groundSprite = pygame.image.load("data/assets/sprites/groundSprite1.png")
    groundSprite = pygame.transform.scale(groundSprite, ((groundSprite.get_width()) * scale, (groundSprite.get_height()) * scale))
    images = [None, groundSprite]

    coco = ball.Ball(pygame.image.load("data/assets/sprites/coconut.png"), scale, 80, 185, name="coco")
    lemon = physics.DynamicObject(pygame.image.load("data/assets/sprites/lemon.png"), scale, 80, 300, name="lemon")
    box = physics.Object(pygame.image.load("data/assets/sprites/groundSprite1.png"), scale*5, 150,300, name="box")
    objects = [coco, lemon, box]

    currMap = getGameMap()

    # ------------------------------
    # "coco", (x, y) = ("376", "333"), (dX, dY) = ("0", "0"), (momX, momY) = ("0", "0")
    # "lemon", (x, y) = ("280", "300")
    # ------------------------------

    isRunning=True
    print("\n-----------------------------------------------")
    print("PHYSICS TESTING")
    print("-----------------------------------------------")
    print("press u-i-o-j-k to manipulate the cannon settings")
    print("WASD and arrow keys to move around coconut and lemon,space to jump the coconut")

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
        if key[pygame.K_SPACE]:
            if physics.grounded(coco, objects, onlyStatics=True):
                coco.momY -= 25

        # if key[pygame.K_f]:
        #     coco.x -= 1
        #     time.sleep(.3)
        # if key[pygame.K_g]:
        #     coco.x += 1
        #     time.sleep(.3)
        # if key[pygame.K_h]:
        #     (coco.x, coco.y) = (376, 333)
        #     coco.momX = 0
        #     coco.momY = 0
        #     time.sleep(.3)

        if key[pygame.K_c]:
            coco.momX = 0
            coco.momY = 0

        if key[pygame.K_UP]:
            lemon.momY -= 3
        if key[pygame.K_DOWN]:
            lemon.momY += 3
        if key[pygame.K_LEFT]:
            lemon.momX -= 3
        if key[pygame.K_RIGHT]:
            lemon.momX += 3

        if key[pygame.K_b]:
            print("\n######################################")
            for object in objects:
                print(object)
            print("######################################")
            time.sleep(0.3)

        # if key[pygame.K_r]:
        #     coco.dX = -1
        #     time.sleep(.3)
        # if key[pygame.K_t]:
        #     coco.dX = 1
        #     time.sleep(.3)

        for object in objects: # Physics, movement
            if isinstance(object, physics.DynamicObject):
                if object is coco:
                    coco.momY += 1
                object.update()
                if ((abs(object.dX) >= 1) or (abs(object.dY) >= 1)):
                    physics.velHandler(object, objects)

        for object in objects: # rendering
            object.draw(mainWindow)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        pygame.display.update()