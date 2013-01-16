import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestConfirmEmail(SeleniumTestCase.SeleniumTestCase):
    
    def test_confirm_email(self):
        try:
            sel = self.selenium
            sel.open("/confirm_email")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=logo"))
            self.failUnless(sel.is_element_present("xpath=//div[2]/div[1]/div"))
            self.failUnless(sel.is_element_present("link=Sign up"))
            self.failUnless(sel.is_element_present("link=Log in"))
            self.failUnless(sel.is_element_present("xpath=//a[@id='topLoginWithFaceBook']/span"))
            self.failUnless(sel.is_text_present("Welcome back"))
            self.failUnless(sel.is_element_present("xpath=//div[2]/div[7]/a/span[2]/strong"))
            self.failUnless(sel.is_text_present("Please verify your account. Click below."))
            self.failUnless(sel.is_element_present("xpath=//div[2]/div[4]/img"))
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass 
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestConfirmEmail))
