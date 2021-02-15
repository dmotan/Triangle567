# -*- coding: utf-8 -*-
"""
Updated Feb 14, 2021
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Diaeddin Motan
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testNotTriangles(self):
        # Test with value <= 0
        self.assertEqual(classifyTriangle(0,3,4),'InvalidInput','0,3,4 is InvalidInput')
        # Test with value >= 200
        self.assertEqual(classifyTriangle(10,300,4),'InvalidInput','10,300,4 is InvalidInput')
        # Test with non-integer values
        self.assertEqual(classifyTriangle(10.2,300,4),'InvalidInput','10.2,300,4 is InvalidInput')
        # Test with values that cannot form a triangle (c > a + b)
        self.assertEqual(classifyTriangle(1,2,4),'InvalidInput','10.2,300,4 is InvalidInput')

    def testRightTriangles(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertNotEqual(classifyTriangle(5,5,4),'Right','5,5,4 is not a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is a Equilateral triangle')
        self.assertEqual(classifyTriangle(4,4,4),'Equilateral','4,4,4 is a Equilateral triangle')
        self.assertNotEqual(classifyTriangle(5,4,4),'Equilateral','5,4,4 is not a Equilateral triangle')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5,6,7),'Scalene','5,6,7 is a Scalene triangle')
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 is a Scalene triangle')
        self.assertNotEqual(classifyTriangle(5,4,4),'Scalene','5,4,4 is not a Scalene triangle')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,2,2 should be Isoceles')
        self.assertEqual(classifyTriangle(4,4,6),'Isoceles','4,4,6 should be Isoceles')
        self.assertNotEqual(classifyTriangle(4,3,6),'Isoceles','4,3,6 should not be Isoceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

