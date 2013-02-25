#-*- coding: utf-8 -*-
''' 
    @author: Sorin

    Copyright Issuu Aps Dec 10, 2012
'''

import unittest, sys
from selenium import webdriver

import SetTestStatus as sts
#import wd.parallel

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        '''
        desired_capabilities = []

        browser = copy.copy(webdriver.DesiredCapabilities.IPAD)
        browser['version'] = '5.1'
        browser['platform'] = 'MAC 10.8'
        browser['name'] = 'IPAD 5.1'
        browser['tags'] = "Parallel IPAD 5.1"
        desired_capabilities += [browser]

        browser = copy.copy(webdriver.DesiredCapabilities.IPAD)
        browser['version'] = '4.3'
        browser['platform'] = '10.6'
        browser['name'] = 'IPAD 4.3'
        browser['tags'] = "Parallel IPAD 4.3"
        desired_capabilities += [browser]

        self.drivers = wd.parallel.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://issuu_express:18a93bc3-9231-4147-a47d-21ac733c71e6@ondemand.saucelabs.com:80/wd/hub"
        )
        '''
        desired_capabilities = webdriver.DesiredCapabilities.IPAD
        desired_capabilities['version'] = '5'
        desired_capabilities['platform'] = 'MAC 10.6'
        desired_capabilities['name'] = 'Testing Selenium 2 in Python at Sauce'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://10.0.10.105:3001/wd/hub"
            #command_executor="http://issuu_express:18a93bc3-9231-4147-a47d-21ac733c71e6@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)
        
    #@wd.parallel.multiply
    def test_issuu(self):
        try:
            self.driver.get("http://issuu.com")
            
            searchElement = self.driver.find_element_by_name("q")
            searchElement.send_keys("cars")
            searchElement.submit()
            
            self.driver.get("http://issuu.com/login?onLogin=/explore")
            usernameElement = self.driver.find_element_by_name("username")
            usernameElement.send_keys("sorintest")
            passwordElement = self.driver.find_element_by_name("password")
            passwordElement.send_keys("sorintest")
            passwordElement.submit()
            
            self.driver.implicitly_wait(3)
            
            searchElement = self.driver.find_element_by_name("q")
            searchElement.send_keys("playboy")
            searchElement.submit()
            
            logoutElement = self.driver.find_elemen
            logoutElement.submit()
            
            print self.__class__.__name__ + " passed!"       
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
  
    #@wd.parallel.multiply
    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()