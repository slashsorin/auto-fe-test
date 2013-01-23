#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jun 15, 2012
'''

from selenium import selenium
from unittest import TestCase
import os
import cfg

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
                 "idle-timeout": cfg.config['idle-timeout'],
                 "max-duration": cfg.config['max-duration'],
                 "command-timeout": cfg.config['command-timeout']
                 }
            if os.getenv('BUILD_NUMBER'):
                c['build'] = os.getenv('BUILD_NUMBER')

            if os.getenv('GIT_COMMIT'):
                if not c.has_key('custom-data'):
                    c['custom-data'] = {}
                if not c.has_key('tags'):
                    c['tags'] = []
                c['custom-data']['commit'] = os.getenv('GIT_COMMIT')
                c['tags'].append('commit:'+os.getenv('GIT_COMMIT'))

            if cfg.config.has_key('avoid-proxy'):
                c['avoid-proxy'] = cfg.config['avoid-proxy']
            if hasattr(self,'avoid_proxy'):
                c['avoid-proxy'] = self.avoid_proxy

            session = selenium(cfg.config['host'],
                               cfg.config['port'],
                               json.dumps(c),
                               "http://" + cfg.config['base-url'])
            session.start()
            session.set_timeout(cfg.config['session_timeout'])
            self.selenium = session
        except AttributeError:
            pass
        except Exception, e:
            print e

    def tearDown(self):
        try:
            self.selenium.stop()
        except AttributeError:
            pass
