import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

import unittest, xmlrunner

class TestBusinessFREE(SeleniumTestCase.SeleniumTestCase):

    def test_business(self):
        try:
            sel = self.selenium
            sel.set_speed("1000")
            sel.open("/business")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[2]/div[11]/object/embed"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='uploadbutton']/a/img"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[3]/div[2]"))
            sel.click("xpath=//div[@class='page-wrapper']/div[2]/div[3]/div[2]")
            sel.click("xpath=//div[@class='page-wrapper']/div[2]/div[3]/div[2]/div[4]/div[1]/table/tbody/tr[4]/td/div/a/span[2]")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//div[@class='page-wrapper']/div[2]/div[3]/div[2]/div[4]/div[2]/table/tbody/tr[4]/td/div/a/span[2]")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("link=Marketers")
            sel.click("link=Advertisers")
            sel.click("xpath=//div[@class='page-wrapper']//a[.='Resellers']")
            #sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Features']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Resellers']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Pricing']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='FAQ']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Cases']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Sign up']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//form[@id='myForm']/div[2]/a/span[2]")
            sel.wait_for_page_to_load("60000")
            #self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[2]/div[11]/object/embed"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='uploadbutton']/a/img"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='page-wrapper']/div[2]/div[3]/div[2]"))
            sel.click("link=Marketers")
            sel.click("link=Advertisers")
            sel.click("xpath=//div[@class='page-wrapper']//a[.='Resellers']")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Features']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Resellers']")
            sel.wait_for_page_to_load("60000")
            sel.go_back()
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='FAQ']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//ul[@class='horizontal-listBiz']//strong[.='Cases']")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("id=top-menubar-container"))
            sel.click("link=Logout")
            sel.wait_for_page_to_load("60000")
                
            #print self.__class__.__name__ + " passed!"
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
        
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                #print self.__class__.__name__ + " failed!"
           
globals().update(make_platform_classes.make_platform_classes(TestBusinessFREE))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test_reports'))