import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestGroupsPrivateLoggedInFree2(SeleniumTestCase.SeleniumTestCase):
    
    def test_groups_private_logged_in_free2(self):
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
            sel.wait_for_page_to_load("60000")
            sel.type("id=comment-text", "This is a comment!")
            sel.click("link=Post reply")
            sel.set_speed("500")
            sel.click("link=Add a publication")
            sel.type("id=comment-publication-url", "http://issuu.com/slanted/docs/slanted18")
            sel.type("id=comment-text", "Document reply!")
            sel.click("xpath=//div[@id='comment-smiley-box']/p[1]/a[1]")
            sel.type("id=comment-smiley-text", "Yaba-da-ba-doooo!!!")
            sel.click("link=excited")
            sel.type("id=comment-smiley-text", "Yaba-da-ba-dooo!")
            sel.click("link=Post reply")
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
        
        except AttributeError:
            pass 
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
                
globals().update(make_platform_classes.make_platform_classes(TestGroupsPrivateLoggedInFree2))