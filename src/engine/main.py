import pygame


def main():
    print("Welcome to the Mammon Engine!")
    pygame.init()
    mainWindow=pygame.display.set_mode((720,720))
    isRunning = True
    testImg = pygame.image.load("../../data/assets/sprites/testSprite.png")
    mainWindow.fill((0, 0, 255))
    mainWindow.blit(testImg, (0,0))
    pygame.display.update()
    while(isRunning):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
    print("Goodbye")


if(__name__ == "__main__"):
    main()