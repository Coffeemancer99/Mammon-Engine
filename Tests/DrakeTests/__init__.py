import Tests.DrakeTests.DrakeTests as testModule
import unittest

def load_tests(loader, standard_tests, pattern = "test*.py"):
    suite = unittest.TestSuite()
    tests = loader.loadTestsFromModule(testModule)
    suite.addTests(tests)
    return suite