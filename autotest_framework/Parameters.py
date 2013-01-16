#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps May 3, 2012
'''

class Parameters():
    def __init__(self):
        self.test_browser = None
        self.run_domain = None
        self.place = None
        
    def __str__(self):
        return "Test browser: " + self.test_browser + " Run Domain: " + str(self.run_domain) + " Place to run: " + str(self.place)
    
currentParameters = Parameters()

def GetParams(*args):
    return currentParameters