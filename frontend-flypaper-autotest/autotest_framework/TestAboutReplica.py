import unittest, xmlrunner
from selenium import selenium
import cfg, new
import os

class TestAbout(unittest.TestCase):
    
    def setUp(self):
        
        platforms = cfg.config['platforms']
        
        self.verificationErrors = []
        self.selenium = selenium(os.environ.get('SELENIUM_HOST'), 
                                 os.environ.get('SELENIUM_PORT'), 
                                 "{\"username\": \"" + os.environ.get('SAUCE_USER_NAME') + 
                                 "\",\"access-key\":\"" + os.environ.get('SAUCE_API_KEY') +
                                 "\",\"browser\": \"" + os.environ.get('SELENIUM_BROWSER') +
                                 "\",\"browser-version\":\"" + os.environ.get('SELENIUM_VERSION') +
                                 "\",\"os\":\"" + os.environ.get('SELENIUM_PLATFORM') + "\"}", 
                                 "http://issuu.com/")
        self.selenium.start()
        
    def test_about(self):
            sel = self.selenium
            sel.open("/about")
            sel.set_speed("500")    
            self.failUnless(sel.is_element_present("id=coverflow-mask"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='index']/div[1]/h1"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='index']/div[2]/div[2]/img"))
            self.failUnless(sel.is_element_present("xpath=//a[@id='popinMobile']/img"))
            sel.click("xpath=//a[@id='popinMobile']/img")
            '''
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
            '''

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
    
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))