import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

class TestLogInLogOut(SeleniumTestCase):
    
    def test_log_in_log_out(self):
        try:
            sel = self.selenium
            sel.open("/explore")
            sel.wait_for_page_to_load("60000")
            sel.click("id=login-link")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("id=loginButton")
            sel.click("xpath=//nav[@class='userstatus']//a[.='sorintest ']")
            sel.click("id=logout-link")
            sel.click("id=login-link")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintestt")
            sel.click("id=loginButton")
            try: self.failIf(sel.is_text_present("sorintest"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.type("id=password", "sorintest")
            sel.click("id=loginButton")
            sel.click("xpath=//nav[@class='userstatus']//a[.='sorintest ']")
            sel.click("id=logout-link")
            
            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #print self.__class__.__name__ + " failed!"
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
        
globals().update(make_platform_classes.make_platform_classes(TestLogInLogOut))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test-reports'))