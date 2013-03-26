from selenium import selenium
import unittest, time, re

class TestScrollDown(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://flypaper.issuu.com/")
        self.selenium.start()
    
    def test_scroll_down(self):
        sel = self.selenium
        sel.open("/explore")
        sel.wait_for_page_to_load("60000")
        sel.click("id=main-container")
        sel.click("xpath=//div[@id='main-container']/section")
        sel.key_press("xpath=//div[@id='main-container']/section", "\\40")
        sel.key_down("xpath=//div[@id='main-container']/section", "\\40")
        sel.key_up("xpath=//div[@id='main-container']/section", "\\40")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
