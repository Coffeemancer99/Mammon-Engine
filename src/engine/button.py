import pygame

'''
button.py
Created by: Andrew Bunn
Used to make a button
'''
class Button:

    def __init__(self, x, y, width, height, scale, onClick, imagePath, window, name=None, shouldRet=None):
        """
        :param x: x position of button
        :param y: y position of button
        :param width: width of button
        :param height: height of button
        :param scale: button scale factor
        :param onClick: function to determine what to do when a
                        button is clicked
        :param imagePath: path for the button image
        :param window: window to display button in
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale = scale
        self.onClick = onClick
        self.imagePath = imagePath  # string
        self.window = window
        self.name = name
        self.shouldRet = shouldRet

        # dummy set true when buttons have no functionality
        self.dummy = False



    def handleClick(self, click, listOfButtons=None):
        """
        handles what to do when a click is detected
        :param click: location of click in the window (x,y)
        :return: returns onClick(), typically launches a menu, minigame, or game
        """
        if self.wasClicked(click):
            if len(listOfButtons) != 0:
                return self.onClick(listOfButtons)
            else:
                return self.onClick()



    def renderButton(self):
        """
        loads the button image, scales it, and renders it
        """
        button = pygame.image.load(self.imagePath)
        # scale
        button = pygame.transform.scale(button,
                                     ((button.get_width()) * self.scale,
                                      (button.get_height()) * self.scale))
        self.window.blit(button, (self.x * self.scale, self.y * self.scale))
        pygame.display.update()



    def wasClicked(self, click):
        """
        :param click: location of click in the window (x,y)
        :return: return true if the button was clicked within it's bounds
                 else return false
        """
        if (click[0] > self.x * self.scale) and (click[0] <= (self.x + self.width) * self.scale):  # x
            if (click[1] > self.y * self.scale) and (click[1] <= (self.y + self.height) * self.scale):  # y
                return True
        return False

