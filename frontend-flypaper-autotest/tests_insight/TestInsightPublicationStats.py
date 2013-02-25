import sys, time

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestInsightPublicationStats(SeleniumTestCase.SeleniumTestCase):

    def test_insight_publication_stats(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/login?onLogin=http%3A%2F%2Finsight.issuu.com%2Fstatistics")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            #self.failUnless(sel.is_element_present("xpath=//div[@id='ember267']/div[3]"))
            #self.failUnless(sel.is_element_present("id=ember478"))
            #self.failUnless(sel.is_element_present("xpath=//span[@id='ember509']//span[.='Mobile']"))
            #self.failUnless(sel.is_element_present("xpath=//span[@id='ember520']//span[.='Desktop']"))
            #self.failUnless(sel.is_element_present("xpath=//div[@id='ember478']/div[2]/div[2]/div[1]"))
            #self.failUnless(sel.is_element_present("xpath=//div[@id='ember478']/div[2]/div[2]/div[2]"))
            #self.failUnless(sel.is_element_present("id=ember548"))
            #self.failUnless(sel.is_element_present("id=ember486"))
            sel.click("id=ember486")
            sel.click("xpath=//div[@id='ember486']//li[normalize-space(.)='Impressions']")
            sel.click("id=ember486")
            sel.click("xpath=//div[@id='ember486']/ul/li[3]")
            sel.click("id=ember486")
            sel.click("xpath=//div[@id='ember486']//li[normalize-space(.)='Downloads']")
            sel.mouse_over("xpath=//span[@id='ember509']/div")
            sel.mouse_over("xpath=//span[@id='ember520']/div")
    
            print self.__class__.__name__ + " passed!"       
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"

globals().update(make_platform_classes.make_platform_classes(TestInsightPublicationStats))