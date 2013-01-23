import sys
import SetTestStatus as sts
import make_platform_classes, SeleniumTestCase

class TestDocs(SeleniumTestCase.SeleniumTestCase):
   
    def test_docs(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/issuubiz/docs")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='docs-list']/div"))
            sel.click("xpath=//span[@class='system-blue-shade-slim-btn-text']/strong/span")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//p[@class='book-cover']/a/img")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - issuubiz - Documents", sel.get_title())
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//p[@class='book-cover']/a/img")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
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
    
globals().update(make_platform_classes.make_platform_classes(TestDocs))
