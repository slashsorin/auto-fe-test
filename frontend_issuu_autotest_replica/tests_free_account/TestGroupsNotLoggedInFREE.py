import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestGroupsNotLoggedInFREE(SeleniumTestCase.SeleniumTestCase):
    
    def test_groups_not_logged_in(self):
        try:
            sel = self.selenium
            sel.set_speed("500");
            sel.open("/groups")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_text_present("A group is a great way to gather publications and discuss topics inside a closed circle. Simply create a group to get started, or browse and join a group you find interesting."))
            self.failUnless(sel.is_element_present("link=Create new group"))
            sel.click("link=Most active")
            sel.click("link=Most members")
            sel.click("link=New groups")
            sel.click("link=Groups we like")
            self.failUnless(sel.is_element_present("id=groups-module-content-groups-explore"))
            self.failUnless(sel.is_element_present("id=groups-module-content-groups-new"))
            self.failUnless(sel.is_element_present("id=groups-main"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='groups-main']/div[2]/div[2]"))
            sel.select("id=filter-category", "Art")
            sel.select("id=groups-top-level-cats", "Bibles (12)")
            sel.select("id=filter-subcategory", "New American Bible")
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("link=Login"))
            self.failUnless(sel.is_element_present("link=Create account"))
            
            #print self.__class__.__name__ + " passed!"
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                #print self.__class__.__name__ + " failed!"
                
globals().update(make_platform_classes.make_platform_classes(TestGroupsNotLoggedInFREE))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))