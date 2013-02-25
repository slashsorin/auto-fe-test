import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestDocInfoPagePro(SeleniumTestCase.SeleniumTestCase):

    def test_doc_info_page_pro(self):
        try:
            sel = self.selenium
            sel.set_speed("700")
            sel.open("/PROaccount/docs/automatedtest_doc/1")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=top-menubar-bg-color"))
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            self.failUnless(sel.is_element_present("id=top_search_form"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='issuu-viewer-spread']/div[2]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='comments']/form/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='main-outer']/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='related-docs']/div[3]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.assertEqual("auto test", sel.get_title())
            sel.click("id=tab-articles")
            sel.click("id=tab-stats")
            sel.click("id=tab-articles")
            sel.click("id=tab-stats")
            sel.click("id=tab-comments")
            sel.click("link=Log in")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "PROaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//form[@id='myForm']/div[2]/a/span[2]")
            sel.wait_for_page_to_load("60000")
            for i in range(60):
                try:
                    if sel.is_element_present("id=comment"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            sel.click("id=comment")
            sel.type("id=comment", "Nice cover!")
            sel.click("id=send-form")
            self.failUnless(sel.is_element_present("xpath=//div[@id='comments-list']/div/div[2]"))
            self.failUnless(sel.is_element_present("id=send-form"))
            self.failUnless(sel.is_element_present("id=tab-articles"))
            self.failUnless(sel.is_element_present("id=tab-comments"))
            self.failUnless(sel.is_element_present("id=author-edit"))
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestDocInfoPagePro))
