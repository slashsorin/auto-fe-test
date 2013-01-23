import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestPrintLoggedIn(SeleniumTestCase.SeleniumTestCase):
    
    def test_print_logged_in(self):
        try:
            sel = self.selenium
            sel.set_speed("1000")
            sel.open("/PROaccount/docs/dev_sauce_ondemand_service")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "PROaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//form[@id='myForm']/div[2]/a/span[2]")
            sel.wait_for_page_to_load("60000")
            sel.set_timeout("2000")
            sel.open("/PROaccount/docs/dev_sauce_ondemand_service#print")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=print-overlay"))
            self.failUnless(sel.is_element_present("id=print-overlay-content"))
            self.failUnless(sel.is_element_present("id=pod-img"))
            self.failUnless(sel.is_text_present("Or order prints"))
            self.failUnless(sel.is_element_present("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Print publication']"))
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestPrintLoggedIn))