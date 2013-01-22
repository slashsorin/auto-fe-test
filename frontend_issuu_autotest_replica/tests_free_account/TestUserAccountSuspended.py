import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

class TestUserAccountSuspended(SeleniumTestCase.SeleniumTestCase):
    
    def test_user_account_suspended(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/login?onLogin=http%3A%2F%2F" + cfg.config['base-url'] + "%2Fuser%2Faccount%2Fsuspended")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "testusersorin")
            sel.type("id=password", "testusersorin")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Account Center / Suspended", sel.get_title())
            self.failUnless(sel.is_text_present("Account Suspended"))
            self.failUnless(sel.is_text_present("Your account has been suspended"))
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='account-info']/div"))
            self.failUnless(sel.is_element_present("link=Pay now"))
            self.failUnless(sel.is_element_present("link=Update billing information"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            #sel.click("xpath=//div[@id='account-info']/div/div[2]/a[2]/span/strong")
            #sel.wait_for_page_to_load("60000")
            #sel.go_back()
            #sel.wait_for_page_to_load("60000")
            #sel.click("xpath=//div[@id='account-info']/div/div[2]/a[1]/span/strong")
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
                
globals().update(make_platform_classes.make_platform_classes(TestUserAccountSuspended))