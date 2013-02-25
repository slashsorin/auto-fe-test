#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Nov 19, 2012
'''     
import sys, time, os, unittest
from selenium import selenium
import Parameters as tParams
import Constants as ct
import io, json
import WebKit
from selenium import webdriver

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestAbout(SeleniumTestCase.SeleniumTestCase):
    
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*firefox", "http://local.tissuu.com:8080")
        self.selenium.start()
        
    def test_about(self):
        try:
            sel = self.selenium
            sel.open("/about")
            sel.set_speed("500")    
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
            sel.click("link=Login")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "masteraccount")
            sel.type("id=password", "nbasketball")
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
            #sel.click("link=Logout")
            #sel.wait_for_page_to_load("60000")
            '''
            f = open('cov_result.json', 'w')
            f.write(sel.execute_script("return window.__coverage__;"))
            f.close()
            '''
            #print sel.get_attribute_from_all_windows()
            
            #f = open("results.json", "wb")
            #f.write(str(json.dump(sel.execute_script("window.__coverage__"))))
            print "a?"
            print str(sel.execute_script("window.__coverage__"))
            
            print "aaa???"
            #f.close()
            '''
            with io.open('cov_rez.txt', 'w', encoding='utf-8') as outfile:
                json.dump(sel.execute_script("window.__coverage__"), outfile)
            '''
            print 'xxx'
            
            #print sel.execute_script("return window.location;")
            
            print self.__class__.__name__ + " passed!"
            
        except AttributeError:
            pass   
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                print self.__class__.__name__ + " failed!"
                
if __name__ == '__main__':
    unittest.main()