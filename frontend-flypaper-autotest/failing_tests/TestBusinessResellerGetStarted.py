import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

class TestBusinessResellerGetStarted(SeleniumTestCase.SeleniumTestCase):

    def test_business_reseller_get_started(self):
        try:
            sel = self.selenium
            sel.set_speed("200")
            sel.open("/business/reseller/")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Get Started")
            try: self.assertEqual(cfg.config['base-url'] + "/business/reseller/#getstarted", sel.get_location())
            except AssertionError, e: self.verificationErrors.append(str(e))
            #sel.wait_for_page_to_load("60000")
            try: self.failUnless(sel.is_element_present("id=username"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=city"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=reenter_email"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='formContainer']/form/div[7]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='formContainer']//span[.='Ad Agency']"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("name=companyCustomerTypeOther"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='formContainer']/form/div[6]/p[3]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='formContainer']/form/p[2]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='formContainer']/form/p[3]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='formContainer']/form/p[5]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='formContainer']/form/input[3]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=menu"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=footer"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='wrapper']/div[3]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            self.failUnless(sel.is_text_present("Pros - Apply to become an Issuu Reseller."))
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"

globals().update(make_platform_classes.make_platform_classes(TestBusinessResellerGetStarted))