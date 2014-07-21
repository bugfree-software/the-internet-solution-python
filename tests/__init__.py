from helium.api import get_driver, start_chrome, go_to, kill_browser
from unittest import TestCase

class TheInternetTestCase(TestCase):
	def setUp(self):
		start_chrome()
		get_driver().delete_all_cookies()
		go_to(self.get_page())
	def tearDown(self):
		kill_browser()
	def get_page(self):
		raise NotImplementedError()
