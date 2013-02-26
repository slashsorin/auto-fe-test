from subprocess import Popen
import glob
import time
import os
import string

def test_fun(path):
    os.chdir(path)
    start = time.time()
    tests = glob.glob('Test*.py')

    processes = []
    
    for test in tests:
        #processes.append(Popen('python %s' %test, shell=True))
        x = string.rstrip(test, '.py')
        processes.append(Popen('python -m unittest %s' % x, shell=True))
        
    print "*" * 50
    print "Time taken: %s minutes" % ((time.time() - start) /60)
    os.chdir('..')

for p in ['tests_flypaper']:
    test_fun(p)