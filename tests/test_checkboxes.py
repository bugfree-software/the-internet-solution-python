from . import TheInternetTestCase
from helium.api import CheckBox

class CheckboxesTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/checkboxes"
	def test_checkboxes_exist(self):
		self.assertTrue(CheckBox("unchecked").exists())
		self.assertTrue(CheckBox("checked").exists())
	def test_is_checked(self):
		self.assertTrue(CheckBox("checked").is_checked())
		self.assertFalse(CheckBox("unchecked").is_checked())