#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps May 14, 2012
'''


import httplib
import base64
#import Constants as ct
import cfg

try:
    import json
except ImportError:
    import simplejson as json

base64string = base64.encodestring('%s:%s' % (cfg.config['username'], cfg.config['access-key']))[:-1]
    
def set_test_status(jobid, passed=True):
        body_content = json.dumps({"passed": passed})
        connection = httplib.HTTPConnection("saucelabs.com")
        connection.request('PUT', '/rest/v1/%s/jobs/%s' % (cfg.config['username'], jobid),
                           body_content,
                           headers={"Authorization": "Basic %s" % base64string})
        result = connection.getresponse()
        return result.status == 200