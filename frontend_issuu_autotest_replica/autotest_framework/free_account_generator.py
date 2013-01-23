from selenium import selenium
import unittest, time, re

import random

class free_account_generator(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*firefox", "https://saucelabs.com/")
        self.selenium.start()
    
    def test_free_account_generator(self):
        
        rands = random.randint(1, 1000000)*random.randint(1, 1000000)
        
        sel = self.selenium
        sel.set_speed("1000")
        sel.open("/")
        sel.wait_for_page_to_load("60000")
        sel.click("link=Signup")
        sel.wait_for_page_to_load("60000")
        sel.type("id=email", "svd+%s@issuu.com" % (rands))
        sel.type("id=username", "sorin%s" % (rands))
        sel.type("id=password", "sorin%s" % (rands))
        sel.click("id=signup_submit")
        sel.wait_for_page_to_load("60000")
        sel.click("xpath=//div[@class='scoutIntro']/div[1]/form/input[1]")
        sel.click("xpath=//div[2]/div[1]/a/span")
        sel.click("id=accountTab")
        sel.click("xpath=//a[@id='viewAPIKeyLink']/img")
        sel.click("name=clippy")
        akey = sel.get_text("xpath=//span[@id='access-key']/tt")
        sel.click("link=Logout")
        sel.wait_for_page_to_load("60000")

        print akey
        print "sorin%s" % (rands)
        return (akey, rands)
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)
    
if __name__ == "__main__":
    unittest.main()
