#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jun 15, 2012
'''
import SauceParams
import os

tp = SauceParams.GetParams()

config={
        'username' : os.environ.get('SAUCE_USER_NAME'),
        'access-key' : os.environ.get('SAUCE_API_KEY'), 
        'host' : os.environ.get('SELENIUM_HOST'),
        'port' : os.environ.get('SELENIUM_PORT'),
        'base-url' : os.environ.get('SELENIUM_STARTING_URL'),

        'platforms' :   [{
                         "os": os.environ.get('SELENIUM_PLATFORM'),
                         "browser": os.environ.get('SELENIUM_BROWSER'),
                         "browser-version": os.environ.get('SELENIUM_VERSION')
                         }
                         ]
        }