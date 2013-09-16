#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

class TestNewServices(SeleniumTestCase):
   
    def test_new_services(self):
        try:
            sel = self.selenium
	        sel.open("/signin?onLogin=https%3A%2F%2Fissuu.com%2Fhome%2Fservices")
	        sel.wait_for_page_to_load("60000")
	        sel.type("id=login-password", "testservices")
	        sel.click("id=login-button")
	        sel.click("xpath=//div[@id='main-container']/div[2]/div/div[2]/section/div/div[2]/div[1]/label/div[3]/span[1]")
	        sel.check("id=plus")
	        sel.click("xpath=//div[@class='fixer']/section[1]/button")
	        self.failUnless(sel.is_element_present("xpath=//div[@id='overlay']/div[3]/div/div/section"))
	        self.failUnless(sel.is_element_present("xpath=//div[@id='overlay']//button[normalize-space(.)='Cancel']"))
	        sel.click("xpath=//div[@id='overlay']//button[normalize-space(.)='Cancel']")
	        sel.click("xpath=//div[@id='main-container']//div[.='$39/mo']")
	        sel.check("id=premium")
	        sel.check("id=100")
	        sel.check("id=500")
	        sel.check("id=1500")
	        sel.check("id=25")
	        sel.check("xpath=//div[@class='products']/section[2]/div/div/label[1]/input")
	        sel.check("xpath=//div[@class='products']/section[2]/div/div/label[2]/input")
	        sel.check("xpath=//div[@class='products']/section[2]/div/div/label[1]/input")
	        sel.check("xpath=//div[@class='products']/section[2]/div/div/label[2]/input")
	        sel.click("link=Show details")
	        sel.click("link=Hide details")
	        sel.click("link=Enter promotion code")
	        sel.type("id=coupon-code", "ceooffer")
	        sel.click("xpath=//form[@id='coupon-field']/div/button")
	        self.failUnless(sel.is_element_present("xpath=//div[@class='fixer']/section[1]/button"))
	        sel.click("xpath=//div[@id='overlay']//button[normalize-space(.)='Cancel']")
	        sel.click("id=logout-link")
	        sel.wait_for_page_to_load("60000")
            
            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #print self.__class__.__name__ + " failed!"
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
        
globals().update(make_platform_classes.make_platform_classes(TestNewServices))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test-reports'))