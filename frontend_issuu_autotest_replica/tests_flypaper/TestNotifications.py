import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

class TestNotifications(SeleniumTestCase):
    
    def test_notifications(self):
        try:
            sel = self.selenium
            sel.set_speed("1000")
            sel.open("https://flypaper.issuu.com/signin?onLogin=http%3A%2F%2Fflypaper.issuu.com%2Fhome%2Fsettings%2Fnotifications")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("id=login-button")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Account Settings")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Notifications")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//form[@id='notifications']//h2[.='Digest email']")
            try: self.failUnless(sel.is_text_present("Digest email"))  
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("My publications"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("Followers"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("Issuu newsletters"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("xpath=//label[@for='notify_digestEmail_false']//span[.='Off']")
            sel.check("id=notify_digestEmail_false")
            sel.click("xpath=//label[@for='notify_myDocumentToStack_false']//span[.='Off']")
            sel.check("id=notify_myDocumentToStack_false")
            sel.click("xpath=//label[@for='notify_followed_true']//span[.='On']")
            sel.check("id=notify_followed_true")
            sel.click("xpath=//label[@for='notify_newsletter_false']//span[.='Off']")
            sel.check("id=notify_newsletter_false")
            sel.click("xpath=//label[@for='notify_newsletter_true']//span[.='On']")
            sel.check("id=notify_newsletter_true")
            sel.click("xpath=//label[@for='notify_myDocumentToStack_true']//span[.='On']")
            sel.check("id=notify_myDocumentToStack_true")
            sel.click("xpath=//label[@for='notify_digestEmail_true']//span[.='On']")
            sel.check("id=notify_digestEmail_true")
            sel.click("xpath=//label[@for='notify_digestEmail_false']//span[.='Off']")
            sel.check("id=notify_digestEmail_false")
            sel.click("xpath=//label[@for='notify_myDocumentToStack_false']//span[.='Off']")
            sel.check("id=notify_myDocumentToStack_false")
            sel.click("xpath=//label[@for='notify_followed_false']//span[.='Off']")
            sel.check("id=notify_followed_false")
            sel.click("xpath=//label[@for='notify_newsletter_false']//span[.='Off']")
            sel.check("id=notify_newsletter_false")
            sel.click("xpath=//label[@for='notify_newsletter_true']//span[.='On']")
            sel.check("id=notify_newsletter_true")
            sel.click("xpath=//label[@for='notify_followed_true']//span[.='On']")
            sel.check("id=notify_followed_true")
            sel.click("xpath=//label[@for='notify_myDocumentToStack_true']//span[.='On']")
            sel.check("id=notify_myDocumentToStack_true")
            sel.click("xpath=//label[@for='notify_digestEmail_true']//span[.='On']")
            sel.check("id=notify_digestEmail_true")
            sel.click("xpath=//form[@id='notifications']/p/button")
            sel.click("id=logout-link")
            sel.wait_for_page_to_load("60000")
                
            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #print self.__class__.__name__ + " failed!"
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
        
globals().update(make_platform_classes.make_platform_classes(TestNotifications))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test-reports'))