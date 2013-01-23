import sys
import SetTestStatus as sts
import make_platform_classes, SeleniumTestCase

class TestSearch(SeleniumTestCase.SeleniumTestCase):
                     
    def test_search(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/search")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Search", sel.get_title())
            self.failUnless(sel.is_element_present("id=top-menubar"))
            sel.click("xpath=//ul[@id='search-type-options']//span[.='People']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='search-result']/div[1]"))
            self.failUnless(sel.is_element_present("id=content"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            sel.click("id=next")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@id='search-type-options']//span[.='Documents']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='search-result']/div[1]"))
            self.failUnless(sel.is_element_present("id=content"))
            self.failUnless(sel.is_element_present("id=right-sidebar"))
            sel.click("id=next")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@id='search-type-options']//span[.='People']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@id='search-type-options']//span[.='Documents']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='tag-cloud-box']/p[1]"))
            self.failUnless(sel.is_element_present("id=tag-cloud-box"))
            sel.click("xpath=//ul[@id='search-type-options']//span[.='People']")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Search", sel.get_title())
            self.failUnless(sel.is_element_present("id=top-menubar"))
            sel.click("xpath=//ul[@id='search-type-options']//span[.='People']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='search-result']/div[1]"))
            self.failUnless(sel.is_element_present("id=content"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            sel.click("id=next")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@id='search-type-options']//span[.='Documents']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='search-result']/div[1]"))
            self.failUnless(sel.is_element_present("id=content"))
            self.failUnless(sel.is_element_present("id=right-sidebar"))
            sel.click("id=next")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@id='search-type-options']//span[.='People']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@id='search-type-options']//span[.='Documents']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='tag-cloud-box']/p[1]"))
            self.failUnless(sel.is_element_present("id=tag-cloud-box"))
            sel.click("xpath=//ul[@id='search-type-options']//span[.='People']")
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
    
globals().update(make_platform_classes.make_platform_classes(TestSearch))