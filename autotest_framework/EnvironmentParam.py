#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jul 27, 2012
'''

class Parameters():
    def __init__(self):
        self.run_domain = None
        
    def __str__(self):
        return "Run Domain: " + str(self.run_domain)
    
currentParameters = Parameters()

def GetParams(*args):
    return currentParameters