import pygame


class Button:



    def __init__(self, x, y, width, height, scale, onClick, imagePath, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale = scale
        self.onClick = onClick
        self.imagePath = imagePath # string
        self.window = window
        self.dummy = False

    def handleClick(self, click):
        if(self.wasClicked(click)):
            return self.onClick()

    def renderButton(self):
        button = pygame.image.load(self.imagePath)
        # scale
        button = pygame.transform.scale(button,
                                     ((button.get_width()) * self.scale,
                                      (button.get_height()) * self.scale))
        self.window.blit(button, (self.x * self.scale, self.y * self.scale))
        pygame.display.update()

    def wasClicked(self, click):
        if((click[0] > self.x * self.scale) and (click[0] <= (self.x + self.width) * self.scale)):  # x
            if ((click[1] > self.y * self.scale) and (click[1] <= (self.y + self.height) * self.scale)):  # y
                return True

        return False

