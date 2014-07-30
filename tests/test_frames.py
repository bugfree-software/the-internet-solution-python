from . import TheInternetTestCase
from helium.api import click, Text

class FramesTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/frames"
	def test_nested_frames(self):
		click("Nested Frames")
		self.assertTrue(Text("LEFT").exists())
		self.assertTrue(Text("MIDDLE").exists())
		self.assertTrue(Text("RIGHT").exists())
		self.assertTrue(Text("BOTTOM").exists())
	def test_iframe(self):
		click("iFrame")
		self.assertTrue(Text("Your content goes here.").exists())