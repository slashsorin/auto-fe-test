import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

import unittest, xmlrunner

class TestFlagDocCommentPRO(SeleniumTestCase.SeleniumTestCase):
    
    def test_flag_doc_comment(self):
        try:
            sel = self.selenium
            sel.open("/login?onLogin=http%3A%2F%2F" + cfg.config['base-url'] + "%2Fflag%2Fdoccomment")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "PROaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//form[@id='myForm']/div[2]/a/span[3]")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']//h3[.='Delete document comment']"))
            self.failUnless(sel.is_element_present("xpath=//table[@class='form']/tbody/tr[2]/td"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='commentDeleteReason']/ul"))
            self.failUnless(sel.is_element_present("xpath=//form[@id='myForm']/div/a/span[2]"))
            sel.check("id=spam")
            sel.check("id=harassment")
            sel.check("id=phishing")
            sel.check("id=other")
            sel.check("id=spam")
            sel.check("id=other")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']/strong")
            self.failUnless(sel.is_text_present("Oops, please change something and try again 200"))
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestFlagDocCommentPRO))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))
