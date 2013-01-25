import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestSignupQuicktourFREE(SeleniumTestCase.SeleniumTestCase):
    
    def test_signup_quicktour(self):
        try:
            sel = self.selenium
            sel.open("/signup/quicktour")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[2]/div[4]/img"))
            self.failUnless(sel.is_text_present("A quick tour"))
            self.failUnless(sel.is_element_present("xpath=//span[@class='system-blue-shade-fat-btn-text']/strong"))
            self.failUnless(sel.is_element_present("xpath=//div[2]/div[1]/div"))
            self.failUnless(sel.is_element_present("id=logo"))
            self.failUnless(sel.is_element_present("id=t3BodyTop"))
            self.failUnless(sel.is_element_present("id=loginLink"))
        
            #print self.__class__.__name__ + " passed!"
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                #print self.__class__.__name__ + " failed!"

globals().update(make_platform_classes.make_platform_classes(TestSignupQuicktourFREE))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))