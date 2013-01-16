import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestCopyright(SeleniumTestCase.SeleniumTestCase):
    
    def test_copyright(self):
        try:
            sel = self.selenium
            sel.open("/about/copyright")
            sel.wait_for_page_to_load("60000")
            sel.set_speed("500")
            sel.click("link=About us")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Support")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Jobs")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Contact")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Business")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu Pro", sel.get_title())
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Copyright", sel.get_title())
            sel.click("link=Terms of Services")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Pro Terms of Use")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//div[@class='page-wrapper']/div[2]/div[2]/ul[1]/li[5]/a")
            sel.wait_for_page_to_load("60000")
            sel.click("link=AdPages Terms")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Jobs")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//div[@class='page-wrapper']/div[2]/div[2]/ul[1]/li[5]/a")
            sel.wait_for_page_to_load("60000")
            sel.click("link=DMCA guidelines")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Copyright FAQ")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=input_keywords"))
            self.failUnless(sel.is_element_present("link=Upload"))
            sel.click("link=Upload")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("link=Login"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("link=Create account"))
            sel.click("link=Create account")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[3]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[7]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[7]/div[2]/div/div/a/span"))
            sel.mouse_over("xpath=//div[@id='footerText']/div[7]/div[2]/div/div/a/span")
            self.failUnless(sel.is_element_present("xpath=//div[4]/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[1]/p"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            #try: self.failIf(sel.is_element_present("link=Create account"))
            #except AssertionError, e: self.verificationErrors.append(str(e))
            #try: self.failUnless(sel.is_element_present("xpath=//li[@id='menubar-user']/div/div/a/span[1]"))
            #except AssertionError, e: self.verificationErrors.append(str(e))
            self.failUnless(sel.is_text_present("FREEaccount"))
            sel.click("link=About us")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Support")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Jobs")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Contact")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Business")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu Pro", sel.get_title())
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - People", sel.get_title())
            sel.click("link=Terms of Services")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Pro Terms of Use")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//div[@class='page-wrapper']/div[2]/div[2]/ul[1]/li[5]/a")
            sel.wait_for_page_to_load("60000")
            sel.click("link=AdPages Terms")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Jobs")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//div[@class='page-wrapper']/div[2]/div[2]/ul[1]/li[5]/a")
            sel.wait_for_page_to_load("60000")
            sel.click("link=DMCA guidelines")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Copyright FAQ")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=input_keywords"))
            self.failUnless(sel.is_element_present("link=Upload"))
            sel.click("link=Upload")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("link=Login"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("link=Create account"))
            sel.click("link=Create account")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[3]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[7]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[7]/div[2]/div/div/a/span"))
            sel.mouse_over("xpath=//div[@id='footerText']/div[7]/div[2]/div/div/a/span")
            self.failUnless(sel.is_element_present("xpath=//div[4]/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[1]/p"))
            sel.click("link=Logout")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Copyright FAQ")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[3]"))
            self.assertEqual("Issuu - Copyright", sel.get_title())
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestCopyright))
