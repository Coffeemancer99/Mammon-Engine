import unittest
import os
if __name__ == "__main__":
    loader = unittest.TestLoader()
    print("\ttestRunner:Loading from " + os.getcwd() + "/Tests/")
    testSuite = loader.discover(start_dir= os.getcwd() + "/Tests/")
    print(testSuite)
    runner = unittest.TextTestRunner()
    print(runner.run(testSuite))
