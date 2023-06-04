import unittest
from unittest.suite import TestSuite

import sys
sys.path.append('MainTest/AdminOrganizationAddLocation')
sys.path.append('MainTest/AdminOrganizationEditLocation')
sys.path.append('MainTest/AdminOrganizationDeleteLocation')


from MainTest.AdminOrganizationAddLocation import addLocation
from MainTest.AdminOrganizationEditLocation import editLocation
from MainTest.AdminOrganizationDeleteLocation import deleteLocation


if __name__ == '__main__':

    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add test to the test suite
    suite.addTests(loader.loadTestsFromModule(addLocation))
    suite.addTests(loader.loadTestsFromModule(editLocation))
    suite.addTests(loader.loadTestsFromModule(deleteLocation))
    
    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)