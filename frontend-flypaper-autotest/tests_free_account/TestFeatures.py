import sys, time, os

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestFeatures(SeleniumTestCase.SeleniumTestCase):

    def test_features(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/business/features")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Issuu PRO']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Resellers']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Pricing']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            #sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='How to']")
            #sel.wait_for_page_to_load("60000")
            #sel.go_back()
            #sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='FAQ']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Cases']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Sign up']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='FAQcornerB']/div/div/div/div"))
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[1]/ul"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[5]/div[1]"))
            self.assertEqual("Issuu Pro - Features", sel.get_title())
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Issuu PRO']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Resellers']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Pricing']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            #sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='How to']")
            #sel.wait_for_page_to_load("60000")
            #sel.go_back()
            #sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='FAQ']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Cases']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=top-menubar"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[1]/ul"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[5]/div[1]"))
            self.assertEqual("Issuu Pro - Features", sel.get_title())
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            sel.click("link=Logout")
            sel.wait_for_page_to_load("60000")
            
            print self.__class__.__name__ + " passed!"       
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
           
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestFeatures))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))