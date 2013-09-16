import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

class TestBasicSettings(SeleniumTestCase):
   
    def test_basic_settings(self):
        try:
            sel = self.selenium
            sel.set_speed("3000")
            sel.open("/signin?onLogin=https%3A%2F%2Fissuu.com%2Fhome%2Fsettings")
            sel.wait_for_page_to_load("60000")
            sel.type("id=login-username", "sorintest")
            sel.type("id=login-password", "sorintest")
            sel.click("id=login-button")
            sel.wait_for_page_to_load("60000")
            #sel.click("xpath=//a[@id='acceptButton']//strong[.='I accept the Terms of Service']")
            #sel.wait_for_page_to_load("60000")
            try: self.failUnless(sel.is_element_present("id=displayname"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='user-info']/fieldset[1]/p[2]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=emailpreview"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=passwordpreview"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("id=passwordpreview")
            try: self.failUnless(sel.is_element_present("id=newPasswordForm"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=firstname"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=lastname"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=city"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=country"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=website"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=website"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=about"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("xpath=//label[@for='safesearch-off']//span[.='Off']")
            sel.check("id=safesearch-off")
            sel.click("xpath=//label[@for='safesearch-on']//span[.='On']")
            sel.check("id=safesearch-on")
            sel.click("xpath=//label[@for='safesearch-off']//span[.='Off']")
            sel.check("id=safesearch-off")
            sel.click("xpath=//label[@for='safesearch-on']//span[.='On']")
            sel.check("id=safesearch-on")
            sel.type("id=about", "personal description")
            #sel.click("xpath=//div[@id='user-info']/p/input")
            
            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #print self.__class__.__name__ + " failed!"
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
        
globals().update(make_platform_classes.make_platform_classes(TestBasicSettings))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test-reports'))