#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jun 15, 2012
'''
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
'''

import SauceParams
import os

try:
    import json
except ImportError:
    import simplejson as json

tp = SauceParams.GetParams()


config={
        'username' : "issuu",
        'access-key' : "23a5b32a-6ab8-4866-8f1d-9a13c98348c2",
        'host' : "ondemand.saucelabs.com",
        'port' : 4444,
        'base-url' : os.getenv('SELENIUM_DOMAIN', 'issuu.com'),
        'session_timeout' : int(os.getenv('SELENIUM_SESSION_TIMEOUT', '90000')),
        'video-upload-on-pass': False,
        #need to check that the idle-timeout works !!!
        'idle-timeout' : 300, # seconds, default is 90
        'max-duration' : 1800, # seconds, default is 1800 ~ 30 min.
        'command-timeout' : 300, # seconds, default is 300

        'platforms' : [{"os": "Windows 2008", "browser": "firefox", "browser-version": "13.", "avoid-proxy": True},
                        #{"os": "Windows 2008", "browser": "googlechrome", "browser-version": ""},
                        #{"os": "Windows 2008", "browser": "iexplore", "browser-version": "9."},
                        #{"os": "Windows 2003", "browser": "safariproxy", "browser-version": "5."},
                        #{"os": "Windows 2003", "browser": "googlechrome", "browser-version": ""},
                        #{"os": "Linux", "browser": "firefox", "browser-version": "9."}#,
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

