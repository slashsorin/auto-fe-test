#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jan 15, 2013
'''

from selenium import selenium
import Parameters as tParams
import Constants as ct

def setUp(self):
    self.verificationErrors = []
    self.selenium = selenium("localhost", 4445, "*firefoxproxy", "http://localhost/JavaScriptClock.html")
    self.selenium.start()
        
def test_js_errors(self):
    