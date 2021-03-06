import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

import unittest, xmlrunner

class TestUserAccountBilling(SeleniumTestCase.SeleniumTestCase):
    
    def test_user_account_billing(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/user/account/login?onLogin=http%3A%2F%2F" + cfg.config['base-url'] + "%2Fuser%2Faccount%2Fbilling")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Account Center Billing", sel.get_title())
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='bgColor']/div[1]/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='account-billingInfo']/div/div[1]"))
            self.failUnless(sel.is_element_present("id=footerText"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='billingHistoryContainer']/div"))
            self.failUnless(sel.is_text_present("Transaction History"))
            sel.click("xpath=//div[@class='page-wrapper']/div[2]")
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

globals().update(make_platform_classes.make_platform_classes(TestUserAccountBilling))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))