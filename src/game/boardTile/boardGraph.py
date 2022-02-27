import networkx as nx
import src.game.boardTile.tile as tile

'''
boardGraph.py created by Andrew Bunn
BoardGraph class implemented by Andrew Bunn
'''

'''
BoardGraph will deal with creating the game board used on startup
Board will be hardcoded for now
== Add random generation == 
'''
class BoardGraph:

    def __init__(self):
        pass

    def generateBoard(self):
        # instantiate a directed graph
        board = nx.DiGraph()
        tileList = []

        oneEffingTile = tile.Tile("PLZ", None, None, None, [False, False, False, False])

        # generate all the tiles and stuff into a list
        for i in range(1,11):
            if(i == 1):
                startTile = tile.Tile("Start", None, None, None, [False, False, False, False])
                tileList.append(startTile)

            else:
                otherTile = tile.Tile(str(i), None, None, None, [False, False, False, False])
                tileList.append(otherTile)

        # add the tiles as nodes
        for i in range(len(tileList)):
            board.add_node(i, data = tileList[i])

        print("========= TILE LIST ========")
        for i in range(len(tileList)):
            print(tileList[i])
        print("========= TILE LIST END ========")


    #     boardTile = tile.Tile(None, None, None, None, [False, False, False, False])

       # instantiate a directed graph
    #     board = nx.DiGraph()
    #
    #
    #     tileList = []
    # #   generate all the tiles and stuff into a list
    #     for i in range(1,11):
    #         if(i == 1):
    #             tileList.append(tile.Tile("Start", None, None, None, [False, False, False, False]))
    #         else:
    #             tileList.append(tile.Tile(i, None, None, None, [False, False, False, False]))
    #
    #     # add the nodes
    #     board.add_node("Start")
    #     for i in range (2, 10):
    #         board.add_node(i, tileList[i])
    #
    #     # add the tiles
    #
    #     # Create the paths
    #     board.add_edges_from([("Start", 2), (2, 3),
    #                           (3, 4), (3, 5)])

        return board
