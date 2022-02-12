import pygame
import networkx as nx

class Tile:

    # next will be a list, as paths may split
    def __init__(self, name, prev, next, tileType, playersHere):
        self.name = name
        self.prev = prev
        self.next = next
        self.tileType = tileType
        self.playersHere = playersHere

        # need function to check tileType and call appropriate functions

        '''
        Need flags
        - isMoney
        - isMinigame
        - isShop
        - isItem
        - isSecretBonus
        '''
    def __repr__(self):
        return self.name