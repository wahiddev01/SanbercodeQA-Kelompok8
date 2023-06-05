import unittest
from unittest.suite import TestSuite

import sys
sys.path.append('MainTest/LoginLogout')
sys.path.append('MainTest/AdminUserManagementUsers')
sys.path.append('MainTest/AdminUserManagementUsersEditUser')
sys.path.append('MainTest/AdminUserManagementUsersAddUser')
sys.path.append('MainTest/AdminUserManagementUsersDeleteUser')
sys.path.append('MainTest/PIMDeleteUsers')
from MainTest.LoginLogout import login
from MainTest.AdminUserManagementUsers import users
from MainTest.AdminUserManagementUsersEditUser import editUser
from MainTest.AdminUserManagementUsersAddUser import addUser
from MainTest.AdminUserManagementUsersDeleteUser import deleteUser
from MainTest.PIMDeleteUsers import deleteUsersPim

if __name__ == '__main__':

    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add test to the test suite
    suite.addTests(loader.loadTestsFromModule(login))
    suite.addTests(loader.loadTestsFromModule(users))
    suite.addTests(loader.loadTestsFromModule(addUser))
    suite.addTests(loader.loadTestsFromModule(editUser))
    suite.addTests(loader.loadTestsFromModule(deleteUser))
    suite.addTests(loader.loadTestsFromModule(deleteUsersPim))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)