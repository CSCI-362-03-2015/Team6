import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#print sys.argv
#name = sys.argv[1]
#print name

class PythonOrgSearch(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
	
	def test_search_in_python_org(self):

		driver = self.driver

		driver.implicitly_wait(10)

		driver.get("http://127.0.0.1:8000/eden/default/user/login?_next=%2Feden%2Fdefault%2Findex")

		#driver.get("http://127.0.0.1:8000/eden/default/index")
		#self.assertIn("Python", driver.title)

 		elem = driver.find_element_by_name("email")
		elem.send_keys("test")
		elem = driver.find_element_by_name("password")
		elem.send_keys("test" + Keys.RETURN)

		elem = driver.find_element_by_link_text("Login")
		elem.click

		assert "Invalid login" in driver.page_source


	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":

	unittest.main()
