from . import TheInternetTestCase
from helium.api import click, hover, Text

class JQueryUITest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/jqueryui/menu"
	def test_menu_navigation(self):
		self.assertTrue(Text("JQueryUI - Menu").exists())
		hover("Enabled")
		click("Back to JQuery UI")
		self.assertFalse(Text("JQueryUI - Menu").exists())
		self.assertTrue(
			Text(
				"JQuery UI is many things, but one thing specifically that "
				"causes automation challenges is their set of Widgets"
			).exists()
		)
		click("Menu")
		self.assertTrue(Text("JQueryUI - Menu").exists())