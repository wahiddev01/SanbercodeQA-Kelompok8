import unittest
from unittest.suite import TestSuite

import sys
sys.path.append('MainTest/LoginLogout')
from MainTest.LoginLogout import login


if __name__ == '__main__':

    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add test to the test suite
    # suite.addTests(loader.loadTestsFromModule(First_Test))
    # suite.addTests(loader.loadTestsFromModule(cart))
    suite.addTests(loader.loadTestsFromModule(login))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)