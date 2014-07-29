from . import TheInternetTestCase
from helium.api import go_to, S, get_driver

class AbTestingTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/abtest"
	def test_ab_variates(self):
		header = S("h3")
		first_variation = header.web_element.text
		self.assertIn(
			first_variation, [u"A/B Test Variation 1", u"A/B Test Control"]
		)
		second_variation = first_variation
		while second_variation == first_variation:
			get_driver().delete_all_cookies()
			go_to("http://the-internet.herokuapp.com/abtest")
			header = S("h3")
			second_variation = header.web_element.text
			self.assertIn(
				second_variation, [u"A/B Test Variation 1", u"A/B Test Control"]
			)
		self.assertNotEqual(first_variation, second_variation)