import pygame
from src.engine.physics.physics import Object, DynamicObject, RectObject, DynamicRect
import src.engine.graphics.spritegen as spritegen
import src.engine.physics.physics as physics
import src.minigame.cannonPanic.playerController as player
import src.minigame.cannonPanic.cannonball as cannonball
import src.engine.scenecreator.tile as tile
import src.engine.scenecreator.drawTileMap as tilemap
from src.minigame.teamSwimmer import swimmerPlayer as swimmerPlayer
from src.minigame.teamSwimmer import seaItem as seaItem
from src.minigame.timer.timer import timer as timer


#Daniels code
def removeObj(objects, object):
    if isinstance(object, DynamicObject): object.halt()
    if object in objects:
        objects.remove(object)


#70 lines


def spawnCoin(objects, scale, xPos):

    scaleFancy = 0.075* scale
    coinSprite = spritegen.grab_sprite("data/assets/sprites/goodSprites/coinS.png", scaleFancy)




    coin = seaItem.seaItem(coinSprite, scale, xPos, 0, objects, 20)



    objects.append(coin)



def startGame(mainWindow, scale, framerate, gameStats):
    clock = pygame.time.Clock()  # Clock used for frame rate
    windowX, windowY = pygame.display.get_surface().get_size()
    isRunning = True

    scaleFancy = 0.06 * scale

    stage = spritegen.grab_sprite("data/assets/sprites/layers/stage.png", scale)
    seats = spritegen.grab_sprite("data/assets/sprites/layers/seats.png", scale)
    player1Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)
    player2Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)
    player3Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)
    player4Spr = spritegen.grab_sprite("data/assets/sprites/goodSprites/pirateDude.png", scaleFancy)
    objects = []
    pirate1= swimmerPlayer.swimmerPlayer(player1Spr, scale, windowX/4, windowY/4, objects, None, None, None)
    pirate2 = swimmerPlayer.swimmerPlayer(player2Spr, scale, windowX / 4 + windowX/8, windowY / 4, objects, None, None, None)
    pirate3 = swimmerPlayer.swimmerPlayer(player3Spr, scale, windowX / 2, windowY / 4, objects, None, None, None)
    pirate4 = swimmerPlayer.swimmerPlayer(player4Spr, scale, windowX / 2 + windowX / 8, windowY / 4, objects, None, None, None)

    objects.append(pirate1)
    objects.append(pirate2)
    objects.append(pirate3)
    objects.append(pirate4)
    seq = "data/assets/sounds/Another.mp3"
    ost = pygame.mixer.Sound(seq)
    ost.play(loops=-1)
    players=[pirate1, pirate2, pirate3, pirate4]
    coinDropDelay = 0.25
    coinDropTimer = timer(8, framerate)
    winnings = max(gameStats.earnings)
    while(isRunning):
        clock.tick(framerate)
        coinDropTimer.decrement()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
            if winnings <= 0:
                if event.type == pygame.KEYDOWN:
                    ost.fadeout(3000)
                    print(event)
                    return gameStats

        if (coinDropTimer.isFinished() and winnings>0):
            winnings-=1
            locations = []
            for i in range(len(gameStats.totalPlayers)):
                if(gameStats.totalPlayers[i]):
                    dropLoc = players[i].x
                    locations.append(dropLoc)
            for dropLoc in locations:
                spawnCoin(objects, scale, dropLoc)
            coinDropTimer = timer(coinDropDelay, framerate)



        for objectz in objects:  # rendering


            objectz.update()
            if(isinstance(objectz, seaItem.seaItem)):
                objectz.fall()

            if ((abs(objectz.dX) >= 1) or (abs(objectz.dY) >= 1)):
                collisions = physics.velHandler(objectz, objects)
                if(isinstance(objectz, seaItem.seaItem) and collisions!=[]):
                    objectz.damagedSound(0)
                    removeObj(objects, objectz)
        mainWindow.fill((0, 0, 0))
        mainWindow.blit(seats, (0, 0))
        mainWindow.blit(stage, (0, 0))
        for objectz in objects:  # rendering
            objectz.draw(mainWindow)


        pygame.display.update()