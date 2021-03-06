import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestFindPeople(SeleniumTestCase.SeleniumTestCase):

    def test_find_people(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/findpeople")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "nbasketball")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=logoList"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='chooseMarkup']/div[3]/img"))
            self.failUnless(sel.is_element_present("xpath=//span[@class='system-blue-shade-fat-btn-text']/strong"))
            self.assertEqual("Issuu - Find people", sel.get_title())
            self.failUnless(sel.is_text_present("Add friends manually"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_text_present("Find people you know"))
            
            print self.__class__.__name__ + " passed!"       
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
           
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestFindPeople))
