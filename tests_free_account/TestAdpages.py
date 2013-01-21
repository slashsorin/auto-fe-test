import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest
import xmlrunner

class TestAdpages(SeleniumTestCase.SeleniumTestCase):

    def test_adpages(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/adpages")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=ad-page"))
            self.failUnless(sel.is_text_present("How it works"))
            self.failUnless(sel.is_text_present("Precise stats"))
            self.failUnless(sel.is_text_present("Engage new audiences"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='adpages-about']/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='adpages-about']/div[2]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='adpages-about']/div[3]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='ad-page']/div[2]/div[3]"))
            self.failUnless(sel.is_element_present("link=Create new Ad"))
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            sel.click("id=adpages-tab1")
            sel.click("link=Create new Ad")
            sel.wait_for_page_to_load("60000")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("xpath=//form[@id='myForm']/div[2]/a/span[2]")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("ISSUU - Advertise on Issuu", sel.get_title())
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
    
globals().update(make_platform_classes.make_platform_classes(TestAdpages))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))