#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jan 24, 2013
'''
import unittest
import xmlrunner

class TheTest(unittest.TestCase):

    def testOne(self):
        self.assertEquals(1, 1)
    def testTwo(self):
        self.assertEquals(2, 2)
    def testThree(self):
        self.assertEquals(3, 4)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TheTest)
    xmlrunner.XMLTestRunner().run(suite)