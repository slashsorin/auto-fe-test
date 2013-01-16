#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jun 15, 2012
'''

from selenium import selenium
from unittest import TestCase
import cfg

import EnvironmentParam

tp = EnvironmentParam.GetParams()

try:
    import json
except ImportError:
    import simplejson as json

class SeleniumTestCase(TestCase):
    __test__ = False

    def setUp(self):
        try:
            #for platf in cfg.config['platforms']:
            c = {"username": cfg.config['username'],
                 "access-key": cfg.config['access-key'],
                 "job-name": getattr(self, "_testMethodName", self.__class__.__name__).replace('_', ' ').capitalize(),
                 "os": self.os,
                 "browser": self.browser,
                 "browser-version": self.version,
                 #need to check that the idle-timeout works !!!
                 "idle-timeout": 300
                 }
            session = selenium(cfg.config['host'],
                           cfg.config['port'],
                           json.dumps(c),
                           "http://" + cfg.config['base-url'])
            session.start()
            session.set_timeout(90000)
            session.selenium.set_speed(self, 500)
            self.selenium = session
        except AttributeError:
            pass

    def tearDown(self):
        try:
            self.selenium.stop()
        except AttributeError:
            pass