import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestGroupsPrivateLoggedInFree3(SeleniumTestCase.SeleniumTestCase):

    def test_groups_private_logged_in_free3(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/groups/testgroupprivate1")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_text_present("Sorry, this is a private group"))
            self.failUnless(sel.is_text_present("Moderated by PROaccount"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "PROaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            sel.set_speed("500")
            sel.click("link=Comment title!")
            sel.set_speed("500")
            sel.set_timeout("500")
            sel.click("link=Delete this discussion")
            sel.click("link=Delete discussion")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Group settings")
            self.failUnless(sel.is_element_present("xpath=//td[@class='c7']/div"))
            sel.type("id=group-name", "test private 123")
            sel.type("id=group-description", "Private group for testing on SauceLabs! Test! Test! Test!")
            sel.select("id=group-category", "Computers")
            sel.select("id=group-subcategory", "Internet")
            sel.click("link=Apply changes")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("link=test private 123"))
            sel.click("link=Group settings")
            sel.click("id=group-edit-graphics")
            self.failUnless(sel.is_element_present("xpath=//div[@id='group-edit-graphics-tab']/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='group-edit-graphics-tab']/div[2]"))
            sel.click("id=group-edit-theme")
            sel.click("xpath=//div[@id='group-edit-theme-tab']/a[6]/img")
            sel.click("link=Save changes")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Group settings")
            sel.click("id=group-edit-url")
            sel.type("id=group-url", "testgroupprivate1")
            sel.click("xpath=//div[@id='group-edit-url-tab']//a[.='Save changes']")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Group settings")
            sel.click("id=group-edit-membership")
            sel.click("id=group-edit-delete")
            sel.click("xpath=//div[@class='dia_box']/div")
            sel.click("link=Invite a friend")
            self.failUnless(sel.is_element_present("xpath=//div[@id='group-invite-members-inner']/form"))
            self.failUnless(sel.is_text_present("Invite these people"))
            sel.click("xpath=//div[@class='dia_box']/div")
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestGroupsPrivateLoggedInFree3))