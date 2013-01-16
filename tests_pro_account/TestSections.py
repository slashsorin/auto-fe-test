import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

class TestSections(SeleniumTestCase.SeleniumTestCase):
        
    def test_sections(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/login?onLogin=http%3A%2F%2F" + cfg.config['base-url'] + "%2Fsections")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "PROaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_text_present("My subscriptions"))
            self.failUnless(sel.is_text_present("New documents"))
            self.failUnless(sel.is_text_present("Popular documents"))
            self.failUnless(sel.is_text_present("Friends documents"))
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_text_present("Options"))
            sel.click("link=Options")
            sel.click("link=Text on/off")
            self.failUnless(sel.is_element_present("id=sections-infobox-inner"))
            sel.click("id=hide-icon")
            sel.click("xpath=//span[@class='system-grey-shade-fat-btn-text']//strong[.='What is Sections']")
            self.failUnless(sel.is_element_present("id=embedVideo"))
            sel.click("xpath=//div[@class='dia_box']/div")
            sel.click("xpath=//div[@class='system-blue-btn-dropdown']//span[.='Add sections']")
            sel.click("xpath=//a[@class='newcustom']//span[.='+ New custom section']")
            self.failUnless(sel.is_element_present("id=flash_issuu"))
            sel.click("xpath=//div[@class='dia_box']/div")
            sel.click("xpath=//a[@id='section1000000000000000']//span[.='Popular documents']")
            sel.click("link=Logout")
            sel.wait_for_page_to_load("60000")
            sel.wait_for_page_to_load("60000")
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
                
globals().update(make_platform_classes.make_platform_classes(TestSections))