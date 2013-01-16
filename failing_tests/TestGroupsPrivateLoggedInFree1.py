import sys
import SetTestStatus as sts
import make_platform_classes, SeleniumTestCase

class TestGroupsPrivateLoggedInFree1(SeleniumTestCase.SeleniumTestCase):
    
    def test_groups_private_logged_in_free1(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/groups/testgroupprivate1")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_text_present("Sorry, this is a private group"))
            self.failUnless(sel.is_text_present("Moderated by FREEaccount"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("link=test private 123"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='groups-main']/div[2]/div[2]"))
            self.failUnless(sel.is_element_present("id=group-discussions"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='groups-module-content-group-discussions']/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("id=top-menubar"))
            sel.click("id=top-menubar")
            sel.click("link=Add something")
            self.failUnless(sel.is_element_present("xpath=//td[@class='c7']/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='group-add-item-form-inner']/div"))
            self.failUnless(sel.is_element_present("id=group-add-item-publication"))
            self.failUnless(sel.is_element_present("id=group-add-item-comment"))
            self.failUnless(sel.is_element_present("link=Add to group"))
            sel.type("id=item-title", "Comment title!")
            sel.type("id=item-comment", "Comment body!")
            sel.select("id=item-publication-mypubs", "2 pages")
            self.failUnless(sel.is_element_present("xpath=//div[@id='group-add-item-publication']//p[.='2 pagesPage 1Page 2 Remove']"))
            sel.click("xpath=//div[@id='group-add-item-publication']//p[.='2 pagesPage 1Page 2 Remove']")
            self.failUnless(sel.is_element_present("xpath=//div[@id='item-smiley-box']/p[1]/a[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='item-smiley-box']/p[2]"))
            sel.click("link=Add to group")
            sel.wait_for_page_to_load("60000")
        
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
                
globals().update(make_platform_classes.make_platform_classes(TestGroupsPrivateLoggedInFree1))