import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

class TestSearchPage(SeleniumTestCase):

    def test_search_page(self):
        try:
            sel = self.selenium
            sel.open("/explore")
            sel.wait_for_page_to_load("60000")
            sel.click("id=input_keywords")
            sel.type("id=input_keywords", "cars")
            sel.key_press("id=input_keywords", "\\13")
            try: self.failUnless(sel.is_text_present("Publishers"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("Stacks"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("Publications"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='search-result']/div[1]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='search-result']/div[2]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@class='search-result']/div[3]"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//body/footer"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//body/header"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//body/nav"))
            except AssertionError, e: self.verificationErrors.append(str(e))

            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #print self.__class__.__name__ + " failed!"
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
        
globals().update(make_platform_classes.make_platform_classes(TestSearchPage))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test-reports'))