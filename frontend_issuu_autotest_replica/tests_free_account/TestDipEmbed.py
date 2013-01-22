import sys, time, os
sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')

import SeleniumTestCase, make_platform_classes
import SetTestStatus as sts

class TestDipEmbed(SeleniumTestCase.SeleniumTestCase):
    
    def test_dip_embed(self):
        try:
            sel = self.selenium
            sel.set_speed("1500")
            sel.open("/sorintest/docs/dev_sauce_ondemand_service")
            sel.wait_for_page_to_load("60000")
            sel.set_timeout("1000")
            sel.click("xpath=//li[@class='embed']/a/span[1]")
            sel.set_speed("500")
            self.failUnless(sel.is_element_present("xpath=//form[@id='skema']/div"))
            self.failUnless(sel.is_element_present("xpath=//form[@id='skema']/div/div[2]"))
            self.failUnless(sel.is_element_present("name=embedCode"))
            self.failUnless(sel.is_element_present("name=url"))
            sel.click("xpath=//h3[@class='showHideEmbedOptions']//strong[.='ShowHide embed options']")
            self.failUnless(sel.is_text_present("Hide embed options"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='previewBox']/div/object/embed"))
            sel.check("id=l2")
            sel.check("id=l1")
            sel.check("id=s3")
            sel.check("id=l2")
            sel.select("xpath=//div[@class='showHideEmbedOptionsContent']/div[3]/div[2]/select", "Red")
            sel.check("id=showTittleAndAutorId")
            sel.click("xpath=//div[@class='showHideEmbedOptionsContent']/div[5]/div[2]/div[2]/div")
            sel.click("link=the old embed page")
            self.failUnless(sel.is_element_present("name=embedCode"))
            self.failUnless(sel.is_element_present("name=url"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='d_main']/div/form/div/div[2]/div[7]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='d_main']/div/form/div/div[2]"))
            self.failUnless(sel.is_element_present("xpath=//div[@class='d_main']/div/form/div/div[2]/div[5]"))
            sel.click("link=Blogger")
            sel.click("link=Orkut")
            sel.click("link=MySpace")
            sel.click("xpath=//div[@class='span-2menu']//a[.='Facebook']")
            sel.click("link=WordPress")
            sel.click("link=Joomla")
            sel.click("link=Typepad")
            sel.click("link=LiveJournal")
            sel.click("xpath=//a[@id='switchToV2']/span[1]")
            sel.click("link=the old embed page")
            sel.click("xpath=//a[@id='switchToV2']/span[1]")
            self.failUnless(sel.is_element_present("xpath=//div[@class='dia_box']/div"))
            sel.click("xpath=//div[@class='dia_box']/div")
            
            print self.__class__.__name__ + " passed!"
            sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True) 
            
        except AttributeError:
            pass
        except: # catch *all* exceptions
            if  sys.exc_info()[1]:
                sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
                print self.__class__.__name__ + " failed!"
    
globals().update(make_platform_classes.make_platform_classes(TestDipEmbed))
