#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jul 11, 2012
'''
class SauceParams():
    def __init__(self):
        self.run_domain = None
        
    def __str__(self):
        return str(self.run_domain)
    
currentParameters = SauceParams()

def GetParams(*args):
    return currentParameters