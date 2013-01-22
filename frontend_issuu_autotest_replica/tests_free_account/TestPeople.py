import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestPeople(SeleniumTestCase.SeleniumTestCase):
    
    def test_people(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/people")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("id=people"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[3]/div[2]/div[1]"))
            sel.click("link=United States")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='people']/div[1]/p[1]"))
            self.failUnless(sel.is_element_present("id=input_keywords_sidebar"))
            self.failUnless(sel.is_element_present("id=btn_search_sidebar"))
            self.assertEqual("Issuu - People", sel.get_title())
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_text_present("Find people wizard"))
            sel.click("xpath=//ul[@id='display-grid']//span[.='Text']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='people']/div[1]"))
            sel.type("id=input_keywords_sidebar", "mihai")
            sel.click("id=btn_search_sidebar")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Search", sel.get_title())
            sel.open("/people")
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//form[@id='myForm']/div[2]/a/span[2]")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("id=people"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[3]/div[2]/div[1]"))
            sel.click("link=United States")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='people']/div[1]/p[1]"))
            self.failUnless(sel.is_element_present("id=input_keywords_sidebar"))
            self.failUnless(sel.is_element_present("id=btn_search_sidebar"))
            self.assertEqual("Issuu - People", sel.get_title())
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_text_present("Find people wizard"))
            sel.click("xpath=//ul[@id='display-grid']//span[.='Text']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='people']/div[1]"))
            sel.type("id=input_keywords_sidebar", "mihai")
            sel.click("id=btn_search_sidebar")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - Search", sel.get_title())
            sel.click("link=Logout")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Logout")
                
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
                
globals().update(make_platform_classes.make_platform_classes(TestPeople))