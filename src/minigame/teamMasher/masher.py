import random
import src.minigame.fruitPanic.fruit as fruit
import src.engine.scenecreator.tile as tile
import src.minigame.fruitPanic.handController as player
import pygame
import time as time
from src.minigame.teamMasher import syncPlayer
from src.minigame.timer import timer
def drawLine(mainWindow, scale):
    lineWidth = 3*scale
    windowX, windowY = pygame.display.get_surface().get_size()
    pygame.draw.line(mainWindow, (255, 255, 255), (0, windowY/2), (windowX, windowY/2), lineWidth)

#Testing out a 2v2 minigame that involves teams having to make a circular motion, except the buttons are split amongst
#the team. They move a boat across a river after each successful circle, the first to the end wins or nobody wins
#if you don't get to the end within a minute.
def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate
    windowX, windowY = pygame.display.get_surface().get_size()
    pirateSprite = pygame.image.load("data/assets/sprites/pirateHand.png")
    t1Camera = pygame.Rect(0, 0, windowX, windowY / 2)
    t2Camera = pygame.Rect(0, windowY / 2, windowX, windowY/2)

    t1Pos = [windowX/4-pirateSprite.get_width(), windowY/4]
    t2Pos = [windowX/4-pirateSprite.get_width(), windowY-windowY/4]
    #The second person in each team holds the # of cycles
    #TEAM 1
    player1 = syncPlayer.masherPlayer(1, pygame.K_LEFT, pygame.K_RIGHT)
    player2 = syncPlayer.masherPlayer(2, pygame.K_UP, pygame.K_DOWN)
    #TEAM 2
    player3 = syncPlayer.masherPlayer(2, pygame.K_a, pygame.K_d)
    player4 = syncPlayer.masherPlayer(2, pygame.K_w, pygame.K_s)

    player1.isTurn=1
    player3.isTurn=1
    isRunning = True
    mainWindow.fill((40, 120, 120))  # Fill with a solid color
    drawLine(mainWindow, scale)
    gameTimer = timer.timer(60, framerate)
    currt1Score = 0 #Keep track of everyone's current score, used for determining winner
    currt2Score = 0
    while(isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        if(gameTimer.isFinished() or (t1Pos[0]>windowX) or (t2Pos[0]>windowX)):
            print("GAME OVER")
            isRunning=False

        #TEAM 1 INPUT
        if(player1.isTurn): #If it is player 1's turn, check for input and hand it off to p2, visa versa
            player2.isTurn = player1.getInput()
        else:
            player1.isTurn = player2.getInput()
        #TEAM 2 INPUT
        if(player3.isTurn): #If it is player 4's turn, check for input and hand it off to p3, visa versa
            player4.isTurn = player3.getInput()
        else:
            player3.isTurn = player4.getInput()
        #If the score has been updated for either team, update their appropriate score and position (move boat up)
        if(currt1Score<player2.score):
            print("SCORE++")
            currt1Score = player2.score
            t1Pos[0]+=12
        if (currt2Score<player4.score):
            print("SCORE++")
            currt2Score = player4.score
            t2Pos[0] += 12
        mainWindow.fill((40, 120, 120)) #Clear the screen
        drawLine(mainWindow, scale) #Split the screen in half
        mainWindow.blit(pirateSprite, (t1Pos[0], t1Pos[1])) #Draw each player's boat
        mainWindow.blit(pirateSprite, (t2Pos[0], t2Pos[1]))
        gameTimer.decrement()
        pygame.display.update()