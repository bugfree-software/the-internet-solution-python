from helium.api import *
from unittest import TestCase

class AbTestingTest(TestCase):
	def setUp(self):
		start_chrome()
		get_driver().delete_all_cookies()
		go_to("http://the-internet.herokuapp.com/abtest")
	def tearDown(self):
		kill_browser()
	def test_ab_variates(self):
		variation = S("h3")
		first_variation = variation.web_element.text
		self.assertIn(
			first_variation, [u"A/B Test Variation 1", u"A/B Test Control"]
		)
		get_driver().delete_all_cookies()
		go_to("http://the-internet.herokuapp.com/abtest")
		variation = S("h3")
		second_variation = variation.web_element.text
		self.assertIn(
			second_variation, [u"A/B Test Variation 1", u"A/B Test Control"]
		)
		self.assertNotEqual(first_variation, second_variation)