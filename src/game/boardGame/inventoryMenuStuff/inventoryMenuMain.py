import pygame

from src.engine.andrewMenus.image import Image
from src.game.boardGame.boardPlayers import BoardPlayer
from src.game.boardGame.inventoryMenuStuff.inventoryMenu import InventoryMenu
from src.engine.button import Button
from src.game.boardGame.inventoryMenuStuff.itemUseMenuFunctions import *
from src.game.boardGame.itemInventory import *
from src.game.boardGame.inventoryMenuStuff.inventoryMenuCreatorFunctions import *


# def makeAllImages(mainWindow, scale, currentPlayer):
#     # Did not have some handling needed in BoardPlayer
#     # for handling if inventory is empty or missing items,
#     # so did this
#     inventory = currentPlayer.getInventory()
#     invBoolList = getInvBoolList(inventory)
#
#     images = []
#
#     # x and y for 64x64 img
#     x = 384
#     # y = 176
#     y = 48
#     width = 64
#     height = 64
#
#     defaultImg = Image(352, 16, 128, 128, scale, "data/assets/sprites/128square.png",
#                        mainWindow, True)
#     images.append(defaultImg)
#
#     if invBoolList[0]:
#         item1Img = inventory[0].getButtonImage()
#         item1Image = Image(x, y, width, height,
#                            scale, "data/assets/sprites/" + item1Img, mainWindow, False)
#         images.append(item1Image)
#
#     if invBoolList[1]:
#         item2Img = inventory[1].getButtonImage()
#         item2Image = Image(x, y, width, height,
#                            scale, "data/assets/sprites/" + item2Img, mainWindow, False)
#         images.append(item2Image)
#
#     if invBoolList[2]:
#         item3Img = inventory[2].getButtonImage()
#         item3Image = Image(x, y, width, height,
#                            scale, "data/assets/sprites/" + item3Img, mainWindow, False)
#         images.append(item3Image)
#
#     if invBoolList[3]:
#         item4Img = inventory[3].getButtonImage()
#         item4Image = Image(x, y, width, height,
#                            scale, "data/assets/sprites/" + item4Img, mainWindow, False)
#         images.append(item4Image)
#
#     return images
#
#
# def getInvBoolList(inventory):
#     invBoolList = [False, False, False, False]
#     for i in range(len(inventory)):
#         invBoolList[i] = True
#     return invBoolList
#
#
# def makeAllButtons(mainWindow, framerate, scale, currentPlayer, itemImages, listOfPlayers):
#     curPlayerInv = currentPlayer.getInventory()
#     invBoolList = getInvBoolList(curPlayerInv)
#     print(invBoolList)
#
#     # On Click Functions for buttons
#     def onClickBackButton(listOfButtons=None):
#         # return mainmenu.launch(width, height, framerate, scale)
#         print("Back not hooked up RESET DUMMY WHEN WE DO")
#
#     def onClickUseButton(listOfButtons=None):
#         # Will need list of buttons, check prev for item existing
#         # If exist, check type, start menu accordingly if bad item
#         if (listOfButtons is not None):
#             if len(listOfButtons) > 1:
#                 if (("item" in listOfButtons[-2].name) and listOfButtons[-1].name == "use" and listOfButtons[
#                     -2].shouldRet):
#                     print("CAN USE")
#                     curItemButton = listOfButtons[-2]
#                     if curItemButton.name == "item1":
#                         if curPlayerInv[0].affectsSecondPlayer():
#                             # Make the images
#                             itemImages = makeAllUseMenuImages(mainWindow, scale, currentPlayer, listOfPlayers)
#
#                             # Make the buttons
#                             invMenuButtons = makeAllUseMenuButtons(mainWindow, framerate, scale,
#                                                                    currentPlayer, images=itemImages)
#
#                             # Make the menu
#                             useMenu = InventoryMenu("Use Item On Who?", buttons=invMenuButtons, images=itemImages,
#                                                     currentPlayer=currentPlayer, listOfPlayers=listOfPlayers)
#                             # Launch the menu
#                             useMenu.launchInv(mainWindow, framerate)
#
#                 else:
#                     print("Use unhooked (button list > 1)")
#             else:
#                 print("Use unhooked")
#
#     def onClickItem1Button(listOfButtons=None):
#         print("Item 1")
#         if invBoolList[0]:
#             itemImages[1].renderImage()
#         else:
#
#             itemImages[0].renderImage()
#
#     def onClickItem2Button(listOfButtons=None):
#         print("Item 2")
#         if invBoolList[1]:
#             itemImages[2].renderImage()
#         else:
#             # render default image
#             itemImages[0].renderImage()
#
#     def onClickItem3Button(listOfButtons=None):
#         print("Item 3")
#         if invBoolList[2]:
#             itemImages[3].renderImage()
#         else:
#             # render default image
#             itemImages[0].renderImage()
#
#     def onClickItem4Button(listOfButtons=None):
#         print("Item 4")
#         if invBoolList[3]:
#             itemImages[4].renderImage()
#         else:
#             # render default image
#             itemImages[0].renderImage()
#
#     # Create Buttons
#     backButton = Button(4, 412, 96, 32, scale, onClickBackButton,
#                         "data/assets/sprites/backMenuButton.png", mainWindow, "back")
#     backButton.dummy = True
#
#     useItemButton = Button(412, 412, 96, 32, scale, onClickUseButton,
#                            "data/assets/sprites/useButton.png", mainWindow, "use")
#     useItemButton.dummy = True
#
#     item1Button = Button(4, 6, 320, 96, scale, onClickItem1Button,
#                          "data/assets/sprites/inventoryItemButton.png",
#                          mainWindow, "item1", shouldRet=invBoolList[0])
#     item1Button.dummy = True
#
#     item2Button = Button(4, 108, 320, 96, scale, onClickItem2Button,
#                          "data/assets/sprites/inventoryItemButton.png",
#                          mainWindow, "item2", shouldRet=invBoolList[1])
#     item2Button.dummy = True
#
#     item3Button = Button(4, 210, 320, 96, scale, onClickItem3Button,
#                          "data/assets/sprites/inventoryItemButton.png",
#                          mainWindow, "item3", shouldRet=invBoolList[2])
#     item3Button.dummy = True
#
#     item4Button = Button(4, 312, 320, 96, scale, onClickItem4Button,
#                          "data/assets/sprites/inventoryItemButton.png",
#                          mainWindow, "item4", shouldRet=invBoolList[3])
#     item4Button.dummy = True
#
#     # return all buttons in a list
#     return [backButton, useItemButton, item1Button, item2Button, item3Button, item4Button]


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
