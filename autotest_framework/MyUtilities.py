#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jun 1, 2012
'''
from selenium import selenium
import Parameters as tParams
import Constants as ct

def setUp1(self):
    self.verificationErrors = []
    self.selenium = selenium("saucelabs.com",
                                 4444,
                                 "{\"username\": \"" + ct.USER_NAME + 
                                    "\",\"access-key\":\"" + ct.ACCESS_KEY + 
                                    "\",\"browser\": \"" + ct.TEST_BROWSER + 
                                    "\",\"job-name\":\"" + self.__class__.__name__ +
                                    "\",\"max-duration\":\"" + ct.MAX_DURATION +
                                    "\",\"record-video\":\"" + ct.RECORD_TEST + 
                                    "\",\"os\":\"" + ct.OS + 
                                    "\",\"public\":\"" + ct.TEST_PRIVATE + 
                                    #"\",\"build\":\"" + ct.BUILD_NUMBER + 
                                    #"\",\"tags\":\"" + ct.TAGS + 
                                    #"\",\"custom-data\":\"" + ct.CUSTOM_DATA + 
                                    #"\",\"video-upload-on-pass\":\"" + ct.VIDEO_UPLOAD_ON_PASS +
                                    #"\",\"record-screenshots\":\"" + ct.RECORD_SCREENSHOTS + 
                                    "\"}",
                                    "http://issuu.com/")
    self.selenium.start()
    self.selenium.set_timeout(90000)
    
def setUp2(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4445, "*firefoxproxy", "http://issuu.com/")
        self.selenium.start()
        
def setUp3(self):
        tp = tParams.GetParams()
        
        if tp.place.find("sauce") > -1:
            
            self.verificationErrors = []
            self.selenium = selenium(ct.DOMAIN, ct.PORT,
                                    "{\"username\": \"" + ct.USER_NAME + 
                                    "\",\"access-key\":\"" + ct.ACCESS_KEY + 
                                    "\",\"browser\": \"" + tp.test_browser + 
                                    "\",\"job-name\":\"" + self.__class__.__name__ + 
                                    "\",\"max-duration\":\"" + ct.MAX_DURATION +
                                    "\",\"record-video\":\"" + ct.RECORD_TEST + 
                                    "\",\"os\":\"" + ct.OS + 
                                    "\"}", 
                                    tp.run_domain)
            self.selenium.start()
        else:
            if tp.place.find("local") > -1  :
                self.verificationErrors = []
                tp = tParams.GetParams()
            if tp.test_browser.find("*firefox"):
                tp.test_browser = tParams.GetParams().test_browser
            if tp.run_domain.find("http://issuu.com"):
                tp.run_domain = tParams.GetParams().run_domain
            self.selenium = selenium("localhost", 4444, tp.test_browser, tp.run_domain)
            self.selenium.start()