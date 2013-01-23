import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestAdPagesTerms(SeleniumTestCase.SeleniumTestCase):
 
    def test_ad_pages_terms(self):
        try:
            sel = self.selenium
            sel.open("/about/adpagesterms")
            sel.wait_for_page_to_load("60000")
            try: self.failUnless(sel.is_text_present("Issuu AdPages Terms of Service"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='span-10']/div/p[1]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[3]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("xpath=//div[@class='page-wrapper']/div[2]/div[3]")
            try: self.failUnless(sel.is_text_present("Questions about copyright?"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=top-menubar-container"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[2]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            try: self.failUnless(sel.is_text_present("Issuu AdPages Terms of Service"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='span-10']/div/p[1]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[3]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("xpath=//div[@class='page-wrapper']/div[2]/div[3]")
            try: self.failUnless(sel.is_text_present("Questions about copyright?"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=top-menubar-container"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[2]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
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

globals().update(make_platform_classes.make_platform_classes(TestAdPagesTerms))