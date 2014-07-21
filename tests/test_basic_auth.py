from . import TheInternetTestCase
from helium.api import Text

class BasicAuthTest(TheInternetTestCase):
	def get_page(self):
		return "http://admin:admin@the-internet.herokuapp.com/basic_auth"
	def test_basic_auth(self):
		self.assertTrue(Text("Basic Auth").exists())