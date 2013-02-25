from selenium import selenium
import unittest, time, re

class upload(unittest.TestCase):
    
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://flypaper.issuu.com/")
        self.selenium.start()
    
    def test_upload(self):
        sel = self.selenium
        sel.set_speed("5000")
        sel.open("/thenest/docs/spring13")
        sel.wait_for_page_to_load("60000")
        sel.click("id=publish-link")
        sel.click("id=publish-select-btn")
        sel.click("link=Cancel")
        sel.click("id=publish-link")
        sel.click("link=Cancel")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



driver = webdriver.Firefox()
element = driver.find_element_by_id("fileUpload")
element.send_keys("myfile.txt")