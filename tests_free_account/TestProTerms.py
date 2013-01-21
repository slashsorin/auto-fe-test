import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestProTerms(SeleniumTestCase.SeleniumTestCase):
    
    def test_pro_terms(self):
        try:
            sel = self.selenium
            sel.set_speed("1000")
            sel.open("/about/proterms")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Parent Account Terms")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Parent Account Terms")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=AdPages Terms")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Parent Account Terms")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=DMCA guidelines")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Copyright FAQ")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Privacy policy")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Business")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Support")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Jobs")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Contact")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[3]"))
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            sel.click("link=Login")
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            sel.click("link=Logout")
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestProTerms))
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))