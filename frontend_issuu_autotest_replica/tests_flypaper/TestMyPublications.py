import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

class TestMyPublications(SeleniumTestCase):
    
    def test_my_publications(self):
        try:
            sel = self.selenium
            sel.set_speed("3000")
            sel.open("/explore")
            sel.wait_for_page_to_load("60000")
            sel.click("id=login-link")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("id=login-button")
            #sel.click("xpath=//nav[@class='userstatus']//span[.='sorintest']")
            sel.click("link=My Publications")
            sel.wait_for_page_to_load("60000")
            #sel.click("xpath=//a[@id='acceptButton']//strong[.='I accept the Terms of Service']")
            #sel.wait_for_page_to_load("60000")
            try: self.failUnless(sel.is_element_present("id=main-container"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=logo"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//header/div"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//body/footer"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("xpath=//body/nav"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("link=Home"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("link=Explore"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=input_keywords"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("id=publish-link"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("link=My Feed"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("link=My Publications"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("link=Stacks"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("link=Subscriptions"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_element_present("link=History"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("link=Select all")
            sel.click("link=Select none")
            sel.click("link=Public")
            sel.click("link=Unpublished")
            sel.click("link=Failed")
            sel.click("xpath=//div[@id='ember265']/div[1]")
            sel.click("link=All")
            sel.click("link=My Feed")
            sel.wait_for_page_to_load("60000")
            try: self.assertEqual("My Feed", sel.get_title())
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Stacks")
            sel.wait_for_page_to_load("60000")
            try: self.assertEqual("Stacks", sel.get_title())
            except AssertionError, e: self.verificationErrors.append(str(e))
            sel.click("xpath=//nav[@class='top-nav']//a[.='My Publications']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//nav[@class='userstatus']//span[.='sorintest']")
            sel.click("id=logout-link")
            sel.wait_for_page_to_load("60000")
            try: self.assertEqual("Explore page", sel.get_title())
            except AssertionError, e: self.verificationErrors.append(str(e))
            
            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #print self.__class__.__name__ + " failed!"
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
        
globals().update(make_platform_classes.make_platform_classes(TestMyPublications))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test-reports'))