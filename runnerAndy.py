import unittest
import sys
sys.path.append('MainTest/LoginLogout')
sys.path.append('MainTest/AdminUserManagementUsersEditUser')
sys.path.append('MainTest/AdminUserManagementUsersDeleteUser')
sys.path.append('MainTest/AdminOrganization')

from MainTest.AdminUserManagementUsersEditUser import editUserAndy
from MainTest.AdminUserManagementUsersDeleteUser import deleteUserAndy
from MainTest.AdminOrganization import organization

if __name__ == '__main__':

    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add test to the test suite
    suite.addTests(loader.loadTestsFromModule(editUserAndy))
    suite.addTests(loader.loadTestsFromModule(deleteUserAndy))
    suite.addTests(loader.loadTestsFromModule(organization))
    
    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)