import sys, time

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestInsightDatePicker(SeleniumTestCase.SeleniumTestCase):

    def test_insight_date_picker(self):
        try:
            sel = self.selenium
            sel.set_speed("500")
            sel.open("/login?onLogin=http%3A%2F%2Finsight.issuu.com%2Fstatistics")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("xpath=//span[@class='system-blue-shade-fat-btn-text']//strong[.='Log in']")
            sel.wait_for_page_to_load("60000")
            sel.click("id=startingDate")
            sel.click("xpath=//div[@id='ui-datepicker-div']//span[.='Prev']")
            sel.click("link=15")
            sel.click("id=endingDate")
            sel.click("xpath=//div[@id='ui-datepicker-div']//span[.='Prev']")
            sel.click("link=22")
            sel.click("xpath=//a[@id='leftTimeArrow']/span")
            sel.click("xpath=//a[@id='rightTimeArrow']/span")
            sel.click("xpath=//div[@id='ember287']//a[normalize-space(.)='quarter']")
            self.failUnless(sel.is_element_present("id=ember287"))
            self.failUnless(sel.is_element_present("id=startingDate"))
            self.failUnless(sel.is_element_present("id=endingDate"))
            self.failUnless(sel.is_element_present("xpath=//a[@id='leftTimeArrow']/span"))
            self.failUnless(sel.is_element_present("xpath=//a[@id='rightTimeArrow']/span"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='ember287']//a[normalize-space(.)='week']"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='ember287']//a[normalize-space(.)='month']"))
            self.failUnless(sel.is_element_present("xpath=//div[@id='ember287']//a[normalize-space(.)='quarter']"))
            self.failUnless(sel.is_element_present("xpath=//a[@id='leftTimeArrow']//div[.='Backward']"))
            self.failUnless(sel.is_element_present("xpath=//a[@id='rightTimeArrow']//div[.='Forward']"))
            sel.click("id=endingDate")
            sel.click("link=20")
            self.failUnless(sel.is_element_present("link=custom"))
    
            print self.__class__.__name__ + " passed!"       
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"

globals().update(make_platform_classes.make_platform_classes(TestInsightDatePicker))