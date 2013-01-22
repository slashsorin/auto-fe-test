import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestMobile(SeleniumTestCase.SeleniumTestCase):
    
    def test_mobile(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/mobile")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Mobile", sel.get_title())
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("id=mobile-publishing"))
            self.failUnless(sel.is_element_present("id=mobile"))
            self.failUnless(sel.is_element_present("id=bottom-features"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_text_present("Publishing gone mobile"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Mobile", sel.get_title())
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("id=mobile-publishing"))
            self.failUnless(sel.is_element_present("id=mobile"))
            self.failUnless(sel.is_element_present("id=bottom-features"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_text_present("Publishing gone mobile"))
            sel.click("link=Logout")
            sel.wait_for_page_to_load("60000")
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestMobile))