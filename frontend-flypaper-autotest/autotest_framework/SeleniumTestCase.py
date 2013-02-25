#-*- coding: utf-8 -*-
'''

    @author: Sorin

    Copyright Issuu Aps Jun 15, 2012
'''

import datetime, unittest
from selenium import selenium
import cfg

try:
    import json
except ImportError:
    import simplejson as json

class SeleniumTestCase(unittest.TestCase):
    __test__ = False
    
    def setUp(self):
        try:
            c = {"username": cfg.config['username'],
                 "access-key": cfg.config['access-key'],
                 "job-name": getattr(self, "_testMethodName", self.__class__.__name__).replace('_', ' ').capitalize(),
                 "os": self.os,
                 "browser": self.browser,
                 "browser-version": self.version,
                 "command-timeout": 600000,
                 "idle-timeout": 300000,
                 "tags": str(datetime.datetime.now()),
                 }
            
            session = selenium(cfg.config['host'],
                               cfg.config['port'],
                               json.dumps(c),
                               "http://" + cfg.config['base-url'])
                
            session.start()
            session.set_timeout(90000)
            self.selenium = session
        
        except AttributeError:
            pass
    
    def tearDown(self):
        try:
            self.selenium.stop()
        except AttributeError:
            pass