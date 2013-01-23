import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestFlagMail(SeleniumTestCase.SeleniumTestCase):
    
    def test_flag_mail(self):
        try:
            sel = self.selenium
            sel.open("/flag/mail")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_text_present("Email flagging"))
            sel.check("id=harassment")
            sel.check("id=phishing")
            sel.check("id=other")
            sel.check("id=spam")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']/strong")
            self.failUnless(sel.is_text_present("Oops, please change something and try again 200"))
            self.failUnless(sel.is_text_present("You are about to flag the following user"))
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"

globals().update(make_platform_classes.make_platform_classes(TestFlagMail))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))