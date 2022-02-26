import node as node
import random
import graph as graph
def main():

    n1 = node.node(5, 0)
    n2 = node.node(8, 1)

    n1.addNeighbor(n2, 3)

    randInt = random.randrange(0,11)
    print(randInt)

    for n in n1.neighbors:
        print(n)

if __name__ == "__main__":
    main()