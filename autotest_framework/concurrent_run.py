from subprocess import Popen
import glob
import time
import os
import string
    
os.chdir('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/tests_free_account/')
start = time.time()

tests = glob.glob('Test*.py')

processes = []

for test in tests:
    x = string.rstrip(test, '.py')
    processes.append(Popen('python -m unittest %s' % x, shell=True))
    
for process in processes:
    process.wait()

print "*" * 50
print "Time taken: %s minutes" % ((time.time() - start) /60)

########################################################################################

os.chdir('/Users/Sorin/Issuu/new_eclipse_ws/frontend-issuu-autotest/tests_pro_account/')
start = time.time()

tests = glob.glob('Test*.py')

processes = []

for test in tests:
    x = string.rstrip(test, '.py')
    processes.append(Popen('python -m unittest %s' % x, shell=True))
    
for process in processes:
    process.wait()

print "*" * 50
print "Time taken: %s minutes" % ((time.time() - start)/60)