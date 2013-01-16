import sys
import SetTestStatus as sts
import make_platform_classes, SeleniumTestCase

class TestDipDownload(SeleniumTestCase.SeleniumTestCase):
  
    def test_dip_download(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/sorintest/docs/automatedtest_doc")
            sel.wait_for_page_to_load("60000")
            sel.set_timeout("1000")
            sel.click("xpath=//li[@class='download']/a/span[1]")
            try: self.failUnless(sel.is_element_present("id=print-overlay"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=username"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=password"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//form[@id='login-form']//strong[.='Log in']"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("Password missing."))
            except AssertionError, e: self.verificationErrors.append(str(e))
            self.failUnless(sel.is_element_present("xpath=//span[@class='system-grey-shade-fat-btn-text']//strong[.='Download']"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='print-overlay']/img"))
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//form[@id='login-form']//strong[.='Log in']")
            self.failUnless(sel.is_element_present("id=print-overlay"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='print-overlay']/img"))
            self.failUnless(sel.is_text_present("Get a professional print delivered to your door"))
            self.failUnless(sel.is_element_present("xpath=//a[@id='print-document']//strong[.='Download']"))
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
        
        except AttributeError:
            pass 
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestDipDownload))
