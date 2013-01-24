import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestPublicationsPRO(SeleniumTestCase.SeleniumTestCase):
    
    def test_publications(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/publications")
            sel.wait_for_page_to_load("60000")
            #self.assertEqual("http://issuu.com/publications", sel.get_location())
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[3]/div[2]/div[1]"))
            self.failUnless(sel.is_element_present("id=shelf"))
            sel.click("link=Dansk")
            sel.click("xpath=//ul[@id='display-grid']//span[.='Text']")
            self.failUnless(sel.is_element_present("xpath=//div[@id='books']/div[1]"))
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("link=Highest rating"))
            self.failUnless(sel.is_element_present("link=Most popular"))
            self.failUnless(sel.is_element_present("link=New arrivals"))
            self.failUnless(sel.is_element_present("link=Most discussed"))
            self.failUnless(sel.is_element_present("link=Most bookmarked"))
            self.failUnless(sel.is_element_present("link=All time"))
            self.failUnless(sel.is_element_present("link=Today"))
            self.failUnless(sel.is_element_present("link=This week"))
            self.failUnless(sel.is_element_present("link=This month"))
            self.failUnless(sel.is_element_present("link=Creative"))
            self.failUnless(sel.is_element_present("link=Sports"))
            self.failUnless(sel.is_element_present("link=Other"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "PROaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//form[@id='myForm']/div[2]/a/span[2]")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[3]/div[2]/div[1]"))
            self.failUnless(sel.is_element_present("id=shelf"))
            sel.click("link=Dansk")
            sel.click("xpath=//ul[@id='display-grid']//span[.='Text']")
            self.failUnless(sel.is_element_present("xpath=//div[@id='books']/div[1]"))
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("link=Highest rating"))
            self.failUnless(sel.is_element_present("link=Most popular"))
            self.failUnless(sel.is_element_present("link=New arrivals"))
            self.failUnless(sel.is_element_present("link=Most discussed"))
            self.failUnless(sel.is_element_present("link=Most bookmarked"))
            self.failUnless(sel.is_element_present("link=All time"))
            self.failUnless(sel.is_element_present("link=Today"))
            self.failUnless(sel.is_element_present("link=This week"))
            self.failUnless(sel.is_element_present("link=This month"))
            self.failUnless(sel.is_element_present("link=Creative"))
            self.failUnless(sel.is_element_present("link=Sports"))
            self.failUnless(sel.is_element_present("link=Other"))
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
    
globals().update(make_platform_classes.make_platform_classes(TestPublicationsPRO))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))