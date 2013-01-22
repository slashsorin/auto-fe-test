#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Jul 11, 2012
'''

import unittest
import sys
import argparse
import SauceParams
import cfg

import concurrent_run

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Issuu Frontend Test Framework.")
        
    parser.add_argument('run_domain', metavar='runDomain', action='store', help='The test domain can be: http://issuu.com, http://adpages-uat.issuu.com, http://web2.issuu.com, http://tissuu.com, etc...')
    
    args = parser.parse_args()
    
    tp = SauceParams.GetParams()
    
    tp.run_domain = args.run_domain
    
    print tp
    '''
    tp.run_domain = 'http://' + str(args.run_domain) + '.com'
    
    print tp.run_domain
    '''
    cfg.config['base-url'] = 'http://' + str(tp) + '.com'
    
    print cfg.config['base-url']
    
    sys.argv = [sys.argv[0], "concurrent_run"]