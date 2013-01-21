import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts
import cfg

import unittest, xmlrunner

class TestMobileIssuuApps(SeleniumTestCase.SeleniumTestCase):
    
    def test_mobile_issuu_apps(self):
        try:
            sel = self.selenium
            sel.open("http://m." + cfg.config['base-url'] + "/apps/")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@id='logoTouchArea']/a/img"))
            self.failUnless(sel.is_element_present("xpath=//body/div[4]"))
            self.failUnless(sel.is_element_present("xpath=//body/div[6]"))
            self.failUnless(sel.is_element_present("xpath=//div[6]/img[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[6]/img[2]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='bigImageWrapper']/div"))
            self.failUnless(sel.is_text_present("EasyRead for superb reading"))
            self.failUnless(sel.is_element_present("link=Install"))
            self.failUnless(sel.is_element_present("link=Support"))
            
            print self.__class__.__name__ + " passed!"       
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
           
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestMobileIssuuApps))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))