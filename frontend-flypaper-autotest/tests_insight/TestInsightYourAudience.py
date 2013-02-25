import sys, time

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestInsightYourAudience(SeleniumTestCase.SeleniumTestCase):
    
    def test_insight_your_audience(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/login?onLogin=http%3A%2F%2Finsight.issuu.com%2Fstatistics")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("xpath=//form[@id='myForm']/div[2]/a/span[2]")
            sel.wait_for_page_to_load("60000")
            #self.failUnless(sel.is_element_present("id=ember612"))
            self.failUnless(sel.is_text_present("Your audience around the world"))
            #self.failUnless(sel.is_element_present("xpath=//div[@id='ember612']/div[2]/div[1]"))
            #self.failUnless(sel.is_element_present("xpath=//div[@id='ember612']/div[2]/div[2]"))
            #self.failUnless(sel.is_element_present("xpath=//div[@id='ember612']/div[2]/div[3]"))
            self.failUnless(sel.is_text_present("Top 5 countries"))
            self.failUnless(sel.is_text_present("Top traffic sources"))
            self.failUnless(sel.is_text_present("Keywords"))
            sel.click("xpath=//div[@id='geo-map']//div[.='+']")
            sel.click("xpath=//div[@id='geo-map']//div[.='+']")
            #sel.click(u"xpath=//div[@id='geo-map']//div[.='-']")
            #sel.click(u"xpath=//div[@id='geo-map']//div[.='-']")
    
            print self.__class__.__name__ + " passed!"       
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"

globals().update(make_platform_classes.make_platform_classes(TestInsightYourAudience))