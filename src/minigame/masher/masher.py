

import random
import src.minigame.fruitPanic.fruit as fruit
import src.engine.scenecreator.tile as tile
import src.minigame.fruitPanic.handController as player
import pygame
import time as time
from src.minigame.teamMasher import masherPlayer
from src.minigame.timer import timer
def drawLine(mainWindow, scale):
    lineWidth = 3*scale
    windowX, windowY = pygame.display.get_surface().get_size()
    pygame.draw.line(mainWindow, (255, 255, 255), (0, windowY/2), (windowX, windowY/2), lineWidth)
#Testing out a 4 player minigame
#Fruits drop from the sky and each player has to catch them. They play as a pirate hook for this one
#When they catch a fruit they get a score, to win you must catch the most
def startGame(mainWindow, scale, framerate):
    clock = pygame.time.Clock()  # Clock used for frame rate

    windowX, windowY = pygame.display.get_surface().get_size()

    t1Camera = pygame.Rect(0, 0, windowX, windowY / 2)
    t2Camera = pygame.Rect(0, windowY / 2, windowX, windowY/2)

    t1Masher = masherPlayer.masherPlayer(1, pygame.K_a, pygame.K_d) #The teamMasher for team 1
    t2Masher = masherPlayer.masherPlayer(2, pygame.K_LEFT, pygame.K_RIGHT) #The teamMasher for team 2
    isRunning = True
    mainWindow.fill((40, 120, 120))  # Fill with a solid color
    drawLine(mainWindow, scale)
    gameTimer = timer.timer(15, framerate)
    while(isRunning):
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
        if(gameTimer.isFinished()): #If the timer runs out, print the scores of each player
            print("GAME OVER")
            print(t1Masher.cycles)
            print(t2Masher.cycles)
            isRunning=False
        gameTimer.decrement()
        t1Masher.getInput()
        t2Masher.getInput()
        pygame.display.update() #Update display window