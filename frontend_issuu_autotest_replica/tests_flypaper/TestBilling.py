import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

class TestBilling(SeleniumTestCase):
    
    def test_billing(self):
        try:
            sel = self.selenium
            sel.set_speed("2000")
            sel.open("/signin?onLogin=https%3A%2F%2Fissuu.com%2Fhome%2Fsettings%2Fbilling")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("id=login-button")
            sel.wait_for_page_to_load("60000")
            #sel.click("xpath=//a[@id='acceptButton']//strong[.='I accept the Terms of Service']")
            #sel.wait_for_page_to_load("60000")
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='main-container']//section[normalize-space(.)='Account summary']"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='main-container']/section[2]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='main-container']/section[3]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='main-container']/section[4]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//body/nav"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//body/header"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//footer/div"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            
            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            self.selenium.get_eval("selenium.sessionId")
            
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            self.selenium.get_eval("selenium.sessionId")
            #if  sys.exc_info()[1]:
                #print self.__class__.__name__ + " failed!"
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                
globals().update(make_platform_classes.make_platform_classes(TestBilling))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test-reports'))