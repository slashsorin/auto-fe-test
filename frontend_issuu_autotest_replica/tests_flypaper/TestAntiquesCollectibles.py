import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

import hmac
from hashlib import md5
import cfg

class TestAntiquesCollectibles(SeleniumTestCase):
   
    
    def test_antiques_collectibles(self):
        try:
            sel = self.selenium
            sel.set_speed("3000")
            sel.open("/antiques-collectibles")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='main-container']/section"))
            self.failUnless(sel.is_element_present("xpath=//html/body/div/section/div/div/h3"))
            self.failUnless(sel.is_element_present("xpath=//html/body/div/section/div/div/p"))
            self.failUnless(sel.is_element_present("xpath=//html/body/div/section/div/div/p[2]"))
            self.failUnless(sel.is_element_present("xpath=//html/body/div/section/div/div"))
            self.failUnless(sel.is_element_present("xpath=//html/body/div/section/div/a/img"))
            
            user = cfg.config['username']
            key = cfg.config['access-key']
            
            linkID = self.selenium.get_eval("selenium.sessionId")
            token = hmac.new(user + ":" + key, linkID, md5).hexdigest()
            
            print "https://saucelabs.com/jobs/" + linkID + "?auth=" + token
            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #print self.__class__.__name__ + " failed!"
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
        
globals().update(make_platform_classes.make_platform_classes(TestAntiquesCollectibles))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test-reports'))