import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestLogin(SeleniumTestCase.SeleniumTestCase):
    
    def test_login(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/login")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Login", sel.get_title())
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("id=putContentHere"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("id=username"))
            self.failUnless(sel.is_element_present("id=password"))
            self.failUnless(sel.is_element_present("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']"))
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            self.failUnless(sel.is_text_present("This field missing."))
            self.failUnless(sel.is_text_present("Password missing."))
            sel.type("id=username", "PROaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            #self.assertEqual("http://issuu.com/home", sel.get_location())
            sel.open("/login")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Login", sel.get_title())
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("id=putContentHere"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("id=username"))
            self.failUnless(sel.is_element_present("id=password"))
            self.failUnless(sel.is_element_present("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']"))
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            self.failUnless(sel.is_text_present("This field missing."))
            self.failUnless(sel.is_text_present("Password missing."))
            sel.type("id=username", "issuub1")
            sel.type("id=password", "issuu")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Logout")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Login", sel.get_title())
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestLogin))