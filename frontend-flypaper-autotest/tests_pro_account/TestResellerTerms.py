import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestResellerTerms(SeleniumTestCase.SeleniumTestCase):
        
    def test_reseller_terms(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/about/resellerterms")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[3]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[1]/div[2]/h2"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[2]"))
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='span-10']/div/p[3]"))
            sel.click("xpath=//div[@class='span-10']/div/p[3]")
            self.failUnless(sel.is_element_present("link=Login"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "PROaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[3]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[1]/div[2]/h2"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[2]"))
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='span-10']/div/p[3]"))
            sel.click("xpath=//div[@class='span-10']/div/p[3]")
            self.failUnless(sel.is_element_present("link=Logout"))
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

globals().update(make_platform_classes.make_platform_classes(TestResellerTerms))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))