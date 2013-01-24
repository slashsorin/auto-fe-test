import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestBookmarksReceivedFREE(SeleniumTestCase.SeleniumTestCase):
        
    def test_bookmarks_received(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/freeaccount/bookmarksreceived")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("id=input_keywords"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            sel.click("xpath=//span[@class='system-blue-shade-slim-btn-text']/strong/span")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']//h1[.='Bookmarks received']"))
            self.failUnless(sel.is_element_present("xpath=//span[@class='system-blue-shade-slim-btn-text']/strong"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("id=input_keywords"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            sel.click("xpath=//span[@class='system-blue-shade-slim-btn-text']/strong/span")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']//h1[.='Bookmarks received']"))
            self.failUnless(sel.is_element_present("xpath=//span[@class='system-blue-shade-slim-btn-text']/strong"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]"))
            sel.click("link=Logout")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - freeaccount - Bookmarks received", sel.get_title())
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
        
globals().update(make_platform_classes.make_platform_classes(TestBookmarksReceivedFREE))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))