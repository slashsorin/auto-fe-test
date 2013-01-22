import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

class TestResendemail(SeleniumTestCase.SeleniumTestCase):
    
    def test_resendemail(self):
        try:
            sel = self.selenium
            sel.set_speed("1000")
            sel.open("/resendemail")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Resend confirmation email", sel.get_title())
            sel.type("id=username", "ResendTest1")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Resend']")
            self.failUnless(sel.is_element_present("xpath=//div[@id='screen2']/div[4]"))
            self.failUnless(sel.is_text_present("A confirmation email has been sent to you ."))
            sel.open("/resendemail")
            sel.wait_for_page_to_load("60000")
            sel.check("name=differentEmail")
            sel.type("id=username", "resendtest1")
            sel.type("id=newEmail", "svd+testtest1@issuu.com")
            sel.type("id=password", "resend")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Resend']")
            self.failUnless(sel.is_element_present("xpath=//div[@id='screen2']/div[4]"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Resend confirmation email", sel.get_title())
            sel.type("id=username", "ResendTest1")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Resend']")
            self.failUnless(sel.is_element_present("xpath=//div[@id='screen2']/div[4]"))
            self.failUnless(sel.is_text_present("A confirmation email has been sent to you ."))
            sel.open("/resendemail")
            sel.wait_for_page_to_load("60000")
            sel.check("name=differentEmail")
            sel.type("id=username", "resendtest1")
            sel.type("id=newEmail", "svd+testtest1@issuu.com")
            sel.type("id=password", "resend")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Resend']")
            self.failUnless(sel.is_element_present("xpath=//div[@id='screen2']/div[4]"))
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
                
globals().update(make_platform_classes.make_platform_classes(TestResendemail))