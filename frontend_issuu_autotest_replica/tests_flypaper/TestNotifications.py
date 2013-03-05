import sys

#sys.path.append('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/autotest_framework/')
sys.path.append('../autotest_framework')


import make_platform_classes
import SetTestStatus as sts

from SeleniumTestCase import SeleniumTestCase

import unittest, xmlrunner

class TestNotifications(SeleniumTestCase):
    
    def test_notifications(self):
        try:
            sel = self.selenium
            sel.set_speed("1000")
            sel.open("https://flypaper.issuu.com/signin?onLogin=http%3A%2F%2Fflypaper.issuu.com%2Fhome%2Fsettings%2Fnotifications")
            sel.wait_for_page_to_load("60000")
            sel.type("id=username", "sorintest")
            sel.type("id=password", "sorintest")
            sel.click("id=loginButton")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//a[@id='acceptButton']//strong[.='I accept the Terms of Service']")
            sel.wait_for_page_to_load("60000")
            sel.click("xpath=//label[@for='notify_docComments_false']//span[.='No']")
            sel.check("id=notify_docComments_false")
            sel.click("xpath=//label[@for='notify_profileComments_false']//span[.='No']")
            sel.check("id=notify_profileComments_false")
            sel.click("xpath=//label[@for='notify_documentCommentsAfterMe_false']//span[.='No']")
            sel.check("id=notify_documentCommentsAfterMe_false")
            sel.click("xpath=//label[@for='notify_profileCommentsAfterMe_false']//span[.='No']")
            sel.check("id=notify_profileCommentsAfterMe_false")
            sel.click("xpath=//label[@for='notify_myDocumentsBookmarked_false']//span[.='No']")
            sel.check("id=notify_myDocumentsBookmarked_false")
            sel.click("xpath=//label[@for='notify_myDocumentGrouped_false']//span[.='No']")
            sel.check("id=notify_myDocumentGrouped_false")
            sel.click("xpath=//label[@for='notify_invitationSignsUp_false']//span[.='No']")
            sel.check("id=notify_invitationSignsUp_false")
            sel.click("xpath=//label[@for='notify_friendRequestAccepted_false']//span[.='No']")
            sel.check("id=notify_friendRequestAccepted_false")
            sel.click("xpath=//label[@for='notify_followed_false']//span[.='No']")
            sel.check("id=notify_followed_false")
            sel.click("xpath=//label[@for='notify_friendUpload_false']//span[.='No']")
            sel.check("id=notify_friendUpload_false")
            sel.click("xpath=//label[@for='notify_groupsCommentsAfterMe_false']//span[.='No']")
            sel.check("id=notify_groupsCommentsAfterMe_false")
            sel.click("xpath=//label[@for='notify_newsletter_false']//span[.='No']")
            sel.check("id=notify_newsletter_false")
            sel.click("xpath=//form[@id='notifications']/p/input")
            sel.click("xpath=//label[@for='notify_newsletter_true']//span[.='Yes']")
            sel.check("id=notify_newsletter_true")
            sel.click("xpath=//label[@for='notify_groupsCommentsAfterMe_true']//span[.='Yes']")
            sel.check("id=notify_groupsCommentsAfterMe_true")
            sel.click("xpath=//label[@for='notify_friendUpload_true']//span[.='Yes']")
            sel.click("xpath=//label[@for='notify_followed_true']//span[.='Yes']")
            sel.check("id=notify_followed_true")
            sel.click("xpath=//form[@id='notifications']/fieldset[3]/div[4]/div/label[1]")
            sel.check("id=notify_friendUpload_true")
            sel.click("xpath=//label[@for='notify_friendRequestAccepted_true']//span[.='Yes']")
            sel.check("id=notify_friendRequestAccepted_true")
            sel.click("xpath=//label[@for='notify_invitationSignsUp_true']//span[.='Yes']")
            sel.check("id=notify_invitationSignsUp_true")
            sel.click("xpath=//label[@for='notify_myDocumentGrouped_true']//span[.='Yes']")
            sel.check("id=notify_myDocumentGrouped_true")
            sel.click("xpath=//label[@for='notify_myDocumentsBookmarked_true']//span[.='Yes']")
            sel.check("id=notify_myDocumentsBookmarked_true")
            sel.click("xpath=//label[@for='notify_profileCommentsAfterMe_true']//span[.='Yes']")
            sel.check("id=notify_profileCommentsAfterMe_true")
            sel.click("xpath=//label[@for='notify_documentCommentsAfterMe_true']//span[.='Yes']")
            sel.check("id=notify_documentCommentsAfterMe_true")
            sel.click("xpath=//label[@for='notify_profileComments_true']//span[.='Yes']")
            sel.check("id=notify_profileComments_true")
            sel.click("xpath=//label[@for='notify_docComments_true']//span[.='Yes']")
            sel.check("id=notify_docComments_true")
            sel.click("xpath=//form[@id='notifications']/p/input")
            
            #print self.__class__.__name__ + " passed!"       
            #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=True)
            
        except AttributeError:
            pass
        #except: # catch *all* exceptions
            #if  sys.exc_info()[1]:
                #print self.__class__.__name__ + " failed!"
                #sts.set_test_status(self.selenium.get_eval("selenium.sessionId"), passed=False)
        
globals().update(make_platform_classes.make_platform_classes(TestNotifications))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='../test-reports'))