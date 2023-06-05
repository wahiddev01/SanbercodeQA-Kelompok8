import unittest
from unittest.suite import TestSuite

import sys
sys.path.append('MainTest/PIMEmployeeListAddEmployee')

#import dari dalam folder MainTest, file EmployeeList.py dengan nama class EmployeeListPIM
from MainTest.PIMEmployeeListAddEmployee.EmployeeList import EmployeeListPIM
#import dari dalam folder MainTest, file AddEmployee.py dengan nama class TestPIMAdd
from MainTest.PIMEmployeeListAddEmployee.AddEmployee import TestPIMAdd

if __name__ == '__main__':

    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add test to the test suite
    suite.addTests(loader.loadTestsFromTestCase(EmployeeListPIM)) #nama class didalam file py
    suite.addTests(loader.loadTestsFromTestCase(TestPIMAdd)) #nama class didalam file py

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)