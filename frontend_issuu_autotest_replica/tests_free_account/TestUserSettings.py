import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

class TestUserSettings(SeleniumTestCase.SeleniumTestCase):
        
    def test_user_settings(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/login?onLogin=http%3A%2F%2F" + cfg.config['base-url'] + "%2Fuser%2Fsettings")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Settings", sel.get_title())
            self.failUnless(sel.is_element_present("link=General settings"))
            self.failUnless(sel.is_element_present("link=Notifications"))
            sel.click("id=accountPasswordLink")
            self.failUnless(sel.is_element_present("xpath=//div[@class='d_main']/div/div"))
            sel.click("xpath=//div[@class='dia_box']/div")
            sel.click("link=change email")
            self.failUnless(sel.is_element_present("xpath=//div[@class='d_main']/div/div/div"))
            sel.click("xpath=//div[@class='dia_box']/div")
            self.failUnless(sel.is_element_present("id=firstName"))
            self.failUnless(sel.is_element_present("id=lastName"))
            self.failUnless(sel.is_element_present("id=web"))
            self.failUnless(sel.is_element_present("id=about"))
            self.failUnless(sel.is_element_present("link=Save changes"))
            sel.check("id=accountTypeBusiness")
            self.failUnless(sel.is_element_present("id=about"))
            self.failUnless(sel.is_element_present("id=profileInformationForm"))
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
                
globals().update(make_platform_classes.make_platform_classes(TestUserSettings))