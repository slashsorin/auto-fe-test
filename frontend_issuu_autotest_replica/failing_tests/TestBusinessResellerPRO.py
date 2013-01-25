import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestBusinessResellerPRO(SeleniumTestCase.SeleniumTestCase):

    def test_business_reader(self):
        try:
            sel = self.selenium
            sel.open("/business/reseller/")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=menu"))
            sel.click("link=Issuu Business Solutions")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu Pro", sel.get_title())
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='wrapper']/div[3]"))
            self.failUnless(sel.is_element_present("link=Issuu Reseller"))
            self.failUnless(sel.is_element_present("link=Get Started"))
            sel.click("link=Get Started")
            self.failUnless(sel.is_text_present("Pros - Apply to become an Issuu Reseller."))
            sel.click("link=Issuu Reseller")
            self.failUnless(sel.is_element_present("xpath=//div[@id='wrapper']/div[4]"))
            self.failUnless(sel.is_element_present("link=Apply to become a Reseller"))
            self.failUnless(sel.is_element_present("id=footer"))
            try: self.failUnless(sel.is_text_present("As you add clients and products to your Reseller account, you start building up discount. You can receive up to 40% discount. Learn more once you've signed up."))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='footercontent']//a[.='Issuu Reader']"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            
            #print self.__class__.__name__ + " passed!"
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                #print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestBusinessResellerPRO))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))