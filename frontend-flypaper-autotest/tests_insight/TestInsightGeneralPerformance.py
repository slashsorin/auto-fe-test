import sys, time

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestInsightGeneralPerformance(SeleniumTestCase.SeleniumTestCase):

    def test_insight_general_performance(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/login?onLogin=http%3A%2F%2Finsight.issuu.com%2Fstatistics")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//div[@id='preview-impressions']/div[1]/div[1]")
            sel.click("xpath=//div[@id='preview-timeSpent']/div[1]/div[1]")
            sel.click("xpath=//div[@id='preview-downloads']/div[1]/div[1]")
            sel.click("xpath=//div[@id='preview-reads']//div[.='Reads']")
            sel.click("xpath=//div[@class='selectedMetric']//div[.='Reads']")
            sel.click("xpath=//div[@id='preview-impressions']//div[.='Impressions']")
            sel.click("xpath=//div[@class='selectedMetric']//div[.='Impressions']")
            sel.click("xpath=//div[@id='preview-timeSpent']//div[.='Average Time Spent']")
            sel.click("xpath=//div[@class='selectedMetric']//div[.='Average Time Spent']")
            sel.click("xpath=//div[@id='preview-downloads']//div[.='Downloads']")
            sel.click("xpath=//div[@class='selectedMetric']//div[.='Downloads']")
            #self.failUnless(sel.is_element_present("id=ember339"))
            self.failUnless(sel.is_element_present("id=preview-reads"))
            self.failUnless(sel.is_element_present("id=preview-impressions"))
            self.failUnless(sel.is_element_present("id=preview-timeSpent"))
            self.failUnless(sel.is_element_present("id=preview-downloads"))
            #self.failUnless(sel.is_element_present("xpath=//div[@id='ember339']//h3[.='All publications']"))
            #self.failUnless(sel.is_element_present("xpath=//div[@id='ember339']//h2[.='General performance']"))
            
            print self.__class__.__name__ + " passed!"       
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"

globals().update(make_platform_classes.make_platform_classes(TestInsightGeneralPerformance))
    