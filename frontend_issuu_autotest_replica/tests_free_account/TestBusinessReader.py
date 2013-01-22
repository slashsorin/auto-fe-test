import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class IssuuBusinessReader(SeleniumTestCase.SeleniumTestCase):

    def test_issuu_business_reader(self):
        try:
            sel = self.selenium
            sel.open("/business/reader/")
            sel.wait_for_page_to_load("60000")
            try: self.failUnless(sel.is_text_present("Issuu Business Solutions Issuu Reader Pricing Reseller"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='panes']/div[2]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='maincontent']/li[1]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='maincontent']/li[2]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='maincontent']/li[3]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='maincontent']/div"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='maincontent']/li[3]/p[2]/img"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='bottomslider']/img"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            self.failUnless(sel.is_element_present("xpath=//li[@class='trialteaser']/div[2]/a"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='bottomcontent']/li[1]"))
            sel.click("xpath=//div[@id='bottomcontent']/li[1]")
            sel.click("link=Reader Enterprise")
            sel.click("link=Reader Free")
            sel.click("link=Reader Pro")
            sel.click("link=Pricing")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Reseller")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Issuu Business Solutions")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Issuu Reader")
            sel.wait_for_page_to_load("60000")
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(IssuuBusinessReader))
