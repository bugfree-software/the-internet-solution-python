from . import TheInternetTestCase
from helium.api import find_all, Text, click, S

class TablesTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/tables"
	def test_table_sorting_example1(self):
		last_names = [
			txt.value
			for txt in find_all(Text(below="Last Name", above="Example 2"))
		]
		self.assertTrue(len(last_names) == 4)
		# assert its not sorted
		self.assertNotEqual(last_names, sorted(last_names))
		click("Last Name")
		sorted_last_names = [
			txt.value
			for txt in find_all(Text(below="Last Name", above="Example 2"))
		]
		self.assertEqual(sorted_last_names, sorted(last_names))
	def test_table_sorting_example2(self):
		last_names = [
			txt.web_element.text for txt in find_all(S("td.last-name"))
		]
		self.assertTrue(len(last_names) == 4)
		# assert its not sorted
		self.assertNotEqual(last_names, sorted(last_names))
		click(S("span.last-name"))
		sorted_last_names = [
			elem.web_element.text for elem in find_all(S("td.last-name"))
		]
		self.assertEqual(sorted_last_names, sorted(last_names))