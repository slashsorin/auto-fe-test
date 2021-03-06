import sys
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

class TestBusinessHowTo_LoggedInFree(SeleniumTestCase.SeleniumTestCase):
    
    def test_business_how_to_logged_in(self):
        try:
            sel = self.selenium
            sel.open("/business/howto_customize")
            sel.set_speed("200")
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='howtomaincornerB']/div/div/div/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='howtomaincornerB']/div/div/div/div/table/tbody/tr/td/div[3]/img"))
            sel.click("link=Uploading")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='howtomaincornerB']/div/div/div/div/table/tbody/tr/td"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='howtomaincornerB']/div/div/div/div/table/tbody/tr/td/div[5]/img"))
            sel.click("link=Embedding a Mini-Issuu")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='howtomaincornerB']/div/div/div/div/table/tbody/tr/td/div[11]"))
            sel.click("link=Embedding a Standalone Issuu")
            sel.wait_for_page_to_load("60000")
            try: self.assertEqual("Issuu Pro - How-to Standalone", sel.get_title())
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.assertEqual(cfg.config['base-url'] + "/business/howto_standalone", sel.get_location())
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("link=Getting Issuu on Facebook profiles")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu Pro - How-to Facebook profile", sel.get_title())
            self.failUnless(sel.is_element_present("xpath=//div[@class='howtomaincornerB']/div/div/div/div/table/tbody/tr/td/div[8]"))
            sel.click("link=Statistics")
            sel.wait_for_page_to_load("60000")
            try: self.assertEqual("Issuu Pro - How-to Statistics", sel.get_title())
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='howtomaincornerB']/div/div/div/div/table/tbody/tr/td/div[8]/img"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("link=Managing your Library")
            sel.wait_for_page_to_load("60000")
            try: self.assertEqual(cfg.config['base-url'] + "/business/howto_library", sel.get_location())
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.assertEqual("Issuu Pro - How-to library", sel.get_title())
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("link=Customize Viewer")
            sel.wait_for_page_to_load("60000")
            try: self.assertEqual("Issuu Pro - How-to customize", sel.get_title())
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='howtomaincornerB']/div/div/div/div/table/tbody/tr/td"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("xpath=//div[@class='howtomaincornerB']/div/div/div/div/table/tbody/tr/td")
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
    
globals().update(make_platform_classes.make_platform_classes(TestBusinessHowTo_LoggedInFree))
