from . import TheInternetTestCase
from helium.api import click, Text, press, CONTROL, COMMAND, write
from sys import platform

class WYSIWYGEditorTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/tinymce"
	def test_use_wysiwyg_editor(self):
		self.assertTrue(Text("Your content goes here.").exists())
		click("Your content goes here.")
		if platform == 'darwin':
			press(COMMAND + 'a')
		else:
			press(CONTROL + 'a')
		write("Hello Helium!")
		self.assertTrue(Text("Hello Helium!").exists())