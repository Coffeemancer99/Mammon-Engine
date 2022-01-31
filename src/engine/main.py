import pygame

def main():
    print("Welcome to the Mammon Engine!")
    pygame.init()
    mainWindow=pygame.display.set_mode((720,720)) #Main window for pygame display
    isRunning = True
    while(isRunning):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning=False
    print("Goodbye")


if(__name__ == "__main__"):
    main()