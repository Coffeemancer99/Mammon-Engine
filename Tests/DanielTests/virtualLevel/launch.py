from Tests.DanielTests.virtualLevel.virtual import *

def startGame(mainWindow = None, scale = 1, framerate = 60):
    print("\nlaunch.startGame taking off!\n")
    results = testImpact()
    print("\nresults = {}".format(results))
    assert results
    return results