import pygame
from src.engine.andrewMenus.menu import Menu


class InventoryMenu(Menu):
    def __init__(self, title, buttons, currentPlayer, listOfPlayers, images=None, scaleFactors=None):
        super().__init__(title, buttons, images, scaleFactors)
        # Now menu as it originally is, is initiallized
        # Can add more functionality from here, using the additional params
