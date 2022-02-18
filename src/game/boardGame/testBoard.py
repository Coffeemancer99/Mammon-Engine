'''
Alternative board style using node objects and positions rather than tiles.

        Authored by Drake Farmer
        2/18/2022
        Pirate Party Game test board file

This test board file works by creating a board class, which contains an array of a linked list structure of the nodes.
By going through these nodes you can travel around the map in order easily without having to scan for nodes.
Speed of searching through nodes entirely depends on where on the map a player is and how the node is being
accessed. Array is static with board save data, so using array index locations as a search key vastly
improves node lookup times. Nodes use x and y positioning for their locations, and include additional attributes
for items, events, multiple pathways, and toggling pathways on and off.


    Node
        Attributes:
                int posX                    ~contains the x position of the node
                int posY                    ~contains the y position of the node
                int nodeType                ~sets what type of node this is
                                                0 = standard node       Node has no additional functionality
                                                1 = money node          Node awards money when landed on
                                                2 = item node           Node gives items when landed on. Calls itemInventory's "getItemRegTileBlock" to give items
                                                3 = event node          Node triggers events when landed on

                array nextNode              ~contains all avaliable nodes for moving forward from this node
                array disNode               ~contains unavaliable progress nodes.
                                                This is used by moving nodes from nextNode to disNode

                array events                ~holds the events which can be triggered by this Node
                                                >>DOUBLE CHECK HOW EVENTS WORK! THIS ARRAY IS A PLACEHOLDER
                                                    Will this work like item functionality?
                                                    Local / boardwide events?
                                                    Will need to do more research into how events will work

        Functions:
                getPos(self)                ~This function returns the x and y position of the node, stylized as "(x,y)"
                getPosX(self)               ~This function returns the x position as an int
                getPosY(self)               ~This function returns the y position as an int
                landedOn(self, player)      ~This function is called when a player lands on the Node
                triggerEvent()              ~This function will trigger the event(s) stored in the events array
                                                >>DOUBLE CHECK HOW EVENTS WORK! THIS FUNCTION IS A PLACEHOLDER
                                                    Multiple events per node or only one event always?

                setPos(int x, int y)        ~Sets the position of the node
                setType(int type)           ~Sets the type of node this is
                addNextNode(int index)      ~adds node at index into nextNode array
                delNextNode(int index)      ~Deletes the node at index from the nextNode array



    Board
        Attributes:
                int boardState              ~A modifiable int for changing board states. WIP ex:
                                                0 = setup
                                                1 = early game
                                                2 = midgame, boss appears
                                                3 = boss defeat
                                                4 = map collapse
                                                    *note* These are placeholder examples of how this might be

                array nodes                 ~This array contains all of the nodes for the board
                array objects               ~This array contains the dynamic objects within the board
                                                >>DOUBLE CHECK IF THIS IS REQUIRED!

                array boardArt              ~Contains a tilemap of the board background art to facilitate with rendering
                                                and zooming in

                array events                ~Contains the events that can occur on this board
                                                >>DOUBLE CHECK HOW EVENTS WORK! THIS ARRAY IS A PLACEHOLDER

        Functions:
                createNode()                ~creates a new node and adds it to the nodes array. Returns array index
                                                of new node

                getNode(int index)          ~returns the node at nodes array index

                deleteNode(int index)       ~deletes the node at nodes array index. Because of how this works this location
                                                in the array remains empty until another node is created, rather than
                                                shifting all other nodes down one space

                triggerEvent(int evIndex)   ~Triggers the event located in the events array at location evIndex


    TO DO:
        -Discuss how events will work, similar to items? Are they called externally or stored within the board?
        -How will we store board save data once we make the board?
        -Make sure that player class can effectively use the node functions correctly
'''
import pygame.sprite
import src.game.boardGame.itemInventory as itemInventory

class Node:
    # Initialize Node
    def __init__(self):
        # Ints
        self.posX = 0           # This int holds the x position of the node
        self.posY = 0           # This int holds the y position of the node
        self.nodeType = 0       # This int determines what type of Node this is
        # Arrays
        self.nextNode = []      # This array holds all nodes the player can travel to next
        self.lastNode = []      # This array holds the node before this one
        self.disNode = []       # This array holds nodes that can be traveled to but are disabled
        self.events = []        # This array might hold node specific events. It is a placeholder

    # The "getPos" returns the x and y positions in a 2 element array
    def getPos(self):
        posArray = [self.posX, self.posY]
        return posArray

    # The "getPosX" function returns the int value of the x position
    def getPosX(self):
        return self.posX

    # The "getPosY" function returns the int value of the y position
    def getPosY(self):
        return self.posY

    # The "landedOn" function is called when a player stops on the node
    def landedOn(self, player):
        pass
        #when landed on, check node type for what to do

    # The "getNextNode" function returns the next node(s). If there is a single node it returns the node itself,
    # while if it has multiple nodes it returns the array containing those nodes
    def getNextNode(self):
        if len(self.nextNode)==1:
            return self.nextNode[1]
        return self.nextNode

    # The "getLastNode" function operates similarly to "getNextNode" but instead returns the previous node(s)
    def getLastNode(self):
        if len(self.lastNode)==1:
            return self.lastNode[1]
        return self.lastNode

    # The "giveItem" function will call itemInventory.py's "getItemRegTileBLock" and return that item
    def giveItem(self):
        item = itemInventory.ItemHandler.getItemRegTileBlock(itemInventory.ItemHandler)
        # Ignore the expected type issue, it is a PyCharm Error
        # Do some checking for the item? Maybe certain items can trigger events when received?
        # Trigger animation or something?
        return item

    # The "giveMoney" function will return a random value, assumed to be used as money.
    def giveMoney(self):
        money = 10
        #include some cool math to figure out money or whatever here
        #trigger animation or something?
        return money



      #Board Class
class Board:
    # Initialize board
    def __init__(self):
        self.boardState = 0     # Boardstate is used to keep track of what state the board is in
        self.nodes = []         # This is an array which will hold the nodes for the board
        self.objects = []       # This is an array which will hold all objects used by the board
        self.boardArt = []      # This is a tilemap array used to hold the board BG artwork
        self.events = []        # This is an array to hold all events used by the map, this is currently a placeholder

    #Initialize Functions
    def createNode(self):
        newNode = Node()
        self.nodes.append(newNode)
        #TO DO
            #-Connect Nodes
            #-Implement Node ID as backup?
            #-Iterate through node or immediatelly append? (check for deleted nodes)
            #-Should we include setup data in the node init?

