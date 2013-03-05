from selenium import selenium
import unittest, time, re

class TestBilling(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://flypaper.issuu.com/")
        self.selenium.start()
    
    def test_billing(self):
        sel = self.selenium
        sel.set_speed("2000")
        sel.open("/signin?onLogin=https%3A%2F%2Fflypaper.issuu.com%2Fhome%2Fsettings%2Fbilling")
        sel.wait_for_page_to_load("60000")
        sel.type("id=username", "sorintest")
        sel.type("id=password", "sorintest")
        sel.click("id=loginButton")
        sel.wait_for_page_to_load("60000")
        sel.click("xpath=//a[@id='acceptButton']//strong[.='I accept the Terms of Service']")
        sel.wait_for_page_to_load("60000")
        try: self.failUnless(sel.is_element_present("xpath=//div[@id='main-container']//section[normalize-space(.)='Account summary']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("xpath=//div[@id='main-container']/section[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("xpath=//div[@id='main-container']/section[3]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("xpath=//div[@id='main-container']/section[4]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("xpath=//body/nav"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("xpath=//body/header"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("xpath=//footer/div"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
