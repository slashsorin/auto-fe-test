import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

class TestExploreDebugMode(SeleniumTestCase):
    
    def test_explore_debug_mode(self):
        try:
            sel = self.selenium
            sel.open("/explore?debug")
            sel.wait_for_page_to_load("60000")
            try: self.failUnless(sel.is_text_present("solr_category_static:Business"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("solr_segment"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("solr_category_static:Learning"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("infobox"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("editors_picks"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("trending"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("solr_category_static:Health(local)"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("solr_category_static:Learning(local)"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("solr_categort_static:News(local)"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("solr_category_static:Art & Design(local)"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("solr_category_static:Home & Garden"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("solr_category_static:Style & Beauty(local)"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("solr_category_static:Media & Entertainment"))
            except AssertionError, e: self.verificationErrors.append(str(e))
            try: self.failUnless(sel.is_text_present("solr_category_static:Computers & Technology"))
            except AssertionError, e: self.verificationErrors.append(str(e))
        
            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
        
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #print self.__class__.__name__ + " failed!"
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
    
globals().update(make_platform_classes.make_platform_classes(TestExploreDebugMode))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test-reports'))