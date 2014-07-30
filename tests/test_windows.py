from . import TheInternetTestCase
from helium.api import find_all, Window, click, Text, switch_to

class WindowsTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/windows"
	def test_open_new_window(self):
		windows = find_all(Window())
		self.assertEqual(len(windows), 1)
		self.assertTrue(Text("Opening a new window").exists())
		main_window = windows[0]
		click("Click Here")
		windows = find_all(Window())
		self.assertEqual(len(windows), 2)
		self.assertTrue(Text("New Window").exists())
		switch_to(main_window)
		self.assertTrue(Text("Opening a new window").exists())