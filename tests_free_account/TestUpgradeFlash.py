import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestUpgradeFlash(SeleniumTestCase.SeleniumTestCase):
    
    def test_upgrade_flash(self):
        try:
            sel = self.selenium
            sel.open("/upgrade_flash")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//html"))
            self.failUnless(sel.is_element_present("xpath=//table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td"))
            self.failUnless(sel.is_element_present("xpath=//table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td"))
            self.failUnless(sel.is_element_present("xpath=//table/tbody/tr[1]/td[2]/table/tbody/tr[3]/td"))
            self.failUnless(sel.is_element_present("xpath=//table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/p"))
            self.failUnless(sel.is_text_present("You need to update your Flash player."))
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
                
globals().update(make_platform_classes.make_platform_classes(TestUpgradeFlash))