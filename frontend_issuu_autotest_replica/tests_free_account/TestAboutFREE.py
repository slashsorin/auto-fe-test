import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

class TestAboutFREE(SeleniumTestCase):
    
    def test_about(self):
        try: 
            sel = self.selenium
            sel.open("/about")
            sel.set_speed("500")    
            self.failUnless(sel.is_element_present("id=coverflow-mask"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='index']/div[1]/h1"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='index']/div[2]/div[2]/img"))
            self.failUnless(sel.is_element_present("xpath=//a[@id='popinMobile']/img"))
            sel.click("xpath=//a[@id='popinMobile']/abcdef")
            for i in range(60):
                try:
                    if sel.is_element_present("xpath=//div[@class='dia_box']/div"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            #self.failUnless(sel.is_element_present("xpath=//div[1]/div/object"))
            sel.click("xpath=//div[@class='dia_box']/div")
            self.failUnless(sel.is_element_present("xpath=//div[@id='index']/table[1]/tbody/tr/td[3]/img"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='index']/table[2]/tbody/tr/td[3]/a/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[7]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[7]/div[2]/div/div/a/span"))
            sel.mouse_over("xpath=//div[@id='footerText']/div[7]/div[2]/div/div/a/span")
            self.failUnless(sel.is_element_present("xpath=//div[4]/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[1]/p"))
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "FREEaccount")
            sel.type("id=password", "autotest")
            sel.click("xpath=//form[@id='myForm']/div[2]/a/span[2]")
            sel.wait_for_page_to_load("60000")
            self.failUnless(sel.is_element_present("id=coverflow-mask"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='index']/div[1]/h1"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='index']/div[2]/div[2]/img"))
            self.failUnless(sel.is_element_present("xpath=//a[@id='popinMobile']/img"))
            sel.click("xpath=//a[@id='popinMobile']/img")
            for i in range(60):
                try:
                    if sel.is_element_present("xpath=//div[@class='dia_box']/div"): break
                except: pass
                time.sleep(1)
            else: self.fail("time out")
            #self.failUnless(sel.is_element_present("xpath=//div[1]/div/object"))
            sel.click("xpath=//div[@class='dia_box']/div")
            self.failUnless(sel.is_element_present("xpath=//div[@id='index']/table[1]/tbody/tr/td[3]/img"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='index']/table[2]/tbody/tr/td[3]/a/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='footer']/div"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[7]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[7]/div[2]/div/div/a/span"))
            sel.mouse_over("xpath=//div[@id='footerText']/div[7]/div[2]/div/div/a/span")
            self.failUnless(sel.is_element_present("xpath=//div[4]/div[1]"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='footerText']/div[1]/p"))
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
    
globals().update(make_platform_classes.make_platform_classes(TestAboutFREE))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))