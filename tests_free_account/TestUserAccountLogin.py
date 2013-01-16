import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

class TestUserAccountLogin(SeleniumTestCase.SeleniumTestCase):
    
    def test_user_account_login(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/login?onLogin=http%3A%2F%2F" + cfg.config['base-url'] + "%2Fuser%2Faccount%2Flogin")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Account Center Login", sel.get_title())
            sel.type("id=password", "autotest")
            sel.click("xpath=//a[@id='submitbutton']/span[1]/strong")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Account Center", sel.get_title())
            sel.open("/user/account/login")
            sel.type("id=password", "autotest")
            sel.click("xpath=//a[@id='submitbutton']/span[1]/strong")
            sel.wait_for_page_to_load("60000")
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
    
globals().update(make_platform_classes.make_platform_classes(TestUserAccountLogin))