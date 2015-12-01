import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
	
	def test_search_in_python_org(self):

		driver = self.driver

		driver.implicitly_wait(10)

		driver.get("http://127.0.0.1:8000/eden/gis/index")
	
		assert "View Fullscreen Map" in driver.page_source


	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":

	unittest.main()
