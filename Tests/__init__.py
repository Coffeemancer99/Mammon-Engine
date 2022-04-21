import os
def load_tests(loader, standard_tests, pattern = "test*.py"):
    print("testRunner: Loading from " + os.getcwd() + "/Tests/")
    testSuite = loader.discover(start_dir=os.getcwd() + "/Tests/")
    return testSuite