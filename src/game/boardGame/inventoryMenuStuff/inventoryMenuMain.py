from src.game.boardGame.inventoryMenuStuff.inventoryMenuCreatorFunctions import *

def main():
    pygame.init()
    mainWindow = pygame.display.set_mode((512, 448))
    framerate = 60
    scale = 1

    launchInventoryMenu(mainWindow, framerate, scale)


def launchInventoryMenu(mainWindow, framerate, scale):
    # Later, pass these items in
    p1 = BoardPlayer(1)
    p2 = BoardPlayer(2)
    p3 = BoardPlayer(3)
    p4 = BoardPlayer(4)
    currentPlayer = p1
    listOfPlayers = [p1, p2, p3, p4]
    p1.setInventory(StealItem())
    p1.setInventory(InvertedControlsItem())
    p2.setInventory(InvertedControlsItem())

    # Make the images
    itemImages = makeAllImages(mainWindow, scale, currentPlayer)

    # Make the buttons
    invMenuButtons = makeAllButtons(mainWindow, framerate, scale, currentPlayer, itemImages, listOfPlayers)

    # Make the menu
    inventoryScreen = InventoryMenu("Inventory", buttons=invMenuButtons, images=itemImages,
                                    currentPlayer=currentPlayer, listOfPlayers=listOfPlayers)
    # Launch the menu
    inventoryScreen.launchInv(mainWindow, framerate)


if __name__ == "__main__":
    main()
