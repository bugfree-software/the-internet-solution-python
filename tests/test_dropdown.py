from . import TheInternetTestCase
from helium.api import ComboBox, select

class DropdownTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/dropdown"
	def test_dropdown_exists(self):
		self.assertTrue(ComboBox("Dropdown List").exists())
	def test_select_value(self):
		self.assertEqual(
			ComboBox("Dropdown List").value, u'Please select an option'
		)
		select("Dropdown List", "Option 1")
		self.assertEqual(
			ComboBox("Dropdown List").value, u'Option 1'
		)
		select("Dropdown List", "Option 2")
		self.assertEqual(
			ComboBox("Dropdown List").value, u'Option 2'
		)