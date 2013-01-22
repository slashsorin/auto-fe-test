#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jun 15, 2012
'''

import SauceParams
import os

try:
    import json
except ImportError:
    import simplejson as json

tp = SauceParams.GetParams()


config={
        'username' : os.environ.get('SAUCE_USER_NAME'),
        'access-key' : os.environ.get('SAUCE_API_KEY'), 
        'host' : os.environ.get('SELENIUM_HOST'),
        'port' : os.environ.get('SELENIUM_PORT'),
        'base-url' : os.environ.get('SELENIUM_STARTING_URL', 'issuu.com'),

        'session_timeout' : int(os.getenv('SELENIUM_SESSION_TIMEOUT', '90000')),
        'video-upload-on-pass': False,
        #need to check that the idle-timeout works !!!
        'idle-timeout' : 300, # seconds, default is 90
        'max-duration' : 1800, # seconds, default is 1800 ~ 30 min.
        'command-timeout' : 300, # seconds, default is 300

        'platforms' :   [{
                         "os": os.environ.get('SELENIUM_PLATFORM'),
                         "browser": os.environ.get('SELENIUM_BROWSER'),
                         "browser-version": os.environ.get('SELENIUM_VERSION')
                         }
                         ]
        }

# merge configuration using env var.
try:
	f = open(os.getenv('AUTOTEST_CONFIG'))
	c = json.load(f)
	for k in c:
		config[k] = c[k]
except Exception, err:
	print 'Failed to parse and merge json config file: ', err
	pass