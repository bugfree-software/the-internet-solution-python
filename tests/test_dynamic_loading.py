from . import TheInternetTestCase
from helium.api import click, wait_until, Text

class DynamicLoadingTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/dynamic_loading"
	def test_element_on_page_that_is_hidden(self):
		click("Example 1: Element on page that is hidden")
		self._load_and_assert()
	def test_element_rendered_after_the_fact(self):
		click("Example 2: Element rendered after the fact")
		self._load_and_assert()
	def _load_and_assert(self):
		click("Start")
		wait_until(lambda: not Text("Loading...").exists())
		self.assertTrue(Text("Hello World!").exists())