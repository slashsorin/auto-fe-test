#-*- coding: utf-8 -*-
'''
    
    @author: Sorin

    Copyright Issuu Aps Sep 24, 2012
'''
import os
import glob
 
tests = glob.glob('test_insight/Test*.py')
for test in tests:
    os.system('python %s' % test)

