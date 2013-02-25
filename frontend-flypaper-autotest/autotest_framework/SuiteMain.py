'''
Created on May 2, 2012

@author: Sorin
'''
import unittest
import Parameters

import TestAbout
import TestAboutPeople
import TestBookmarks
import TestBookmarksReceived
import TestBusiness
import TestCases
import TestCommentsReceived
import TestContact
import TestCopyright, TestDMCA, TestDocs, TestFAQ, TestFeatures, TestGraphics, TestHowTo, TestJoinUs, TestParentTerms, TestPress, TestPrivacy
import TestProTerms, TestShareOverlay, TestSubscribers, TestSubscriptions, TestTerms, TestUserConnections, TestUserPage

import sys
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Issuu Frontend Test Framework.")
    
    parser.add_argument('place', metavar='placeToRunOn', action='store', help='The environment on which the tests will be run. The values for this can be: local OR sauce')
    parser.add_argument('test_browser', metavar='testBrowser', action='store', help='The browser which will be used in the tests. This can be: *firefox, *googlechrome, *safariproxy (for MAC) and *iexplore (for Windows)')
    parser.add_argument('run_domain', metavar='runDomain', action='store', help='The test domain can be: http://issuu.com, http://adpages-uat.issuu.com, http://web2.issuu.com, http://tissuu.com, etc...')
    
    args = parser.parse_args()

    tp = Parameters.GetParams()

    tp.place = args.place
    tp.test_browser = args.test_browser
    tp.run_domain = args.run_domain
    
    sys.argv = [sys.argv[3], "TestAb"]
    
    '''
    sys.argv = [sys.argv[3], "TestAbout", "TestAboutPeople", "TestBookmarks", "TestBookmarksReceived", "TestBusiness", "TestCases", "TestCommentsReceived", "TestContact",
                            "TestCopyright", "TestDMCA", "TestDocs", "TestFAQ", "TestFeatures", "TestGraphics", "TestHowTo", "TestJoinUs", "TestParentTerms", "TestPress",
                            "TestPrivacy", "TestProTerms", "TestShareOverlay", "TestSubscribers", "TestSubscriptions", "TestTerms", "TestUserConnections", "TestUserPage"]
    '''
    TestAbout.unittest.main() 
    '''
    TestAboutPeople.unittest.main()
    TestBookmarks.unittest.main()
    TestBookmarksReceived.unittest.main()
    TestBusiness.unittest.main()
    TestCases.unittest.main()
    TestCommentsReceived.unittest.main()
    TestContact.unittest.main()
    TestCopyright.unittest.main()
    TestDMCA.unittest.main()
    TestDocs.unittest.main()
    TestFAQ.unittest.main()
    TestFeatures.unittest.main()
    TestGraphics.unittest.main()
    TestHowTo.unittest.main()
    TestJoinUs.unittest.main()
    TestParentTerms.unittest.main()
    TestPress.unittest.main()
    TestPrivacy.unittest.main()
    TestProTerms.unittest.main()
    TestShareOverlay.unittest.main()
    TestSubscribers.unittest.main()
    TestSubscriptions.unittest.main()
    TestTerms.unittest.main()
    TestUserConnections.unittest.main()
    TestUserPage.unittest.main()
    '''