import pygame

from src.engine.andrewMenus.image import Image
from src.game.boardGame.boardPlayers import BoardPlayer
from src.game.boardGame.inventoryMenuStuff.inventoryMenu import InventoryMenu
from src.engine.button import Button
from src.game.boardGame.itemInventory import *


def makeAllUseMenuImages(mainWindow, scale, currentPlayer, playerList):
    p1Check = Image(12, 192, 96, 96, scale, "data/assets/sprites/checkMark96.png",
                    mainWindow, True)
    images = [p1Check]
    return images


def makeAllUseMenuButtons(mainWindow, framerate, scale, currentPlayer, listOfPlayers, images=None,
                          curPlayerItemIndex=None):

    curPlayerInv = currentPlayer.getInventory()

    def onClickBackButton(listOfButtons=None, listOfImages=None):
        print("USE MENU Back")
        return

    def onClickUseButton(listOfButtons=None, listOfImages=None):
        # players are not in order in list... ordered on who goes first
        # extract the players so items can be used on them
        player1, player2, player3, player4 = getPlayers()

        if (listOfButtons is not None):
            if len(listOfButtons) > 1:
                if listOfButtons[-2].name == "p1" and listOfButtons[-1].name == "use":
                    # Wanted to refactor to make a function of each of these nested if's
                    # but because of the potential return, it would mess things up.
                    # I felt that it would be messier to add a flag and return accordingly
                    if not curPlayerInv[curPlayerItemIndex].getFunctionality(currentPlayer,
                                                                             player1):
                        print("Cannot Use Item, same item already used")
                    else:
                        currentPlayer.getInventory().pop(curPlayerItemIndex)
                        return
                elif listOfButtons[-2].name == "p2" and listOfButtons[-1].name == "use":
                    # should i pass to this menu and its functions the inventory index
                    if not curPlayerInv[curPlayerItemIndex].getFunctionality(currentPlayer,
                                                                             player2):
                        print("Cannot Use Item, same item already used")
                    else:
                        currentPlayer.getInventory().pop(curPlayerItemIndex)
                        return
                elif listOfButtons[-2].name == "p3" and listOfButtons[-1].name == "use":
                    # should i pass to this menu and its functions the inventory index
                    if not curPlayerInv[curPlayerItemIndex].getFunctionality(currentPlayer,
                                                                             player3):
                        print("Cannot Use Item, same item already used")
                    else:
                        currentPlayer.getInventory().pop(curPlayerItemIndex)
                        return
                elif listOfButtons[-2].name == "p4" and listOfButtons[-1].name == "use":
                    # should i pass to this menu and its functions the inventory index
                    if not curPlayerInv[curPlayerItemIndex].getFunctionality(currentPlayer,
                                                                             player4):
                        print("Cannot Use Item, same item already used")
                    else:
                        currentPlayer.getInventory().pop(curPlayerItemIndex)
                        return

    def getPlayers():
        player1 = list((filter(lambda x: x.getPlayerID() == 1, listOfPlayers)))[0]
        player2 = list((filter(lambda x: x.getPlayerID() == 2, listOfPlayers)))[0]
        player3 = list((filter(lambda x: x.getPlayerID() == 3, listOfPlayers)))[0]
        player4 = list((filter(lambda x: x.getPlayerID() == 4, listOfPlayers)))[0]
        return player1, player2, player3, player4

    def changeXAndRender(x):
        """
        This function renders the image in images[0] at the
        specified x position
        :param x: value to change x position of image to
        """
        images[0].x = x
        images[0].renderImage()

    def onClickP1Button(listOfButtons=None, listOfImages=None):
        print("P1 Chosen")
        changeXAndRender(12)
        # change selected pid in data object (assume we need something to transfer data
        # between menus and game)

    def onClickP2Button(listOfButtons=None, listOfImages=None):
        print("P2 Chosen")
        changeXAndRender(140)

    def onClickP3Button(listOfButtons=None, listOfImages=None):
        print("P3 Chosen")
        changeXAndRender(268)

    def onClickP4Button(listOfButtons=None, listOfImages=None):
        print("P4 Chosen")
        changeXAndRender(396)

    width = 96
    height = 96

    # Create Buttons
    backButton = Button(4, 412, width, 32, scale, onClickBackButton,
                        "data/assets/sprites/newBackButton.png", mainWindow, "back")

    acceptButton = Button(412, 412, width, 32, scale, onClickUseButton,
                          "data/assets/sprites/newUseButton.png", mainWindow, "use")
    acceptButton.dummy = True

    p1Button = Button(12, 288, width, height, scale, onClickP1Button,
                      "data/assets/sprites/bigTestPlayer1.png", mainWindow, "p1")
    p1Button.dummy = True
    p2Button = Button(140, 288, width, height, scale, onClickP2Button,
                      "data/assets/sprites/bigTestPlayer2.png", mainWindow, "p2")
    p2Button.dummy = True
    p3Button = Button(268, 288, width, height, scale, onClickP3Button,
                      "data/assets/sprites/bigTestPlayer3.png", mainWindow, "p3")
    p3Button.dummy = True
    p4Button = Button(396, 288, width, height, scale, onClickP4Button,
                      "data/assets/sprites/bigTestPlayer4.png", mainWindow, "p4")
    p4Button.dummy = True

    return [p1Button, p2Button, p3Button, p4Button, backButton, acceptButton]


def launchUseMenu(mainWindow, framerate, scale):
    p1 = BoardPlayer(1)
    p2 = BoardPlayer(2)
    p3 = BoardPlayer(3)
    p4 = BoardPlayer(4)
    currentPlayer = p1
    listOfPlayers = [p1, p2, p3, p4]
    p1.setInventory(InvertedControlsItem())
    p1.setInventory(InvertedControlsItem())

    # Make the images
    itemImages = makeAllUseMenuImages(mainWindow, scale, currentPlayer, listOfPlayers)

    # Make the buttons
    invMenuButtons = makeAllUseMenuButtons(mainWindow, framerate, scale,
                                           currentPlayer, listOfPlayers, images=itemImages)

    # Make the menu
    useMenu = InventoryMenu("Use Item On Who?", buttons=invMenuButtons, images=itemImages,
                            currentPlayer=currentPlayer, listOfPlayers=listOfPlayers)
    # Launch the menu
    useMenu.launchInv(mainWindow, framerate)


def main():
    pygame.init()
    mainWindow = pygame.display.set_mode((512, 448))
    framerate = 60
    scale = 1
    launchUseMenu(mainWindow, framerate, scale)


if __name__ == "__main__":
    main()
