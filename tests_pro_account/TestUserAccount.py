import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

class TestUserAccount(SeleniumTestCase.SeleniumTestCase):
        
    def test_user_account(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/login?onLogin=http%3A%2F%2F" + cfg.config['base-url'] + "%2Fuser%2Faccount")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "PROaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Account Center", sel.get_title())
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_text_present("Account Center"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='account-summary']/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='account-info']/div[1]"))
            self.failUnless(sel.is_element_present("link=Change Plan"))
            '''
            self.failUnless(sel.is_element_present("xpath=//div[@id='subaccounts-listing']/table"))
            sel.click("xpath=//td[@class='hac']/div")
            self.failUnless(sel.is_element_present("link=Change Account Plan"))
            self.failUnless(sel.is_element_present("link=Unlink Account"))
            self.failUnless(sel.is_element_present("id=username"))
            self.failUnless(sel.is_element_present("id=password"))
            self.failUnless(sel.is_element_present("link=Add Account"))
            self.failUnless(sel.is_element_present("xpath=//tr[@class='commander']/td[2]"))
            '''
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
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
                
globals().update(make_platform_classes.make_platform_classes(TestUserAccount))