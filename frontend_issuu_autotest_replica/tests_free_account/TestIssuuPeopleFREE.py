import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestIssuuPeopleFREE(SeleniumTestCase.SeleniumTestCase):
    
    def test_issuu_people(self):
        try:
            sel = self.selenium
            sel.open("/people")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - People", sel.get_title())
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("link=Login"))
            self.failUnless(sel.is_element_present("link=Create account"))
            self.failUnless(sel.is_element_present("id=people"))
            self.failUnless(sel.is_element_present("link=Most documents"))
            sel.click("link=Most popular")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Portugal")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Belgium")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Australia")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Spain")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Any")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Italy")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            sel.click("link=Most friends")
            sel.wait_for_page_to_load("60000")
            sel.click("link=All")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Only with picture")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Most recent")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=input_keywords"))
            
            #print self.__class__.__name__ + " passed!"
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                #print self.__class__.__name__ + " failed!"

globals().update(make_platform_classes.make_platform_classes(TestIssuuPeopleFREE))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))