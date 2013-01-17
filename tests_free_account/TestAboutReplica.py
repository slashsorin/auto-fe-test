from selenium import selenium
import unittest, time, re
import xmlrunner

class TestAbout(unittest.TestCase):
    
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("ondemand.saucelabs.com", 
                                 80, 
                                 "{\"username\": \"issuu\",\"access-key\":\"23a5b32a-6ab8-4866-8f1d-9a13c98348c2\",\"browser\": \"firefox\",\"browser-version\":\"18\",\"job-name\":\"TestAbout\",\"max-duration\":1800,\"record-video\":true,\"user-extensions-url\":\"\",\"os\":\"Windows 2012\"}", 
                                 "http://issuu.com/")
        self.selenium.start()
        
    def test_about(self):
        sel = self.selenium
        sel.open("/about")
        sel.set_speed("300")
        self.failUnless(sel.is_element_present("id=coverflow-mask"))
        self.failUnless(sel.is_element_present("xpath=//div[@id='index']/div[1]/h1"))
        self.failUnless(sel.is_element_present("xpath=//div[@id='index']/div[2]/div[2]/img"))
        self.failUnless(sel.is_element_present("xpath=//a[@id='popinMobile']/img"))
        sel.click("xpath=//a[@id='popinMobile']/adad")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
