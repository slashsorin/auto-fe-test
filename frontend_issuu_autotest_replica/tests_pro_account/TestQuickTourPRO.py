import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestQuickTourPRO(SeleniumTestCase.SeleniumTestCase):
    
    def test_quick_tour(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/signup/quicktour")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Signup - A quick tour", sel.get_title())
            self.failUnless(sel.is_element_present("xpath=//div[2]/div[4]/img"))
            self.failUnless(sel.is_element_present("link=issuu"))
            self.failUnless(sel.is_element_present("id=t3BodyTop"))
            self.failUnless(sel.is_element_present("xpath=//div[2]/div[1]/div"))
            self.failUnless(sel.is_element_present("xpath=//span[@class='system-blue-shade-fat-btn-text']/strong"))
            sel.click("id=loginLink")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "PROaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Signup - A quick tour", sel.get_title())
            self.failUnless(sel.is_element_present("xpath=//div[2]/div[4]/img"))
            self.failUnless(sel.is_element_present("link=issuu"))
            self.failUnless(sel.is_element_present("id=t3BodyTop"))
            self.failUnless(sel.is_element_present("xpath=//div[2]/div[1]/div"))
            self.failUnless(sel.is_element_present("xpath=//span[@class='system-blue-shade-fat-btn-text']/strong"))
            sel.click("link=Log out")
            sel.wait_for_page_to_load("60000")
            
            #print self.__class__.__name__ + " passed!"
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                #print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestQuickTourPRO))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))