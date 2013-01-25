import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestPrintNotLoggedInFREE(SeleniumTestCase.SeleniumTestCase):

    def test_print_not_logged_in(self):
        try:
            sel = self.selenium
            sel.set_speed("1000")
            sel.open("/sorintest/docs/dev_sauce_ondemand_service#print")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=print-overlay"))
            self.failUnless(sel.is_element_present("xpath=//a[@id='print-document-disabled']//strong[.='Print publication']"))
            #self.failUnless(sel.is_element_present("id=pod-img"))
            self.failUnless(sel.is_text_present("Print this publication"))
            #self.failUnless(sel.is_text_present("Get a beautiful quality print delivered right to your door"))
            
            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
           
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                #print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestPrintNotLoggedInFREE))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))