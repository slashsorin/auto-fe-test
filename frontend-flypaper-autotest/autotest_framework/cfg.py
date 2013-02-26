#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jun 15, 2012
'''
import SauceParams

tp = SauceParams.GetParams()
'''
config={
        'username' : os.environ.get('SAUCE_USER_NAME'), #"issuu",
        'access-key' : os.environ.get('SAUCE_API_KEY'), #"23a5b32a-6ab8-4866-8f1d-9a13c98348c2",
        'host' : os.environ.get('SELENIUM_HOST'), #"ondemand.saucelabs.com",
        'port' : os.environ.get('SELENIUM_PORT'), #4444,
        'base-url' : os.environ.get('SELENIUM_DOMAIN'),

        'platforms' :   [{
                         "os": os.environ.get('SELENIUM_PLATFORM'),
                         "browser": os.environ.get('SELENIUM_BROWSER'),
                         "browser-version": os.environ.get('SELENIUM_VERSION')
                         }
                         ]
        }
'''
config={
        'username' : "issuu",
        'access-key' : "23a5b32a-6ab8-4866-8f1d-9a13c98348c2",
        'host' : "ondemand.saucelabs.com",
        'port' : 4444,
        'base-url' : "adpages-uat.issuu.com",
        'platforms' :   [{
                         "os": "Mac 10.6",
                         "browser": "firefox",
                         "browser-version": "19"
                         }]
        }