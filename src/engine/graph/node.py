class node():
    def __init__(self, value, nID):
        self.value = value
        self.neighbors = []
        self.edges = []
        self.nID = nID
        self.start = 0 #If it is the starting node
        self.end = 0 #If it is the ending node

    def addNeighbor(self, neighbor, edge):
        self.neighbors.append(neighbor)
        self.edges.append(edge)

    def __repr__(self):
        return (str(self.value))
