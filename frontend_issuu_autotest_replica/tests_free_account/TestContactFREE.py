import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestContactFREE(SeleniumTestCase.SeleniumTestCase):
        
    def test_contact(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/about/contact")
            sel.wait_for_page_to_load("60000")
            sel.click("link=About us")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Support")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Press")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//div[@class='page-wrapper']/div[2]/div[2]/ul[1]/li[5]/a")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Jobs")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Business")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Blog")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Terms of Services")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Pro Terms of Use")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Parent Account Terms")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=AdPages Terms")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=DMCA guidelines")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Copyright FAQ")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
    
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("id=btn_search"))
            sel.mouse_over("xpath=//ul[@id='top-menubar']/li[1]/div/div/a")
            self.failUnless(sel.is_element_present("xpath=//ul[@id='top-menubar']/li[1]/div"))
            self.failUnless(sel.is_element_present("link=Create account"))
            self.failUnless(sel.is_element_present("link=Login"))
            sel.set_speed("500")
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            try: self.failUnless(sel.is_element_present("link=Create account"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//li[@id='menubar-user']/div/div/a/span[1]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
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
            sel.click("link=Business")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu Pro", sel.get_title())
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.set_speed("500")
            sel.click("link=Terms of Services")
            sel.wait_for_page_to_load("60000")
            sel.click("link=About us")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Support")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Press")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//div[@class='page-wrapper']/div[2]/div[2]/ul[1]/li[5]/a")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Jobs")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Business")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.set_speed("500")
            sel.click("link=Blog")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Terms of Services")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Pro Terms of Use")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Parent Account Terms")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=AdPages Terms")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=DMCA guidelines")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Copyright FAQ")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("id=btn_search"))
            sel.mouse_over("xpath=//ul[@id='top-menubar']/li[1]/div/div/a")
            self.failUnless(sel.is_element_present("xpath=//ul[@id='top-menubar']/li[1]/div"))
            self.failUnless(sel.is_element_present("link=Create account"))
            self.failUnless(sel.is_element_present("link=Login"))
            sel.click("link=Logout")
            sel.wait_for_page_to_load("60000")
            
            #print self.__class__.__name__ + " passed!"
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                #print self.__class__.__name__ + " failed!"
            
globals().update(make_platform_classes.make_platform_classes(TestContactFREE))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))