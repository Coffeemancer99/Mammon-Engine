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
                                                1 = item node           Node gives items when landed on. Calls itemInventory's "getItemRegTileBlock" to give items
                                                2 = event node          Node triggers events when landed on

                array nextNode              ~contains all avaliable nodes for moving forward from this node
                array disNode               ~contains unavaliable progress nodes.
                                                This is used by moving nodes from nextNode to disNode

                array events                ~holds the events which can be triggered by this Node
                                                >>DOUBLE CHECK HOW EVENTS WORK! THIS ARRAY IS A PLACEHOLDER
                                                    Will this work like item functionality?

        Functions:
                getPos(self)                ~This function returns the x and y position of the node, stylized as "(x,y)"
                getPosX(self)               ~This function returns the x position as an int
                getPosY(self)               ~This function returns the y position as an int
                landedOn(self, player)      ~This function is called when a player lands on the Node
                triggerEvent(



'''