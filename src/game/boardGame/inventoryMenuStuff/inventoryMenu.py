import pygame
from src.engine.andrewMenus.menu import Menu


class InventoryMenu(Menu):
    def __init__(self, title, buttons, currentPlayer, listOfPlayers, images=[], scaleFactors=None):
        super().__init__(title, buttons, images, scaleFactors)
        self.displayThing = []
        # Now menu as it originally is, is initiallized
        # Can add more functionality from here, using the additional params

    # Only difference here is that we don't pygame.display.update() in
    # render functions, only do in main loop. Allowed less images to be
    # created in itemUseMenu
    def launchInv(self, mainWindow, framerate):
        clock = pygame.time.Clock()
        listOfButtons = []
        isRunning = True
        listOfImagesCopy = self.images.copy()

        while isRunning:
            # Paint screen background grey
            mainWindow.fill((55, 55, 55))

            for button in self.buttons:
                button.renderButtonNoUpdate()

            if self.images is not None:
                for image in self.images:
                    if image.displayNow:
                        image.renderImageNoUpdate()

            if len(listOfImagesCopy) > 0:
                for image in listOfImagesCopy:
                    if image.renderThis:
                        image.renderImageNoUpdate()

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
                                if len(listOfButtons) == 0 and len(listOfImagesCopy) > 0:
                                    return button.handleClick(click, listOfImages=listOfImagesCopy)
                                elif len(listOfButtons) > 0 and len(self.images) > 0:
                                    return button.handleClick(click, listOfButtons, listOfImages=listOfImagesCopy)
                                elif len(listOfButtons) > 0 and len(listOfImagesCopy) == 0:
                                    return button.handleClick(click, listOfButtons)
                                else:
                                    return button.handleClick()
                            else:
                                if len(listOfButtons) == 0 and len(listOfImagesCopy) > 0:
                                    button.handleClick(click, listOfImages=listOfImagesCopy)
                                elif len(listOfButtons) > 0 and len(listOfImagesCopy) > 0:
                                    button.handleClick(click, listOfButtons, listOfImages=listOfImagesCopy)
                                elif len(listOfButtons) > 0 and len(listOfImagesCopy) == 0:
                                    button.handleClick(click, listOfButtons)
                                else:
                                    button.handleClick()
                                # button.handleClick(click, listOfButtons)
                            break

            pygame.display.update()
