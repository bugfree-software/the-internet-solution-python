from helium.api import *
from unittest import TestCase

class DragAndDropTest(TestCase):
	def setUp(self):
		start_chrome("http://the-internet.herokuapp.com/drag_and_drop")
	def tearDown(self):
		kill_browser()
	def test_drag_and_drop(self):
		self.assertTrue(Text("A", to_left_of=Text("B")).exists())
		self.assertFalse(Text("A", to_right_of=Text("B")).exists())
		drag("A", "B")
		self.assertFalse(Text("A", to_left_of=Text("B")).exists())
		self.assertTrue(Text("A", to_right_of=Text("B")).exists())