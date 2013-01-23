import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

import unittest, xmlrunner

class TestJoinUs(SeleniumTestCase.SeleniumTestCase):
    
    def test_join_us(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/joinus/")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Let's work together", sel.get_title())
            self.failUnless(sel.is_element_present("xpath=//div[@class='containerTopHeader']/div[1]/a/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='twitterspace']/h1"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='panes']/div[3]/img"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='containerBgTop']/div[2]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footer']/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='containerFooter']/p"))
        
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
            
globals().update(make_platform_classes.make_platform_classes(TestJoinUs))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))