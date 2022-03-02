import pygame
from src.engine.andrewMenus import testGameMenu
from src.engine.menus import mainmenu
from src.engine.button import Button

'''
menu.py
Created by: Andrew Bunn
Generic menu class for creating menus filled with buttons
'''

class Menu:


    def __init__(self, title, buttons):
        """
        :param title: menu's title
        :param buttons: all the buttons for the menu
        """
        self.title = title
        self.buttons = buttons


    def launch(self, mainWindow, framerate, scale):
        """
        launches a menu and handles clicks
        :param mainWindow: the window to display the menu in
        :param framerate: set the refresh rate of the menu
        :param scale: what to scale the display by
        :return: returns button.handleClick() which will typically
                 launch a menu, minigame, or game
        """
        clock = pygame.time.Clock()

        # Paint screen background grey
        mainWindow.fill((55, 55, 55))

        for button in self.buttons:
            button.renderButton()

        pygame.display.update()
        isRunning = True

        while (isRunning):
            clock.tick(framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False

                # Handle Clicks
                if event.type == pygame.MOUSEBUTTONUP:
                    click = pygame.mouse.get_pos()

                    for button in self.buttons:
                        if button.wasClicked(click) == True:
                            if button.dummy == False:
                                # return whatever is defined to do onClick
                                return button.handleClick(click)
                            else:
                                button.handleClick(click)
                            break
