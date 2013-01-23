import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestCreateGroups(SeleniumTestCase.SeleniumTestCase):
    
    def test_create_groups(self):
        try:
            sel = self.selenium
            sel.open("/groups")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Create new group")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "PROaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Create new group")
            sel.type("id=group-name", "test group")
            sel.type("id=group-description", "test group description!")
            self.failUnless(sel.is_element_present("id=group-description"))
            self.failUnless(sel.is_element_present("id=group-name"))
            self.failUnless(sel.is_element_present("id=group-category"))
            self.failUnless(sel.is_element_present("id=group-subcategory"))
            sel.select("id=group-category", "Computers")
            sel.select("id=group-subcategory", "User Interfaces")
            sel.click("link=Done, create group")
            self.failUnless(sel.is_text_present("The description must be 30 - 1000 characters long."))
            sel.type("id=group-description", "test group description for this test group!!!!!!")
            sel.click("link=Done, create group")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=group-edit"))
            sel.click("id=group-edit-graphics")
            self.failUnless(sel.is_element_present("xpath=//div[@id='group-edit-graphics-tab']/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='group-edit-graphics-tab']/div[2]"))
            sel.click("id=group-edit-theme")
            sel.click("xpath=//div[@id='group-edit-theme-tab']/a[1]/img")
            sel.click("xpath=//div[@id='group-edit-theme-tab']/a[3]/img")
            sel.click("id=group-edit-url")
            sel.click("id=group-edit-membership")
            sel.check("id=group-access-private")
            sel.click("xpath=//div[@id='group-edit-membership-tab']//a[.='Save changes']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=groups-main"))
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
    
globals().update(make_platform_classes.make_platform_classes(TestCreateGroups))
