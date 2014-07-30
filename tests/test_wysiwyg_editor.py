from . import TheInternetTestCase
from helium.api import click, Text, write

class WYSIWYGEditorTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/tinymce"
	def test_use_wysiwyg_editor(self):
		self.assertTrue(Text("Your content goes here.").exists())
		click("File")
		click("New document")
		write("Hello Helium!")
		self.assertTrue(Text("Hello Helium!").exists())