import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

class TestStacks(SeleniumTestCase):

    def test_stacks(self):
        try:
            sel = self.selenium
            sel.set_speed("2000")
            sel.open("https://issuu.com/signin?onLogin=http%3A%2F%2Fissuu.com%2Fhome%2Fpublications")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("id=login-button")
            sel.wait_for_page_to_load("60000")
            sel.click("link=Stacks")
            sel.wait_for_page_to_load("60000")
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='main-container']/section"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//div[@id='main-container']/div/nav"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//nav[@class='left-nav']//button[.='Edit']"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("xpath=//nav[@class='left-nav']//button[.='Edit']")
            sel.click("xpath=//div[@id='main-container']//button[.='Done']")
            try: self.failUnless(sel.is_element_present("xpath=//nav[@class='left-nav']/ul"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("link=New stack"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("xpath=//nav[@class='left-nav']//button[.='Edit']")
            sel.click("xpath=//div[@id='main-container']//button[.='Done']")
            sel.click("link=New stack")
            sel.type("id=itemcreator", "Test stack :)")
            sel.click("xpath=//a[@class='access']//span[.='C']")
            sel.click("link=Public stack")
            sel.click("link=C")
            sel.click("link=Secret stack")
            sel.click("xpath=//a[@class='access']//span[.='L']")
            sel.click("link=Public stack")
            sel.click("xpath=//nav[@class='left-nav']//button[.='Edit']")

            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #print self.__class__.__name__ + " failed!"
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
        
globals().update(make_platform_classes.make_platform_classes(TestStacks))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test-reports'))