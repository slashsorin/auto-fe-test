import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestFlagDocumentFREE(SeleniumTestCase.SeleniumTestCase):

    def test_flag_document(self):
        try:
            sel = self.selenium
            sel.open("/login?onLogin=http%3A%2F%2Fissuu.com%2Fflag%2Fdocument")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='flag']/ul"))
            self.failUnless(sel.is_text_present("Sexual or pornographic"))
            self.failUnless(sel.is_text_present("Violent or repulsive"))
            self.failUnless(sel.is_text_present("Hateful or abusive"))
            self.failUnless(sel.is_text_present("Spam"))
            self.failUnless(sel.is_element_present("xpath=//form[@id='myForm']/div/a/span[2]"))
            self.failUnless(sel.is_text_present("Document flagging"))
            sel.click("xpath=//ul[@class='radioHolder']//label[.='Hateful or abusive']")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']/strong")
            
            #print self.__class__.__name__ + " passed!"
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                #print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestFlagDocumentFREE))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))
