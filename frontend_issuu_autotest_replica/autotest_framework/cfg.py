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
        'username' : "issuu",
        'access-key' : "23a5b32a-6ab8-4866-8f1d-9a13c98348c2",
        'host' : "ondemand.saucelabs.com",
        'port' : 4444,
        'base-url' : os.getenv('SELENIUM_DOMAIN', 'https://flypaper.issuu.com'),
        'session_timeout' : int(os.getenv('SELENIUM_SESSION_TIMEOUT', '90000')),
        'video-upload-on-pass': False,
        #need to check that the idle-timeout works !!!
        'idle-timeout'    : 300,     # seconds, default is 90
        'max-duration'    : 1800,    # seconds, default is 1800 ~ 30 min.
        'command-timeout' : 300,     # seconds, default is 300

        'platforms' :  [#{"os": "Windows 2003", "browser": "iexplore", "browser-version": "8", "avoid-proxy": True},
						#{"os": "Windows 2008", "browser": "iexplore", "browser-version": "8"},
						{"os": "Windows 2008", "browser": "iexplore", "browser-version": "9."},
						{"os": "Windows 2003", "browser": "firefox", "browser-version": "13.", "avoid-proxy": True},
						#{"os": "Windows 2008", "browser": "firefox", "browser-version": "11"},
						#{"os": "Windows 2012", "browser": "firefox", "browser-version": "11"},
						#{"os": "Windows 2003", "browser": "safari", "browser-version": "5", "avoid-proxy": True},
						#{"os": "Windows 2008", "browser": "safari", "browser-version": "5"},
						#{"os": "Windows 2003", "browser": "googlechrome", "browser-version": "", "avoid-proxy": True},
						{"os": "Windows 2008", "browser": "googlechrome", "browser-version": ""}
						#{"os": "Mac 10.8", "browser": "googlechrome", "browser-version": ""},
						#{"os": "Mac 10.6", "browser": "googlechrome", "browser-version": "", "avoid-proxy": True},
						#{"os": "Mac 10.6", "browser": "firefox", "browser-version": "11", "avoid-proxy": True},
						#{"os": "Mac 10.6", "browser": "safari", "browser-version": "5", "avoid-proxy": True},
						#{"os": "Mac 10.8", "browser": "safari", "browser-version": "6."}
						#{"os": "Linux", "browser": "firefox", "browser-version": "11", "avoid-proxy": True}
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

