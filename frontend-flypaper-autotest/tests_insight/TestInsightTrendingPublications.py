import sys, time

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestInsightTrendingPublications(SeleniumTestCase.SeleniumTestCase):

    def test_insight_trending_publications(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/login?onLogin=http%3A%2F%2Finsight.issuu.com%2Fstatistics")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            #self.failUnless(sel.is_element_present("id=ember570"))
            #self.failUnless(sel.is_element_present("xpath=//div[@id='ember570']//h2[.='Trending publications']"))
            self.failUnless(sel.is_element_present("xpath=//table[@class='doc-list']/thead/tr/th[1]/div"))
            self.failUnless(sel.is_element_present("xpath=//th[@class='publication-date']/div"))
            self.failUnless(sel.is_element_present("xpath=//th[@class='reads']/div"))
            self.failUnless(sel.is_element_present("xpath=//th[@class='impressions']/div"))
            self.failUnless(sel.is_element_present("xpath=//th[@class='avg-time-spent']/div"))
            self.failUnless(sel.is_element_present("xpath=//th[@class='performance']/div"))
            sel.click("xpath=//table[@class='doc-list']/thead/tr/th[1]/div")
            sel.click("xpath=//th[@class='publication-date']/div")
            sel.click("xpath=//th[@class='reads']/div")
            sel.click("xpath=//th[@class='impressions']/div")
            sel.click("xpath=//th[@class='avg-time-spent']/div")
            sel.click("xpath=//th[@class='performance']/div")
            sel.click("xpath=//th[@class='avg-time-spent']/div")
            sel.click("xpath=//th[@class='impressions']/div")
            sel.click("xpath=//th[@class='reads']/div")
            sel.click("xpath=//th[@class='publication-date']/div")
            sel.click("xpath=//table[@class='doc-list']/thead/tr/th[1]/div")
            self.failUnless(sel.is_element_present("link=Show all publications"))
            #sel.mouse_over("xpath=//table[@class='doc-list']/tbody/tr[3]/td[1]/a")
            #self.failUnless(sel.is_element_present("xpath=//div[@class='tipsy-inner']/img"))
        
            print self.__class__.__name__ + " passed!"       
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
                
globals().update(make_platform_classes.make_platform_classes(TestInsightTrendingPublications))