import pygame

'''
menu.py
Created by: Andrew Bunn
Generic menu class for creating menus filled with buttons
'''


class Menu:

    def __init__(self, title, buttons, images=None, scaleFactors=None):
        """
        :param title: menu's title
        :param buttons: all the buttons for the menu
        """
        self.title = title
        self.buttons = buttons
        self.images = images
        self.scaleFactors = scaleFactors

    def launch(self, mainWindow, framerate):
        """
        launches a menu and handles clicks
        :param mainWindow: the window to display the menu in
        :param framerate: set the refresh rate of the menu
        :param scale: what to scale the display by
        :return: returns button.handleClick() which will typically
                 launch a menu, minigame, or game
        """
        clock = pygame.time.Clock()
        listOfButtons = []

        # Paint screen background grey
        mainWindow.fill((55, 55, 55))

        for button in self.buttons:
            button.renderButton()

        if self.images is not None:
            for image in self.images:
                if image.displayNow:
                    image.renderImage()

        pygame.display.update()
        isRunning = True

        while isRunning:

            clock.tick(framerate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False

                # Handle Clicks
                if event.type == pygame.MOUSEBUTTONUP:
                    click = pygame.mouse.get_pos()

                    for button in self.buttons:
                        if button.wasClicked(click):
                            listOfButtons.append(button)
                            # print("Click Det in Menu")
                            if not button.dummy:
                                # return whatever is defined to do onClick
                                if len(listOfButtons) == 0:
                                    return button.handleClick(click)
                                else:
                                    return button.handleClick(click, listOfButtons)
                            else:
                                button.handleClick(click, listOfButtons)
                            break
