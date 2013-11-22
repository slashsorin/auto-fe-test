"""
Helium can be used to perform Google searches
"""
from helium.api import *
start_firefox("google.com")
write("Helium")
press(ENTER)
click("Helium - Wikipedia, the free encyclopedia")