"""
This example presents how Helium can be used to automatically test websites
on the example of the blog located at the homepage of Automa - Next Generation
GUI Automation Tool.
"""
from helium.api import *
import unittest

class TestAutomaBlog(unittest.TestCase):
	def setUp(self):
		self.ff = start_chrome("www.getautoma.com/blog")
	def test_display_posts_by_category(self):
		# find the link named "Software Testing" below the "Categories" header
		software_testing_category = Link(
			"Software Testing", below=Text("Categories")
		)
		self.assertTrue(software_testing_category.exists())
		click(software_testing_category)
		self.assertTrue(
			Text("Showing posts in category: Software Testing").exists()
		)
		self.assertTrue(Link("Show all").exists())
		click(Link("Show all"))
		self.assertFalse(
			Text("Showing posts in category: Software Testing").exists()
		)
	def tearDown(self):
		kill(self.ff)

# run the test
if __name__ == '__main__':
	unittest.main()