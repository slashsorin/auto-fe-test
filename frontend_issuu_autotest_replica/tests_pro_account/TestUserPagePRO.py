import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

import unittest, xmlrunner

class TestUserPagePRO(SeleniumTestCase.SeleniumTestCase):
        
    def test_user_page(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/PROaccount")
            sel.wait_for_page_to_load("60000")
            sel.click("link=See all")
            sel.wait_for_page_to_load("60000")
            self.assertEqual("Issuu - proaccount - Documents", sel.get_title())
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='user-profile']/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='user-profile']/div[2]"))
            sel.click("xpath=//div[@id='user-friends']//a[.='See all']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=See all")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("id=documents-count")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("id=bookmarks-made-count")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "proaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='box-padding']//p[.='About me text missing Add now']"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='user-photo']/img"))
            self.failUnless(sel.is_element_present("id=comment"))
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Post']")
            sel.type("id=comment", "test post !!!")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Post']")
            sel.click("xpath=//a[@id='comment-post']/span[3]")
            sel.click("id=comment")
            sel.click("link=Logout")
            sel.wait_for_page_to_load("60000")
            
            #print self.__class__.__name__ + " passed!"
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                #print self.__class__.__name__ + " failed!"

globals().update(make_platform_classes.make_platform_classes(TestUserPagePRO))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))