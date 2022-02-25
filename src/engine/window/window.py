import pygame

class window():
    def __init__(self, width, height, scale):
        self.window = pygame.display.set_mode((width, height))
        self.scale = scale
        self.width = width
        self.height = height

    #Scales window by a specified amount
    def scaleWindow(self, scale):
        self.scale = scale #Update scale
        self.window = pygame.display.set_mode((self.width*scale, self.height*scale)) #Update window

    def renderSprites(self, actors):
        list(map(lambda x: self.window.blit(x.sprite, (x.rect.x, x.rect.y)), actors))  # Draw players/tiles/UI

class fourPlayerWindow(window):
    def __init__(self, width, height, scale):
        super().__init__(width, height, scale)
        # "Cameras" aka spicy box colliders to segment each player's window
        self.p1Camera = pygame.Rect(0, 0, width/2, height/2)
        self.p2Camera = pygame.Rect(width/2, 0, width/2, height/2)
        self.p3Camera = pygame.Rect(0, height/2, width/2, height/2)
        self.p4Camera = pygame.Rect(width/2, height/2, width/2, height/2)
        self.cameras = [self.p1Camera, self.p2Camera, self.p3Camera, self.p4Camera]


