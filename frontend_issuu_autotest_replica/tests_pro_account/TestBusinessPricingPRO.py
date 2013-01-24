import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestBusinessPricingPRO(SeleniumTestCase.SeleniumTestCase):
    
    def test_business_pricing(self):
        try:
            sel = self.selenium
            sel.set_speed("200")
            sel.open("/business/pricing")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[2]/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[2]/div[2]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[5]/div[2]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[5]/div[1]"))
            self.failUnless(sel.is_text_present("No, you can upload as many publications as you like. We do however expect fair use of our service so if you exceed 1 million readers a month or 15GB storage the price is subject to negotiation."))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_text_present("Main benefits"))
            self.failUnless(sel.is_text_present("Main features"))
            self.failUnless(sel.is_element_present("xpath=//ul[@class='ol-ul-override']//a[.='Cases']"))
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[1]/ul"))
        
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
                
globals().update(make_platform_classes.make_platform_classes(TestBusinessPricingPRO))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))